from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Goal:
    name: str
    objective: str
    metric: str
    constraints: tuple[str, ...] = ()


DEFAULT_GOAL = Goal(
    name="self-improvement-baseline",
    objective="Improve the quality of EvoSeed while preserving existing behavior.",
    metric="tests_passed_and_quality_score",
    constraints=(
        "preserve_existing_tests",
        "never_modify_main_directly",
        "bounded_mutation",
    ),
)
