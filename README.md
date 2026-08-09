<h1><img src="https://raw.githubusercontent.com/barnumbirr/hazelnut/master/doc/hazelnut.png" height=85 alt="hazelnut" title="hazelnut"> hazelnut</h1>

[![PyPi Version](https://img.shields.io/pypi/v/hazelnut.svg)](https://pypi.python.org/pypi/hazelnut/)

**hazelnut** is an Apache licensed library written in Python designed to
provide a simple and pythonic way to parse `/proc/meminfo` on Linux based
systems.

Supports Python 3.10, 3.11, 3.12, 3.13, and 3.14.

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

Search (case insensitive):

```python
>>> mem.search('Swap')
['SwapCached:         7576 kB', 'SwapTotal:      16776188 kB', 'SwapFree:       16639112 kB']
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

## License

```
Copyright 2014-2026 Martin Simon

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
WDC : WbcWJzVD8yXt3yLnnkCZtwQo4YgSUdELkj
HBN : F2Zs4igv8r4oJJzh4sh4bGmeqoUxLQHPki
DOGE: DRBkryyau5CMxpBzVmrBAjK6dVdMZSBsuS
```
