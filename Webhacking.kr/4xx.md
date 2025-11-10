- MDN 400 문서 보면서 푸는 것을 권장한다.
- 400 Bad Request
	- 파라미터에 특수문자를 삽입해 본다.
	- 웹페이지 소스코드에서 입력 양식 패턴으로 `pattern='KEY\{([0-9]|[a-f]){32}\}'` 설정해 두었다.
	- `GET /?key1=#&key2=&key3=&key4=&key5=&key6=&key7=&key8=&key9= HTTP/1.1`
	- `KEY{10fac9b9f4112a1d9a650fec275bf164}`
- 404 Not Found
	- GET 경로에 없는 경로를 요청해 본다.
	- `GET /adsf?key1=&key2=&key3=&key4=&key5=&key6=&key7=&`
	- /adsf 경로는 없는 경로이다.
	- `KEY{23c0b3a9ccc44b72f17a99eadb351d2f}`
- 405 Method not allowed
	- `DELETE /asdf HTTP/1.1`
	- 허가되지 않은 동작을 수행해 본다.
	- `KEY{e5602408f2037c05bbbb0995fec6bc58}`
- 


400 403 404 405 408 412 414 416 417