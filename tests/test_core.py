from __future__ import annotations

import warnings

import pytest

from hazelnut import MemInfo

SAMPLE_MEMINFO = """\
MemTotal:        8092460 kB
MemFree:          499880 kB
MemAvailable:    5454920 kB
Buffers:          219088 kB
Cached:          4980040 kB
SwapCached:         7576 kB
Active:          5647392 kB
Inactive:        1628708 kB
Active(anon):    1794356 kB
Inactive(anon):   492656 kB
Active(file):    3853036 kB
Inactive(file):  1136052 kB
Unevictable:         200 kB
Mlocked:             200 kB
SwapTotal:      16776188 kB
SwapFree:       16639112 kB
Dirty:               172 kB
Writeback:             0 kB
AnonPages:       2070440 kB
Mapped:           204800 kB
Shmem:            210036 kB
Slab:             247884 kB
SReclaimable:     219356 kB
SUnreclaim:        28528 kB
KernelStack:        4144 kB
PageTables:        11904 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:    20822416 kB
Committed_AS:    3317504 kB
VmallocTotal:   34359738367 kB
VmallocUsed:      362844 kB
VmallocChunk:   34359347296 kB
HardwareCorrupted:     0 kB
AnonHugePages:         0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
DirectMap4k:       83644 kB
DirectMap2M:     8202240 kB
"""


@pytest.fixture()
def meminfo(tmp_path):
    path = tmp_path / "meminfo"
    path.write_text(SAMPLE_MEMINFO)
    return MemInfo(path=str(path))


# --- __version__ ---


def test_version_is_accessible():
    from hazelnut import __version__

    assert isinstance(__version__, str)
    assert __version__ == "1.0.0"


# --- __str__ ---


def test_str_returns_all_lines(meminfo):
    output = str(meminfo)
    lines = output.splitlines()
    assert len(lines) == 43
    assert "MemTotal:" in output
    assert "DirectMap2M:" in output


def test_str_lines_are_stripped(meminfo):
    for line in str(meminfo).splitlines():
        assert line == line.strip()


# --- __repr__ ---


def test_repr_format(meminfo):
    assert repr(meminfo).startswith("MemInfo(path=")


def test_repr_contains_path(meminfo):
    assert meminfo.path in repr(meminfo)


# --- to_dict ---


def test_to_dict_returns_dict(meminfo):
    d = meminfo.to_dict()
    assert isinstance(d, dict)


def test_to_dict_keys_have_no_colon(meminfo):
    for key in meminfo.to_dict():
        assert ":" not in key


def test_to_dict_known_value(meminfo):
    d = meminfo.to_dict()
    assert d["MemTotal"] == "8092460 kB"


def test_to_dict_value_without_unit(meminfo):
    d = meminfo.to_dict()
    assert d["HugePages_Total"] == "0"


def test_to_dict_key_with_parens(meminfo):
    d = meminfo.to_dict()
    assert d["Active(anon)"] == "1794356 kB"


def test_to_dict_all_keys_present(meminfo):
    d = meminfo.to_dict()
    assert len(d) == 43


# --- dict (deprecated alias) ---


def test_dict_returns_same_as_to_dict(meminfo):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        assert meminfo.dict() == meminfo.to_dict()


def test_dict_emits_deprecation_warning(meminfo):
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        meminfo.dict()
        assert len(w) == 1
        assert issubclass(w[0].category, DeprecationWarning)
        assert "to_dict" in str(w[0].message)


# --- search ---


def test_search_case_insensitive(meminfo):
    results = meminfo.search("swap")
    assert len(results) == 3
    assert results[0].startswith("SwapCached:")
    assert results[1].startswith("SwapTotal:")
    assert results[2].startswith("SwapFree:")


def test_search_returns_stripped_lines(meminfo):
    for line in meminfo.search("Mem"):
        assert line == line.strip()
        assert "\n" not in line


def test_search_no_match(meminfo):
    assert meminfo.search("NonExistent") == []


def test_search_key_with_parens(meminfo):
    results = meminfo.search(r"Active\(anon\)")
    assert len(results) == 1
    assert "1794356" in results[0]


# --- get ---


def test_get_known_key(meminfo):
    assert meminfo.get("MemTotal") == 8092460


def test_get_exact_match_not_prefix(meminfo):
    result = meminfo.get("Mem")
    assert result is None


def test_get_missing_key(meminfo):
    assert meminfo.get("NoSuchKey") is None


def test_get_key_with_parens(meminfo):
    assert meminfo.get("Active(anon)") == 1794356


def test_get_value_without_unit(meminfo):
    """HugePages_Total has no 'kB' suffix and no trailing whitespace."""
    assert meminfo.get("HugePages_Total") == 0


def test_get_zero_value_with_unit(meminfo):
    assert meminfo.get("Writeback") == 0


def test_get_large_value(meminfo):
    assert meminfo.get("VmallocTotal") == 34359738367


# --- edge cases ---


def test_empty_file(tmp_path):
    path = tmp_path / "empty"
    path.write_text("")
    mem = MemInfo(path=str(path))
    assert mem.to_dict() == {}
    assert mem.search("anything") == []
    assert mem.get("MemTotal") is None
    assert str(mem) == ""


def test_file_not_found():
    mem = MemInfo(path="/nonexistent/path")
    with pytest.raises(FileNotFoundError):
        mem.to_dict()


def test_line_with_no_numeric_value(tmp_path):
    path = tmp_path / "weird"
    path.write_text("SomeKey:   no_digits_here\n")
    mem = MemInfo(path=str(path))
    assert mem.get("SomeKey") is None
    assert mem.to_dict() == {"SomeKey": "no_digits_here"}
