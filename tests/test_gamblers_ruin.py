from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

import markov_chain

if TYPE_CHECKING:
    from random import Random


@dataclass(frozen=True)
class Game:
    david: int
    goliath: int
    round_bet: int

    def transition(self, k: int, rnd: Random) -> Game:
        win_odds = 0.45
        match rnd.random() < win_odds:
            case True:
                return Game(
                    self.david - self.round_bet,
                    self.goliath + self.round_bet,
                    self.round_bet,
                )
            case False:
                return Game(
                    self.david + self.round_bet,
                    self.goliath - self.round_bet,
                    self.round_bet,
                )


def test_gamblers_ruin() -> None:
    times_to_test = 1_000
    david_wins, goliath_wins = markov_chain.run(Game(2_000, 10_000, 1_000), (Game(12_000, 0, 1_000), Game(0, 12_000, 1_000)), times_to_test, seed=2)
    assert david_wins[0] + goliath_wins[0] == times_to_test
    assert david_wins[0] < goliath_wins[0]
    david_wins, goliath_wins = markov_chain.run(Game(2_000, 10_000, 500), (Game(12_000, 0, 500), Game(0, 12_000, 500)), times_to_test, seed=2)
    assert david_wins[0] + goliath_wins[0] == times_to_test
    assert david_wins[0] > goliath_wins[0]
    david_wins, goliath_wins = markov_chain.run(Game(2_000, 10_000, 200), (Game(12_000, 0, 200), Game(0, 12_000, 200)), times_to_test, seed=2)
    assert david_wins[0] + goliath_wins[0] == times_to_test
    assert david_wins[0] > goliath_wins[0]
    david_wins, goliath_wins = markov_chain.run(Game(2_000, 10_000, 100), (Game(12_000, 0, 100), Game(0, 12_000, 100)), times_to_test, seed=2)
    assert david_wins[0] + goliath_wins[0] == times_to_test
    assert david_wins[0] > goliath_wins[0]
