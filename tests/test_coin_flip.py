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
    times_to_test = 1_000
    times_reached, avg_steps_taken = markov_chain.run(SeenSequence(None, None), (SeenSequence("H", "T"),), times_to_test, seed=2)[0]
    assert pytest.approx(4, abs=0.1) == avg_steps_taken
    assert times_reached == times_to_test

    times_reached, avg_steps_taken = markov_chain.run(SeenSequence(None, None), (SeenSequence("H", "H"),), times_to_test, seed=2)[0]
    assert pytest.approx(6, abs=0.1) == avg_steps_taken
    assert times_reached == times_to_test
