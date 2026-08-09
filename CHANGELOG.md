# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- Type hints, shipped with a `py.typed` marker.
- `to_dict()`, replacing `dict()` (kept as a deprecated alias).
- `MemInfo(path=...)` accepts `os.PathLike` paths.

### Changed

- **BREAKING**: `search()` matches the pattern against keys with
  `re.search` semantics — `search("total")` now finds `MemTotal`.
- **BREAKING**: `get()` uses exact key matching instead of prefix
  matching, and returns `None` instead of crashing on values without digits.
- **BREAKING**: `search()` returns stripped lines (no trailing `\n`).
- **BREAKING**: `repr()` returns `MemInfo(path='...')` instead of the file contents.
- Minimum supported Python is 3.10 (Python 2 support dropped).

### Removed

- **BREAKING**: `fileobj()` (now private).
- `__title__`, `__author__`, `__repo__` and `__license__`; `__version__` remains.
- `setup.py`/`MANIFEST` packaging (replaced by `pyproject.toml`).

## [0.4.1] - 2017-08-15

### Changed

- Python 3 compatibility.

[unreleased]: https://github.com/barnumbirr/hazelnut/compare/v0.4.1...HEAD
[0.4.1]: https://github.com/barnumbirr/hazelnut/releases/tag/v0.4.1
