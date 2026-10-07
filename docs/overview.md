# Overview — AIC-Interop

## Problem

Parallel TestNets are intended to explore phases and configurations **side by side**.  
Without a strict isolation rule, experiments can accidentally influence each other, collapsing the value of “parallel” and creating unclear trust boundaries.

## Approach

1. Each net has a distinct `net_id`.
2. By default, **no** message or state effect crosses from one net to another.
3. Cross-net effect requires an **explicit, ordered grant** `<<from, to>>`.
4. Grants can be revoked; after revoke, new cross-net sends are denied again.
5. Self-bridge (`from == to`) is unnecessary and disallowed in the sketch.

## Reference vs deployment

The Python package under `reference/python` implements **policy checks in process**.  
It does not move packets on a real network.  
Any future wiring into AIC-TestNet must preserve default-deny at the enforcement point, not only in documentation.

## Formal link

AIC-Formal models a related invariant (`Inv_DefaultDenyBridge`):  
messages appear in the cross-net set only if a matching grant exists.  
This repository is the engineering-facing sketch and reference client for that idea.