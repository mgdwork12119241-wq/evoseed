from evoseed.core import EvolutionLedger, next_generation


def test_generations_are_monotonic(tmp_path):
    ledger = EvolutionLedger(tmp_path / ".evoseed")
    first = next_generation(ledger, "improve the seed")
    second = next_generation(ledger, "add a measurable capability")

    assert first.number == 1
    assert second.number == 2
    assert second.parent == "generation-0001"
    assert ledger.latest().number == 2
