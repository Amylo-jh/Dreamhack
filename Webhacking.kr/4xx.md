- MDN 400 문서 보면서 푸는 것을 권장한다.
## 400 Bad Request
- 파라미터에 특수문자를 삽입해 본다.
- 웹페이지 소스코드에서 입력 양식 패턴으로 `pattern='KEY\{([0-9]|[a-f]){32}\}'` 설정해 두었다.
- `GET /?key1=#&key2=&key3=&key4=&key5=&key6=&key7=&key8=&key9= HTTP/1.1`
- HTTP 버전을 이상한 문자열로 고쳐서 보내도 400 에러를 내도록 할 수 있다.
- 호스트 헤더를 조작해도 400 에러가 나도록 할 수 있다.
- `KEY{10fac9b9f4112a1d9a650fec275bf164}`
## 403 Forbidden
- 소스코드에 있는 경로 나와 있는것들을 유심히 본다.
- 파일 디렉터리 리스팅과 연관이 있다.
- /img/flag.png는 이미 있는 겨올이지만, /img 경로 자체에 접근해 보면 허가되지 않아 403 오류가 나게 된다.
```HTTP Request
GET /img/ HTTP/1.1
Host: webhacking.kr:10022
Cache-Control: max-age=0
Accept-Language: ko-KR,ko;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: keep-alive


```
- `KEY{cd79de80772c1873bcf63e41e3379c6f}`
## 404 Not Found
- GET 경로에 없는 경로를 요청해 본다.
- `GET /adsf?key1=&key2=&key3=&key4=&key5=&key6=&key7=&`
- /adsf 경로는 없는 경로이다.
- `KEY{23c0b3a9ccc44b72f17a99eadb351d2f}`
## 405 Method not allowed
- `DELETE /asdf HTTP/1.1`
- 허가되지 않은 동작을 수행해 본다.
	- TRACE 같은 여러 HTTP 메서드들에 대해 찾아봐도 된다.
- `KEY{e5602408f2037c05bbbb0995fec6bc58}`
## 408 Request Timeout
- POST로 보낼것처럼 하고 내용물을 타임아웃 날 때까지 보내지 않기
```HTTP Request
POST /?key1=&key2=&key3=&key4=&key5=&key6=&key7=&key8=&key9= HTTP/1.1
Host: webhacking.kr:10022
Accept-Language: ko-KR,ko;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Content-Length: 0

```
- `KEY{e44fa3e1865a3839cbc0b658f1ae08cf}`
## 416 Range Not Satisfiable
- 특정 내용의 범위를 지정해서 보내달라고 요청을 했는데, 그 내용이 서버에 저장된 컨텐츠 내용 범위 바깥일 경우
- Range 구문을 사용할 수 있다.
```HTTP Request
GET /?key10=&key2=&key3=&key4=&key5=&key6=&key7=&key8=&key9= HTTP/1.1
Host: webhacking.kr:10022
Cache-Control: max-age=0
Accept-Language: ko-KR,ko;q=0.9
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Range: bytes=1000-1999


```
- `KEY{e44fa3e1865a3839cbc0b658f1ae08cf}`
## 417 Expectations unsupported
- 


412 414 417