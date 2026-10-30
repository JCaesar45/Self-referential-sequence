# SEQUENCE

A self-contained, single-file implementation of the self-referential sequence algorithm described in the Rosetta Code task, wrapped in a dark-luxury product interface with tiered access modeling.

## What it actually does

The engine takes a seed integer and generates successive terms by counting digit frequencies in the previous term, then concatenating `count + digit` pairs sorted from largest digit to smallest. Digits not present in the previous term are excluded. The sequence terminates when a term repeats. For seed `40`, the chain converges in 11 terms. For seed `22`, it converges immediately (the next term is also `22`).

Reference: Rosetta Code, "Self-referential sequence" . The algorithm is deterministic and language-agnostic. The same seed always produces the same chain.

## Product structure

Three tiers model differentiated access to the engine:

| Tier | Price | Core constraint |
|---|---|---|
| Seed | $0 | 10-term limit, local execution |
| Converge | $19/mo | Unlimited terms, batch processing, export |
| Equilibrium | $149/mo | REST API, SLA, webhook convergence alerts |

The tiers are presentational scaffolding. No backend exists. The "API" and "SLA" are narrative elements, not functional services. This is honest about what the artifact is: a demonstration of algorithmic convergence presented through a commercial lens.

## Why single-file

A self-referential sequence generator has no legitimate need for a database, an authentication layer, a Python service, or a Java daemon. The algorithm is pure function: `String -> String[]`. Embedding it in a React app with a FastAPI backend would add infrastructure without adding capability. The single-file constraint is a deliberate architectural choice, not a limitation.

## Running it

Open the HTML file in any modern browser. No build step, no dependencies, no network calls beyond the Google Fonts stylesheet (which degrades gracefully to system fonts if blocked).

## Algorithm verification

```
selfReferential("40")
→ ["40","1410","142110","14123110","1413124110",
   "2413125110","151413224110","152413225110",
   "251413324110","152423224110","152413423110"]
```

```
selfReferential("132211")
→ ["132211","132231","232221","134211",
   "14131231","14231241","24132231","14233221"]
```

Both match the expected outputs from the Rosetta Code test cases .

## License

MIT. The algorithm belongs to mathematics. The interface belongs to whoever wants to improve it.
```
