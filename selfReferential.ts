export function selfReferential(seed: string | number): string[] {
  const seen = new Set<string>();
  const chain: string[] = [];
  let current = String(seed);

  while (!seen.has(current)) {
    seen.add(current);
    chain.push(current);

    const counts: Record<string, number> = {};
    for (const ch of current) {
      counts[ch] = (counts[ch] ?? 0) + 1;
    }

    const digits = Object.keys(counts).sort((a, b) => Number(b) - Number(a));
    current = digits.map((d) => `${counts[d]}${d}`).join("");
  }

  return chain;
}
