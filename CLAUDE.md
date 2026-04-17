# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
uv sync --dev          # Install all dependencies including dev tools
uv run pytest          # Run all tests
uv run pytest tests/test_foo.py::test_name  # Run a single test
uv run ruff check .    # Lint
uv run ruff check --fix .  # Lint with auto-fix
uv run mypy src/       # Type check
```

## Architecture

This is an early-stage Python package using the `src/` layout:

- `src/authority_drift_training/` — main package source
- `tests/` — pytest test suite
- `pyproject.toml` — project config, tool settings, and dev dependencies managed by `uv`

**Tooling:**
- `uv` for dependency management and running tools
- `ruff` for linting (rules: E, F, I, UP; line length 88)
- `mypy` in strict mode
- `pytest` for tests

All three (ruff, mypy, pytest) must pass in CI before merging.
