from aic_interop import BridgePolicy, SendResult


def test_default_deny():
    p = BridgePolicy(nets={"a", "b"})
    assert p.send("a", "b") is SendResult.DENIED


def test_grant_allows_directional():
    p = BridgePolicy(nets={"a", "b"})
    assert p.grant("a", "b")
    assert p.send("a", "b") is SendResult.ALLOWED
    assert p.send("b", "a") is SendResult.DENIED


def test_revoke():
    p = BridgePolicy(nets={"a", "b"})
    p.grant("a", "b")
    assert p.revoke("a", "b")
    assert p.send("a", "b") is SendResult.DENIED


def test_unknown_net_denied():
    p = BridgePolicy(nets={"a"})
    assert p.grant("a", "missing") is False
    assert p.send("a", "missing") is SendResult.DENIED


def test_no_self_grant():
    p = BridgePolicy(nets={"a"})
    assert p.grant("a", "a") is False
    assert p.send("a", "a") is SendResult.DENIED


def test_add_net_then_grant():
    p = BridgePolicy(nets={"a"})
    assert p.add_net("b")
    assert p.grant("a", "b")
    assert p.is_granted("a", "b")