from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal

import pytest

import markov_chain

if TYPE_CHECKING:
    from random import Random

type Side = Literal["H", "T"]


@dataclass(frozen=True)
class SeenSequence:
    a: None | Side
    b: None | Side

    def transition(self, k: int, rnd: Random) -> SeenSequence:
        return SeenSequence(self.b, rnd.choice(("H", "T")))


def test_coin_flip() -> None:
    assert pytest.approx(4, abs=0.1) == markov_chain.run(SeenSequence(None, None), SeenSequence("H", "T"), 1_000, seed=2)
    assert pytest.approx(6, abs=0.1) == markov_chain.run(SeenSequence(None, None), SeenSequence("H", "H"), 1_000, seed=2)
