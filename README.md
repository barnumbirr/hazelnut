<h1><img src="https://raw.githubusercontent.com/barnumbirr/hazelnut/master/doc/hazelnut.png" height=85 alt="hazelnut" title="hazelnut"> hazelnut</h1>

[![PyPI Version](https://img.shields.io/pypi/v/hazelnut.svg)](https://pypi.org/project/hazelnut/)
[![Python Versions](https://img.shields.io/pypi/pyversions/hazelnut.svg)](https://pypi.org/project/hazelnut/)
[![CI](https://github.com/barnumbirr/hazelnut/actions/workflows/ci.yml/badge.svg)](https://github.com/barnumbirr/hazelnut/actions/workflows/ci.yml)

**hazelnut** is an Apache licensed library written in Python designed to
provide a simple and pythonic way to parse `/proc/meminfo` on Linux based
systems.

## Installation

```
pip install hazelnut
```

## Usage

```python
>>> from hazelnut import MemInfo
>>> mem = MemInfo()
>>> repr(mem)
"MemInfo(path='/proc/meminfo')"
```

Print all meminfo contents:

```python
>>> print(mem)
MemTotal:        8092460 kB
MemFree:          499880 kB
...
```

Return output as dict:

```python
>>> mem.to_dict()
{
    "MemTotal": "8092460 kB",
    "MemFree": "499880 kB",
    "Buffers": "219088 kB",
    "HugePages_Total": "0",
    ...
}
```

Search keys (case-insensitive, matches anywhere in the key — anchor with `^` if needed):

```python
>>> mem.search('total')
['MemTotal:        8092460 kB', 'SwapTotal:      16776188 kB', 'VmallocTotal:   34359738367 kB', 'HugePages_Total:       0']
```

Get memory value as int (exact key match):

```python
>>> mem.get('MemTotal')
8092460
>>> mem.get('Active(anon)')
1794356
>>> mem.get('NoSuchKey') is None
True
```

Values are returned as bare integers with the unit dropped: most fields
are expressed in kB (kibibytes), a few (e.g. `HugePages_Total`) are
plain counts.

## License

```
Copyright 2015-2026 Martin Simon

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## Buy me a coffee?

If you feel like buying me a coffee (or a beer?), donations are welcome:

```
BTC : bc1qq04jnuqqavpccfptmddqjkg7cuspy3new4sxq9
DOGE: DRBkryyau5CMxpBzVmrBAjK6dVdMZSBsuS
ETH : 0x2238A11856428b72E80D70Be8666729497059d95
LTC : MQwXsBrArLRHQzwQZAjJPNrxGS1uNDDKX6
```
