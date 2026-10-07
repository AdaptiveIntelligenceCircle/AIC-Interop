#!/usr/bin/env python3
"""Default-deny bridge demo (in-process, experimental)."""

from aic_interop import BridgePolicy, SendResult


def main() -> None:
    print("AIC-Interop bridge demo")
    print("Pre-Covenant / under-claim / default-deny\n")

    policy = BridgePolicy(nets={"net0", "net1", "net2"})

    r0 = policy.send("net0", "net1", {"msg": "hello"})
    print(f"send net0->net1 without grant: {r0.value}")
    assert r0 is SendResult.DENIED

    assert policy.grant("net0", "net1") is True
    r1 = policy.send("net0", "net1", {"msg": "hello"})
    print(f"send net0->net1 after grant:    {r1.value}")
    assert r1 is SendResult.ALLOWED

    # Directional: reverse still denied
    r2 = policy.send("net1", "net0", {"msg": "back"})
    print(f"send net1->net0 (no reverse):   {r2.value}")
    assert r2 is SendResult.DENIED

    assert policy.revoke("net0", "net1") is True
    r3 = policy.send("net0", "net1", {"msg": "again"})
    print(f"send net0->net1 after revoke:   {r3.value}")
    assert r3 is SendResult.DENIED

    # Self-bridge rejected
    assert policy.grant("net0", "net0") is False
    print("self-grant net0->net0: rejected")

    print("\nGrants:", list(policy.grants_list()))
    print("Done.")


if __name__ == "__main__":
    main()