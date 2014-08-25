# Random notes taken during CTF / exploit exercises
This repository contains various useful tips for CTF / exploiting.

## Packing adresses in Python
```python
# Slow, unreadable and boring way :
adress = '\xef\xbe\xad\xde'

# better way
from struct import pack
adress = pack('<I', 0xdeadbeef)
```
