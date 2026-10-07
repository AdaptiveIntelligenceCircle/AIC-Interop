"""
Default deny bridge policy (in process reference)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Iterable, Mapping, MutableSet, Optional, Set, Tuple


NetId = str
Grant = Tuple[NetId, NetId]


class SendResult(str, Enum):
    ALLOWED = "allowed"
    DENIED = "denied"


@dataclass
class BridgePolicy:
    """In-memory default-deny bridge grants between parallel nets.

    Cross-net send is denied unless an explicit ordered grant exists.
    """

    nets: Set[NetId] = field(default_factory=set)
    grants: MutableSet[Grant] = field(default_factory=set)

    def __post_init__(self) -> None:
        self.nets = {n for n in self.nets if n}
        # Drop invalid grants if any were passed in
        self.grants = {
            (a, b)
            for (a, b) in self.grants
            if a and b and a != b and a in self.nets and b in self.nets
        }

    def add_net(self, net_id: NetId) -> bool:
        if not net_id or net_id in self.nets:
            return False
        self.nets.add(net_id)
        return True

    def known(self, net_id: NetId) -> bool:
        return bool(net_id) and net_id in self.nets

    def grant(self, from_net: NetId, to_net: NetId) -> bool:
        if not self.known(from_net) or not self.known(to_net):
            return False
        if from_net == to_net:
            return False
        pair = (from_net, to_net)
        if pair in self.grants:
            return False
        self.grants.add(pair)
        return True

    def revoke(self, from_net: NetId, to_net: NetId) -> bool:
        pair = (from_net, to_net)
        if pair not in self.grants:
            return False
        self.grants.discard(pair)
        return True

    def is_granted(self, from_net: NetId, to_net: NetId) -> bool:
        return (from_net, to_net) in self.grants

    def send(
        self,
        from_net: NetId,
        to_net: NetId,
        payload: Optional[Mapping] = None,
    ) -> SendResult:
        """Policy check only — does not deliver payload anywhere."""
        _ = payload  # reserved for future mock delivery hooks
        if not self.known(from_net) or not self.known(to_net):
            return SendResult.DENIED
        if from_net == to_net:
            return SendResult.DENIED
        if self.is_granted(from_net, to_net):
            return SendResult.ALLOWED
        return SendResult.DENIED

    def grants_list(self) -> Iterable[Grant]:
        return sorted(self.grants)