#system-hacking 
# Payload
- 내가 처음 작성한 코드
```python
from pwn import *

context.log_level = 'debug'

r = remote("host8.dreamhack.games", 12503)
# r = process(["python3", "prob.py"])

r.recvuntil(b"There are 50 rounds.\n\n", drop=True)
for i in range(0, 50):
    idx = 0
    for j in range(10):
        line = r.recvline()
        if b"flag" in line:
            idx = j
    r.recvuntil(b"Which item do you want to buy?\n> ", drop=True)
    r.sendline(str(idx).encode())
    r.recvline()

r.interactive()
```
- 드림핵 정답 코드
```python
import sys
from pwn import *

context.log_level = 'debug'

if len(sys.argv) != 3:
    print("how to use: python3 prob_exploit.py [HOST] [PORT]")
    exit()
r = remote(sys.argv[1], int(sys.argv[2]))

r.recvuntil(b"There are 50 rounds.\n\n", drop=True)
for i in range(0, 50):
    idx = 0
    for j in range(10):
        line = r.recvline()
        if b"flag" in line:
            idx = j
    r.recvuntil(b"Which item do you want to buy?\n> ", drop=True)
    r.sendline(str(idx).encode())
    r.recvline()

r.interactive()
```
# 검색 키워드
- pwntools 기본 사용법
- 인자 사용법
# 해설
## 소스코드 분석
- 10가지 메뉴 중에서 flag가 포함된 메뉴 번호를 50번 맞게 출력해야 한다.
- 메뉴가 한번 할때마다 섞이기 때문에, 자동으로 해야 한다.
- 50번을 10초 안에 모두 맞춰야 한다.
- 자동으로 메뉴 중에서 flag가 포함된 메뉴번호를 골라내야 한다.
# 익스플로잇 과정
- 위 과정을 맞게 하면 50번 입력이 끝나고 플래그를 출력한다.![[Pasted image 20251006124357.png]]