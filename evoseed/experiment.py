from __future__ import annotations

from dataclasses import dataclass

from .evaluator import Evaluation, Evaluator
from .goals import Goal
from .mutation import Mutation, MutationEngine


@dataclass(frozen=True)
class Experiment:
    generation: int
    goal: Goal
    mutation: Mutation
    evaluation: Evaluation


class EvolutionExperiment:
    """Runs the first deterministic evolution loop without an AI provider."""

    def __init__(self) -> None:
        self.mutations = MutationEngine()
        self.evaluator = Evaluator()

    def run(self, generation: int, goal: Goal, *, tests_passed: bool, quality_score: float) -> Experiment:
        mutation = self.mutations.propose(goal.objective)
        evaluation = self.evaluator.evaluate(
            tests_passed=tests_passed,
            quality_score=quality_score,
        )
        return Experiment(generation, goal, mutation, evaluation)
