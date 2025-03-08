from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Literal

import markov_chain

type Side = Literal["H", "T"]


@dataclass
class SeenSequence:
    a: None | Side
    b: None | Side

    def transition(self, k: int) -> None:
        self.a = self.b
        self.b = random.choice(("H", "T"))


def test_coin_flip() -> None:
    print("ALICE")
    print(markov_chain.run(SeenSequence(None, None), SeenSequence("H", "T"), 1_000))
    print("BOB")
    print(markov_chain.run(SeenSequence(None, None), SeenSequence("H", "H"), 1_000))
