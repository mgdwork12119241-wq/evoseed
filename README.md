# EvoSeed 🧬

**An open-source experimental engine for AI-assisted software evolution.**

EvoSeed explores a simple question:

> Can an AI-driven software system discover, test, measure, and retain useful improvements across generations without a human writing every patch by hand?

This project is an experiment in **autonomous software engineering**, not a claim of consciousness or unrestricted self-replication.

## The idea

```text
Goal
  ↓
AI proposes a bounded mutation
  ↓
Candidate is isolated
  ↓
Build + tests + measurements
  ↓
Evaluator scores the candidate
  ↓
Reject or accept
  ↓
Generation N+1
```

The AI proposes. The evaluation system decides. Every accepted change should be observable in Git history and reproducible from an experiment record.

## Why build it?

Most AI coding tools generate a patch and stop. EvoSeed asks what happens when proposal, execution, testing, measurement, and selection become a repeatable loop.

Potential uses include:

- automated refactoring experiments
- performance optimization searches
- test-quality improvement
- bug-fix candidate generation
- comparing AI models on software-engineering tasks
- research into evolutionary and autonomous software engineering

## What it is not

EvoSeed is **not** designed to give an AI unrestricted access to credentials, infrastructure, or the internet. It should not grant itself permissions, bypass review, or create uncontrolled execution loops.

The project follows a principle of:

> **Self-improvement without self-authorization.**

## AI providers

The architecture is provider-oriented. OpenAI can be used as the first provider through the `OPENAI_API_KEY` GitHub Actions secret. The secret must never be committed to the repository.

A provider is responsible for proposing candidate changes; EvoSeed's evaluator remains responsible for acceptance.

## First experiment

The initial goal is deliberately narrow:

> Improve the quality of EvoSeed while preserving existing behavior.

Success is measured using passing tests and a quality score. Mutations are bounded and `main` is protected by policy.

The experiment should progress in stages:

1. deterministic evaluator
2. AI proposal provider
3. isolated candidate generation
4. automated build/test/evaluation
5. generation records
6. controlled acceptance of better candidates
7. comparison of multiple models and strategies

## GitHub Worker

GitHub Actions acts as the repeatable worker environment. A future evolution workflow can:

1. load a goal
2. call the configured AI provider
3. create an isolated candidate
4. run tests and benchmarks
5. calculate a score
6. publish an experiment artifact
7. open a reviewable pull request when a candidate is better

The worker should have explicit limits on runtime, files changed, generations, and API usage.

## Observability

Each generation should record:

- generation number
- goal
- model/provider
- proposal
- files changed
- test result
- quality/performance metrics
- score
- acceptance decision
- rejection reason

This makes the experiment inspectable rather than magical.

## Roadmap

- [x] Initial repository and MIT license
- [x] Generation model
- [x] Deterministic evaluator
- [x] Bounded mutation engine
- [x] Explicit goal model
- [x] First experiment loop
- [x] GitHub Actions test worker
- [ ] OpenAI provider
- [ ] Candidate isolation
- [ ] Automatic experiment artifacts
- [ ] Generation ledger
- [ ] Reviewable automatic pull requests
- [ ] Multi-model comparison
- [ ] Evolution dashboard

## License

MIT
