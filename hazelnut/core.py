from __future__ import annotations

import os
import re
import warnings
from collections.abc import Iterator
from typing import TextIO

_DIGITS_RE = re.compile(r"(\d+)")


class MemInfo:
    """Interface to parse ``/proc/meminfo`` on Linux systems.

    Every method reads the file afresh, so consecutive calls reflect the
    memory usage at the time of each call. Methods that read the file --
    including ``str()`` -- raise ``OSError`` (e.g. ``FileNotFoundError``)
    when it cannot be opened.
    """

    def __init__(self, path: str | os.PathLike[str] = "/proc/meminfo") -> None:
        self.path = os.fspath(path)

    def _open(self) -> TextIO:
        return open(self.path, encoding="utf-8")

    def _parse_lines(self) -> Iterator[tuple[str, str]]:
        """Yield ``(key, value)`` pairs from the meminfo file."""
        with self._open() as f:
            for line in f:
                key, sep, value = line.partition(":")
                if sep:
                    yield key.strip(), value.strip()

    def __str__(self) -> str:
        with self._open() as f:
            return "\n".join(line.strip() for line in f)

    def __repr__(self) -> str:
        return f"MemInfo(path={self.path!r})"

    def to_dict(self) -> dict[str, str]:
        """Return meminfo contents as a dictionary.

        Keys are the field names (without the colon), values are the
        remainder of the line (e.g. ``"8092460 kB"`` or ``"0"``).
        """
        return dict(self._parse_lines())

    def dict(self) -> dict[str, str]:
        """Deprecated: use :meth:`to_dict` instead."""
        warnings.warn(
            "MemInfo.dict() is deprecated, use MemInfo.to_dict() instead",
            DeprecationWarning,
            stacklevel=2,
        )
        return self.to_dict()

    def search(self, regex: str) -> list[str]:
        """Return lines whose key matches *regex* (case-insensitive).

        The pattern is matched against the key only (the part before the
        colon) with :func:`re.search` semantics, so ``search("total")``
        finds ``MemTotal`` and ``SwapTotal``. Anchor with ``^`` to match
        from the start of the key.
        """
        matcher = re.compile(regex, re.IGNORECASE)
        results = []
        with self._open() as f:
            for line in f:
                key, sep, _ = line.partition(":")
                if sep and matcher.search(key):
                    results.append(line.strip())
        return results

    def get(self, key: str) -> int | None:
        """Return the leading integer of the value for an exact *key*.

        Units are discarded: most meminfo values are expressed in kB
        (kibibytes), while some (e.g. ``HugePages_Total``) are plain
        counts. Returns ``None`` when the key is missing or its value
        contains no digits.
        """
        for name, value in self._parse_lines():
            if name == key:
                match = _DIGITS_RE.search(value)
                return int(match.group(1)) if match else None
        return None
