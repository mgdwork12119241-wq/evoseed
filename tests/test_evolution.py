from evoseed.evaluator import Evaluator
from evoseed.mutation import MutationEngine


def test_evaluator_rejects_failed_tests():
    result = Evaluator().evaluate(tests_passed=False, quality_score=90)
    assert not result.passed
    assert "tests_failed" in result.reasons


def test_evaluator_accepts_good_candidate():
    result = Evaluator().evaluate(tests_passed=True, quality_score=80)
    assert result.passed
    assert result.score == 80


def test_mutation_is_bounded():
    mutation = MutationEngine().propose("improve tests", files=("a.py",))
    assert mutation.goal == "improve tests"
    assert mutation.files == ("a.py",)
