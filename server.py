from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, field_validator
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
import httpx
import os

from self_referential import self_referential

app = FastAPI(title="SEQUENCE API", version="1.0.0")

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class SeedRequest(BaseModel):
    seed: str
    webhook_url: str | None = None

    @field_validator("seed")
    @classmethod
    def seed_must_be_digits(cls, v: str) -> str:
        if not v.isdigit():
            raise ValueError("seed must contain only digits")
        if len(v) > 128:
            raise ValueError("seed exceeds maximum length of 128 digits")
        return v


class SequenceResponse(BaseModel):
    seed: str
    chain: list[str]
    terms: int
    stable_value: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/sequence", response_model=SequenceResponse)
@limiter.limit("30/minute")
async def sequence(request: Request, body: SeedRequest):
    try:
        chain = self_referential(body.seed)
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))

    response = SequenceResponse(
        seed=body.seed,
        chain=chain,
        terms=len(chain),
        stable_value=chain[-1],
    )

    if body.webhook_url:
        async with httpx.AsyncClient(timeout=5.0) as client:
            try:
                await client.post(body.webhook_url, json=response.model_dump())
            except httpx.HTTPError:
                pass

    return response
