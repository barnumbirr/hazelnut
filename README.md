<h1><img src="https://raw.githubusercontent.com/c0ding/hazelnut/master/doc/hazelnut.png" height=85 alt="hazelnut" title="hazelnut"> hazelnut</h1>

[![PyPi Version](http://img.shields.io/pypi/v/hazelnut.svg)](https://pypi.python.org/pypi/hazelnut/)   [![Downloads](http://img.shields.io/pypi/dm/hazelnut.svg)](https://pypi.python.org/pypi/hazelnut/)
[![Code Health](https://landscape.io/github/c0ding/hazelnut/master/landscape.svg)](https://landscape.io/github/c0ding/hazelnut/master)

**hazelnut** is an APACHE licensed library written in Python designed to provide a simple and pythonic way to parse the _/proc/meminfo_ file on LINUX based systems.

## Installation:

From source use

		$ python setup.py install

or install from PyPi

		$ pip install hazelnut
		
## Documentation:

- Basic use:

```
>>> from hazelnut import MemInfo
>>> mem = MemInfo()
>>> mem
MemTotal:        8092252 kB
MemFree:         5444872 kB
MemAvailable:    7138880 kB
Buffers:          484724 kB
Cached:          1299716 kB
SwapCached:            0 kB
Active:          1732744 kB
Inactive:         671312 kB
Active(anon):     509420 kB
Inactive(anon):   111312 kB
Active(file):    1223324 kB
Inactive(file):   560000 kB
Unevictable:           0 kB
Mlocked:               0 kB
SwapTotal:      16776188 kB
SwapFree:       16776188 kB
Dirty:                 0 kB
Writeback:             0 kB
AnonPages:        619632 kB
Mapped:            96216 kB
Shmem:              1120 kB
Slab:             184200 kB
SReclaimable:     159252 kB
SUnreclaim:        24948 kB
KernelStack:        3856 kB
PageTables:         5664 kB
NFS_Unstable:          0 kB
Bounce:                0 kB
WritebackTmp:          0 kB
CommitLimit:    20822312 kB
Committed_AS:    1755880 kB
VmallocTotal:   34359738367 kB
VmallocUsed:      362896 kB
VmallocChunk:   34359343324 kB
HardwareCorrupted:     0 kB
AnonHugePages:         0 kB
HugePages_Total:       0
HugePages_Free:        0
HugePages_Rsvd:        0
HugePages_Surp:        0
Hugepagesize:       2048 kB
DirectMap4k:       97980 kB
DirectMap2M:     8187904 kB
```

- Return output as dict:

```
>>> mem.dict()
{
	"Inactive:": "671312 kB",
	"Mlocked:": "0 kB",
	"HardwareCorrupted:": "0 kB",
	"Bounce:": "0 kB",
	"Active:": "1746544 kB",
	"Cached:": "1299720 kB",
	"Unevictable:": "0 kB",
	"SReclaimable:": "159256 kB",
	"DirectMap2M:": "8187904 kB",
	"Buffers:": "484736 kB",
	"Hugepagesize:": "2048 kB",
	"MemAvailable:": "7126028 kB",
	"HugePages_Rsvd:": "0",
	"Inactive(anon):": "111312 kB",
	"CommitLimit:": "20822312 kB",
	"SUnreclaim:": "24940 kB",
	"Inactive(file):": "560000 kB",
	"SwapCached:": "0 kB",
	"HugePages_Total:": "0",
	"Active(file):": "1223340 kB",
	"Writeback:": "0 kB",
	"Dirty:": "0 kB",
	"PageTables:": "5700 kB",
	"Shmem:": "1120 kB",
	"MemFree:": "5432004 kB",
	"Mapped:": "96256 kB",
	"WritebackTmp:": "0 kB",
	"Slab:": "184196 kB",
	"HugePages_Free:": "0",
	"AnonPages:": "633396 kB",
	"HugePages_Surp:": "0",
	"DirectMap4k:": "97980 kB",
	"Committed_AS:": "1774860 kB",
	"VmallocUsed:": "362896 kB",
	"MemTotal:": "8092252 kB",
	"SwapTotal:": "16776188 kB",
	"NFS_Unstable:": "0 kB",
	"VmallocTotal:": "34359738367 kB",
	"Active(anon):": "523204 kB",
	"KernelStack:": "3856 kB",
	"SwapFree:": "16776188 kB",
	"AnonHugePages:": "0 kB",
	"VmallocChunk:": "34359343324 kB"
}
```

- Search (is case insensitive):

```
>>> mem.search('Swap')
['SwapCached:            0 kB\n', 'SwapTotal:      16776188 kB\n', 'SwapFree:       16776188 kB\n']
```

## License:

```
	Apache v2.0 License
	Copyright 2014-2015 Martin Simon

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