from __future__ import annotations

from typing import Literal, Protocol, Self


class State(Protocol):
    def transition(self, k: int) -> None: ...


def run[T: State](initial: T, goal: T, n: int, max_iterations: int = -1) -> float:
    sum: int = 0
    for _ in range(n):
        sum += _run(initial, goal, max_iterations)

    return sum / n


def _run(initial: State, goal: State, max_iterations: int) -> int:
    k = 0
    match max_iterations:
        case -1:
            expr = lambda: True
        case _:
            expr = lambda: k <= max_iterations

    # print(f"k={k} state={initial}")
    while expr():
        initial.transition(k)
        k += 1
        # print(f"k={k} state={initial}")
        if initial == goal:
            break
    return k
