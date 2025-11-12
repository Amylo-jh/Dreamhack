#system-hacking 
# Payload
- 내가 처음 작성한 코드
```python
from pwn import *

context.log_level = 'debug'
r = remote("host8.dreamhack.games", 23745)
# r = process("./chall")

for i in range(0, 50):
    a = r.recvuntil(b'+')
    b = r.recvuntil(b'=')
    r.recvline()
    a = int(a[:-1])
    b = int(b[:-1])
    c = bytes(str(a+b), 'utf-8')
    
    r.sendline(c)

print(r.recvall())
```
- 개선된 코드
```python
from pwn import *

context.log_level = 'debug'
r = remote("host8.dreamhack.games", 23745)
# r = process("./chall")

for i in range(0, 50):
    a = int(r.recvuntil(b'+', drop=True))
    b = int(r.recvuntil(b'=?\n', drop=True))
    r.sendline(str(a+b).encode())

r.interactive()
```
# 검색 키워드
- pwntools 기본 사용법
- 자료형 변환
# 해설
## 소스코드 분석
- `alarm(1)`을 실행하면 1초 후 `SIGALARM` 시그널을 전달한다. `initialize()` 내부의 `signal()`로 `SIGALARM` 시그널이 전달될 경우에 실행할 함수를 설정한다. 이렇게 설정된 함수 `alarm_handler()`는 "TIME OUT"을 출력하고, 프로세스를 종료한다.
	- 1초안에 숫자 덧셈 결과를 입력하지 않으면 프로그램이 종료된다.
	- 50개의 숫자 덧셈을 각각 1초 안에 해야 플래그를 얻을 수 있다.
## 익스플로잇 과정
- 두 숫자의 합을 물어 보는 문자열을 잘 파싱해서 더한 후, 결과를 잘 보내면 된다.
- 50번 반복 후, 출력되는 NICE! 와 플래그 값을 터미널에 띄워 주면 된다.![[Pasted image 20251006111100.png]]