# EvoSeed 🧬

**EvoSeed** is an experimental open-source system for evolving software through **tested, observable generations**.

The project starts with a small seed. Each future generation may propose improvements, build them, test them, measure them, and keep only changes that satisfy explicit rules.

> EvoSeed is not intended to be a self-aware system. It is a controlled engineering experiment in AI-assisted software evolution.

## Core loop

```text
Seed
  ↓
Observe
  ↓
Propose
  ↓
Change in an isolated branch/workspace
  ↓
Build + Test + Measure
  ↓
Evaluate
  ├── pass → next generation
  └── fail → reject / rollback
```

## Generation 0

The first implementation deliberately does **not** give an AI unrestricted write access to the repository. It establishes the transparent generation ledger and automated test gate first.

Current components:

- `evoseed/core.py` — generation model and append-only ledger
- `evoseed/cli.py` — command-line interface
- `tests/` — regression tests
- `.github/workflows/test.yml` — GitHub Actions test gate

## Roadmap

1. **Seed** — establish a minimal measurable software seed.
2. **Evaluator** — score candidate changes against explicit metrics.
3. **Mutation engine** — generate isolated candidate changes.
4. **AI adapter** — optionally ask a configured model for improvement proposals.
5. **Sandbox** — constrain execution and repository access.
6. **Evolution controller** — accept/reject generations automatically.
7. **Supabase memory** — store experiments, metrics, failures, and lineage.
8. **Dashboard** — visualize the project's evolution over time.

Every accepted generation should remain reproducible and auditable through Git history.

## License

MIT. See [LICENSE](LICENSE).
