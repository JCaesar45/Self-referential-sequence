from typing import List


def self_referential(seed) -> List[str]:
    seen = set()
    chain = []
    current = str(seed)

    while current not in seen:
        seen.add(current)
        chain.append(current)

        counts = {}
        for ch in current:
            counts[ch] = counts.get(ch, 0) + 1

        digits = sorted(counts.keys(), key=int, reverse=True)
        current = "".join(f"{counts[d]}{d}" for d in digits)

    return chain


if __name__ == "__main__":
    import json
    import sys

    seed = sys.argv[1] if len(sys.argv) > 1 else "40"
    print(json.dumps(self_referential(seed), indent=2))
