from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Evaluation:
    passed: bool
    score: float
    reasons: tuple[str, ...]


class Evaluator:
    """Deterministic gate for candidate generations.

    EvoSeed deliberately starts with a conservative evaluator. AI-generated
    mutations must pass explicit checks before they can become a generation.
    """

    def evaluate(self, *, tests_passed: bool, quality_score: float) -> Evaluation:
        score = max(0.0, min(100.0, float(quality_score)))
        reasons: list[str] = []
        if not tests_passed:
            reasons.append("tests_failed")
        if score < 50.0:
            reasons.append("score_below_threshold")
        return Evaluation(
            passed=not reasons,
            score=score,
            reasons=tuple(reasons),
        )
