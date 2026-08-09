# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Type hints throughout the codebase.
- `to_dict()` method replacing the old `dict()` method.
- `MemInfo.dict()` kept as a deprecated alias with `DeprecationWarning`.
- Test suite with pytest (~25 tests).
- CI/CD with GitHub Actions (lint + test on Python 3.10–3.14, PyPI publishing).
- `pyproject.toml` based packaging (replaces `setup.py`/`distutils`).

### Changed

- **BREAKING**: `get()` now uses exact key matching instead of prefix matching.
- **BREAKING**: `get()` returns `None` instead of crashing when no numeric value is found.
- **BREAKING**: `search()` returns stripped lines (no trailing `\n`).
- **BREAKING**: `__repr__` returns `MemInfo(path='...')` instead of the full file contents.
- **BREAKING**: `fileobj()` renamed to `_open()` (private API).
- `to_dict()` uses `partition(":")` for more robust parsing.
- Minimum Python version is now 3.10.

### Removed

- `setup.py` and `MANIFEST` (replaced by `pyproject.toml`).
- Manual metadata dunder variables in `__init__.py` (version now from `importlib.metadata`).
- Python 2.x support.

## [0.4.1] - 2017-08-15

### Changed

- Python 3 compatibility.

[unreleased]: https://github.com/barnumbirr/hazelnut/compare/v0.4.1...HEAD
[0.4.1]: https://github.com/barnumbirr/hazelnut/releases/tag/v0.4.1
