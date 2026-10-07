# Threat model sketch (bridge)

**Orientation only. Not a complete threat model or assurance case.**

## Assets

- Isolation between parallel nets
- Integrity of the grant set (who may cross)
- Clarity of public claims (no false sense of production bridging)

## Adversary goals (illustrative)

- Cause cross-net influence without a grant
- Expand a grant beyond its pair (direction or net identity confusion)
- Convince operators that default-deny is active when it is not enforced

## In scope for this repository

- Policy logic errors in the **reference** grant/send checks
- Documentation that weakens default-deny

## Out of scope (must be handled elsewhere if ever deployed)

- Network-level spoofing of `net_id`
- Compromise of nodes that hold grant authority
- Side channels and covert cross-net channels via shared hardware
- Supply-chain attacks on binaries

## Mitigations reflected in the sketch

- Default-deny
- Explicit ordered pairs
- No self-grants
- Fail-closed parsing in the reference client

## Residual risk statement

Even a correct policy module can be bypassed if enforcement is not on the real path of effects.  
Reference tests do not prove deployment correctness.