from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import json
from pathlib import Path


@dataclass(frozen=True)
class Generation:
    number: int
    parent: str | None
    goal: str
    status: str
    score: float
    created_at: str

    @classmethod
    def create(cls, number: int, parent: str | None, goal: str, status: str = "proposed", score: float = 0.0) -> "Generation":
        return cls(number, parent, goal, status, score, datetime.now(timezone.utc).isoformat())


class EvolutionLedger:
    """Append-only local ledger for transparent generation history."""

    def __init__(self, root: str | Path = ".evoseed") -> None:
        self.root = Path(root)
        self.path = self.root / "generations.jsonl"

    def record(self, generation: Generation) -> None:
        self.root.mkdir(parents=True, exist_ok=True)
        with self.path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(asdict(generation), sort_keys=True) + "\n")

    def all(self) -> list[Generation]:
        if not self.path.exists():
            return []
        rows: list[Generation] = []
        for line in self.path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(Generation(**json.loads(line)))
        return rows

    def latest(self) -> Generation | None:
        rows = self.all()
        return rows[-1] if rows else None


def next_generation(ledger: EvolutionLedger, goal: str) -> Generation:
    previous = ledger.latest()
    number = 1 if previous is None else previous.number + 1
    parent = None if previous is None else f"generation-{previous.number:04d}"
    generation = Generation.create(number, parent, goal)
    ledger.record(generation)
    return generation
