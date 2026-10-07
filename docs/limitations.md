# Limitations

1. **Not a production bridge** — no performance, availability, or security certification.
2. **In-process policy only** — the reference client does not move real TestNet traffic.
3. **No cryptography** — grants are plain data structures; authenticity is out of scope.
4. **No multi-hop** — only direct `(from, to)` pairs.
5. **Formal models are separate** — see AIC-Formal; this repo does not replace model checking.
6. **Pre-Covenant** — no mainnet or Covenant declaration.
7. **Entity ≠ immunity** — use of these materials creates no special legal status.
8. **Under-claim** — “tests passed” means the reference code matched its own rules, nothing more.