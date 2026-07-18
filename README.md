# fj

Local platform for algorithmic problems and programming contests.

The project is intended as a self-hosted competitive programming system (similar to a local Codeforces-like setup):
- creating and running contests;
- managing a catalog of problems and tests;
- submitting solutions with automatic judging;
- basic analytics for attempts and results.

The repository is currently under active development.

## Status

MVP is in progress. Interfaces and internal architecture may change.

## Structure

The monorepo is split into packages and services:
- `packages/` - shared libraries (application, config, core, db, domain, observability);
- `services/` - application services (api, worker, scheduler).

## Quick Start

Detailed setup instructions will be added later.

Current high-level flow (via `uv`):
1. Install `uv`.
2. From the repository root, install workspace dependencies:

```bash
uv sync --all-packages --group dev
```

3. Run services only through `uv run`.

API:
```bash
uv run --package api uvicorn api.app:app --reload
```

Code checks:
```bash
ruff format
ruff check --fix
ty check
```

## Roadmap (draft)

- auth and roles system foundations;
- full solution judging pipeline;
- UI for contests and standings;
- local deployment via a single compose stack.

## License

See `LICENSE`.
