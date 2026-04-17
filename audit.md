# Semantic Scholar Python Library — Audit

## SemanticScholar.py (761 lines, main client class)
- Type hints: Y — function signatures typed, but uses older
  typing.List / typing.Union instead of modern list / | syntax
  (ruff UP rule would flag these)
- Docstrings: Y — class and methods have Sphinx-style docstrings
- Tests: Y — single test file exists (tests/test_semanticscholar.py)
- Error handling: None in this file. Delegated entirely to
  AsyncSemanticScholar and ApiRequester.
- Hardcoded config: api_url defaults to None, passed through to
  AsyncSemanticScholar
- Notes: Sync class wraps an async class via _run_async helper.
  Clean API surface with consistent method signatures.

## ApiRequester.py (error handling layer)
- Type hints: (check)
- Docstrings: Y
- Tests: Covered by the 130 tests in test_semanticscholar.py
- Error handling: Good. Uses tenacity retry with specific
  exception type (ConnectionRefusedError). No bare except blocks.
- Notes: This is where the actual HTTP and retry logic lives.
  Worth studying the tenacity pattern for your own runner.py later.

## Codebase-wide observations
- No bare except blocks anywhere. All error handling uses specific
  exception types.
- 130 tests in a single test file.
- Consistent use of type hints, though older typing module style
  throughout (List, Union, Tuple instead of list, |, tuple).
- Custom exception class (SemanticScholarException.py) exists.
- Async/sync pattern: AsyncSemanticScholar does the real work,
  SemanticScholar wraps it synchronously via _run_async.

## Modules ranked by learning value
1. ApiRequester.py — retry logic with tenacity, HTTP handling.
   Directly useful for your runner.py in the Authority Drift project.
2. AsyncSemanticScholar.py — the real implementation. Good for
   understanding async patterns if needed for P1 FastAPI work.
3. PaginatedResults.py — iterator pattern over API responses.
   Common pattern worth knowing.
4. SemanticScholar.py — clean API surface but thin wrapper.
5. Model classes (Paper.py, Author.py, etc.) — data modeling
   patterns, comparable to your Pydantic models.


