# Default-deny bridge design

**Experimental. Pre-Covenant. Under-claim.**

## Definitions

| Term | Meaning in this sketch |
|------|------------------------|
| **Net** | An isolated parallel network identified by `net_id` |
| **Grant** | Explicit permission for ordered pair `(from_net, to_net)` |
| **Send attempt** | Request to carry an effect from one net toward another |
| **Default-deny** | Absent grant ⇒ attempt fails; no implicit trust |

## State (conceptual)

- `bridge_granted`: set of ordered pairs `(from, to)` with `from ≠ to`
- Cross-net **effects** only recorded or applied when `(from, to) ∈ bridge_granted` at the time of enforcement

## Operations

1. **GrantBridge(from, to)**  
   - Preconditions: `from` and `to` are known nets, `from ≠ to`  
   - Effect: add `(from, to)` to `bridge_granted`

2. **RevokeBridge(from, to)**  
   - Effect: remove `(from, to)` if present  
   - Ongoing or future sends using that pair fail after revoke (sketch does not define in-flight delivery semantics beyond “new attempts denied”)

3. **Send(from, to, payload)**  
   - If `(from, to) ∈ bridge_granted` → allow path (reference client returns success)  
   - Else → **deny** (fail-closed)

## Directionality

Grants are **directional**.  
`(A, B)` does not imply `(B, A)`.  
Symmetric communication requires two grants.

## What is not decided here

- Authentication of grant issuers
- Wire encoding of payloads
- Reliability, ordering, or replay
- Multi-hop paths (A→B→C): only direct grants are in scope
- Economic or token conditions for grants (**forbidden** as protocol rule-power)

## Failure posture

When uncertain (unknown net, malformed pair, missing grant): **deny**.