from __future__ import annotations

from random import Random
from typing import Protocol, Self


class State(Protocol):
    def transition(self, k: int, rnd: Random) -> Self: ...


def run[T: State](initial: T, goals: tuple[T, ...], n: int, max_iterations: int = -1, seed: int | None = None) -> tuple[tuple[int, float], ...]:
    rnd = Random(seed)
    times_reached_steps_taken = [[0, 0] for _ in range(len(goals))]
    for _ in range(n):
        goal_reached, time_taken = _run(initial, goals, max_iterations, rnd)
        times_reached_steps_taken[goal_reached][0] += 1
        times_reached_steps_taken[goal_reached][-1] += time_taken
    return tuple((times_reached, steps / n) for times_reached, steps in times_reached_steps_taken)


def _run[T: State](initial: T, goals: tuple[T, ...], max_iterations: int, rnd: Random) -> tuple[int, int]:
    k = 0
    match max_iterations:
        case -1:
            expr = lambda: True
        case _:
            expr = lambda: k <= max_iterations

    while expr():
        initial = initial.transition(k, rnd)
        k += 1
        for idx, goal in enumerate(goals):
            if initial == goal:
                return idx, k
    raise NotImplementedError
