# AIC-Interop

**Default-deny bridge design notes and a minimal reference client for Parallel TestNet isolation experiments.**

Status: **pre-Covenant**, experimental, under-claim.  
This repository describes how cross-net influence **should default to deny**, and provides a small reference implementation of grant / revoke / send policy checks.  
It is **not** a production bridge, not a networking stack, and not a declaration of mainnet interop.

## Purpose

- Document the **default-deny** posture between parallel nets (`net_id` isolation).
- Provide a **minimal reference client** that only allows cross-net effects when an explicit bridge grant exists.
- Align with formal intent from AIC-Formal (`Inv_DefaultDenyBridge` in the Isolation model).
- Keep all claims experimental and reversible.

## Explicit non-goals

| This repository does | This repository does **not** |
|----------------------|------------------------------|
| Specify default-deny bridge policy sketches | Ship a production multi-net fabric |
| Offer a minimal in-process / mock reference client | Guarantee secure real-world bridging |
| Support grant / revoke / attempt-send checks | Implement full transport, crypto, or consensus |
| Stay under-claim and pre-Covenant | Claim Parallel TestNets are linked in production |

## Layout

```
AIC-Interop/
├── README.md
├── LICENSE
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── SECURITY.md
├── docs/
│   ├── overview.md
│   ├── default-deny-bridge.md
│   ├── threat-model-sketch.md
│   ├── running.md
│   └── limitations.md
├── specs/
│   └── bridge-policy-sketch.md
├── reference/python/          # minimal reference client
│   ├── aic_interop/
│   ├── examples/
│   └── tests/
├── schemas/
├── examples/
└── scripts/
```

## Core rule (one sentence)

**Cross-net messages and state influence are denied unless a specific ordered grant `<<from_net, to_net>>` is present.**

## Quick start (Python reference)

```bash
cd reference/python
PYTHONPATH=. python3 examples/bridge_demo.py
PYTHONPATH=. python3 -m pytest tests/ -q
```

## Relationship to other AIC repositories

- **AIC-Formal** (`parallel_nets/Isolation.tla`) — formal default-deny invariant.
- **AIC-TestNet / Parallel TestNet** — intended environment for experimental nets with `net_id`.
- **AIC-Reference-Clients** — shared Decision vocabulary; this repo focuses on **bridge policy**, not Ethical Kernel evaluate.
- **AIC-Security-Harness** — may later fuzz bridge policy parsers; not required here.

## Principles observed

- **Default-deny** between nets.
- **Explicit grant** for any cross-net effect.
- **Under-claim** public language.
- **No token rule-power** over bridge grants.
- **Entity ≠ immunity**.
- **Pre-Covenant** — no main surface declaration.

## License

GPL-3.0-or-later (see LICENSE).

## Maintenance note

During reduced maintainer availability the repository remains public.  

Contributions that preserve default-deny and under-claim posture are welcome.
