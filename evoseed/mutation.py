from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Mutation:
    goal: str
    description: str
    files: tuple[str, ...]


class MutationEngine:
    """Produces bounded mutation proposals; it never edits files itself."""

    def propose(self, goal: str, *, files: tuple[str, ...] = ()) -> Mutation:
        if len(files) > 10:
            raise ValueError("mutation scope exceeds the default 10-file limit")
        return Mutation(
            goal=goal,
            description=f"Propose a bounded change to improve: {goal}",
            files=files,
        )
