function selfReferential(n) {
  const seen = new Set();
  const result = [];
  let current = String(n);

  while (!seen.has(current)) {
    seen.add(current);
    result.push(current);

    // Count occurrences of each digit in current
    const counts = {};
    for (const ch of current) {
      counts[ch] = (counts[ch] || 0) + 1;
    }

    // Sort digits largest to smallest
    const digits = Object.keys(counts).sort((a, b) => b - a);

    // Build next term: concatenate count + digit for each
    let next = "";
    for (const d of digits) {
      next += String(counts[d]) + d;
    }

    current = next;
  }

  return result;
}
