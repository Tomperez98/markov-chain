from __future__ import annotations

from random import Random
from typing import Protocol, Self


class State(Protocol):
    def transition(self, k: int, rnd: Random) -> Self: ...


def run[T: State](initial: T, goal: T, n: int, max_iterations: int = -1, seed: int | None = None) -> float:
    rnd = Random(seed)
    sum: int = 0
    for _ in range(n):
        sum += _run(initial, goal, max_iterations, rnd)
    return sum / n


def _run(initial: State, goal: State, max_iterations: int, rnd: Random) -> int:
    k = 0
    match max_iterations:
        case -1:
            expr = lambda: True
        case _:
            expr = lambda: k <= max_iterations

    while expr():
        initial = initial.transition(k, rnd)
        k += 1
        if initial == goal:
            break
    return k
