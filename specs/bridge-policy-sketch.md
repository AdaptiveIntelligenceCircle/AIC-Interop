# Bridge policy sketch (normative for the reference client)

**Status: experimental sketch for AIC-Interop reference code. Pre-Covenant.**

## Nets

- Finite set `Nets` of non-empty string identifiers.
- `net_id` values are opaque strings in the reference client.

## Grants

- `Grants ⊆ Nets × Nets`
- Invariant: `∀ (a,b) ∈ Grants. a ≠ b`

## API (reference)

```
grant(from, to) -> bool
revoke(from, to) -> bool
is_granted(from, to) -> bool
send(from, to, payload) -> SendResult
```

`SendResult` is one of:

- `allowed` — grant present at check time
- `denied` — missing grant, unknown net, or invalid pair

## Rules

1. `grant(a, a)` always fails.
2. `grant(a, b)` fails if `a ∉ Nets` or `b ∉ Nets`.
3. `send(a, b, _)` returns `allowed` only if `(a, b) ∈ Grants`.
4. After `revoke(a, b)`, subsequent `send(a, b, _)` returns `denied` unless granted again.
5. Unknown or empty net ids → deny.

## Non-rules (explicitly excluded)

- Implicit transitive trust
- Token balance conditions
- Global “allow all parallel nets” switch in this sketch