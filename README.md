<h1><img src="https://raw.githubusercontent.com/mrsmn/hazelnut/master/doc/hazelnut.png" height=85 alt="hazelnut" title="hazelnut"> hazelnut</h1>

[![PyPi Version](http://img.shields.io/pypi/v/hazelnut.svg)](https://pypi.python.org/pypi/hazelnut/)


**hazelnut** is an APACHE licensed library written in Python designed to provide a simple and pythonic way to parse the _/proc/meminfo_ file on LINUX based systems.
This library has been tested with Python 2.7.x and Python 3.6.x.


## Installation:

From source use

		$ python setup.py install

or install from PyPi

		$ pip install hazelnut

## Documentation:

- Basic use:

```python
>>> from hazelnut import MemInfo
>>> mem = MemInfo()
>>> mem
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
```

- Return output as dict:

```python
>>> mem.dict()
{
	"WritebackTmp": "0 kB",
	"SwapTotal": "16776188 kB",
	"Active(anon)": "1794356 kB",
	"SwapFree": "16639112 kB",
	"DirectMap4k": "83644 kB",
	"KernelStack": "4144 kB",
	"MemFree": "499880 kB",
	"HugePages_Rsvd": "0",
	"Committed_AS": "3317504 kB",
	"SUnreclaim": "28528 kB",
	"NFS_Unstable": "0 kB",
	"VmallocChunk": "34359347296 kB",
	"Writeback": "0 kB",
	"Inactive(file)": "1136052 kB",
	"MemTotal": "8092460 kB",
	"VmallocUsed": "362844 kB",
	"HugePages_Free": "0",
	"AnonHugePages": "0 kB",
	"Shmem": "210036 kB",
	"AnonPages": "2070440 kB",
	"Active": "5647392 kB",
	"Inactive(anon)": "492656 kB",
	"HugePages_Total": "0",
	"Hugepagesize": "2048 kB",
	"Cached": "4980040 kB",
	"SwapCached": "7576 kB",
	"VmallocTotal": "34359738367 kB",
	"Dirty": "172 kB",
	"Mapped": "204800 kB",
	"Unevictable": "200 kB",
	"SReclaimable": "219356 kB",
	"MemAvailable": "5454920 kB",
	"Slab": "247884 kB",
	"DirectMap2M": "8202240 kB",
	"HugePages_Surp": "0",
	"Bounce": "0 kB",
	"Inactive": "1628708 kB",
	"PageTables": "11904 kB",
	"HardwareCorrupted": "0 kB",
	"CommitLimit": "20822416 kB",
	"Mlocked": "200 kB",
	"Buffers": "219088 kB",
	"Active(file)": "3853036 kB"
}
```

- Search (is case insensitive):

```python
>>> mem.search('Swap')
['SwapCached:         7576 kB\n', 'SwapTotal:      16776188 kB\n', 'SwapFree:       16639112 kB\n']
```

- Get memory usage as int (is case sensitive):

```python
>>> mem.get('Inactive(anon)')
492656
```

## License:

```
Copyright 2014-2017 Martin Simon

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
