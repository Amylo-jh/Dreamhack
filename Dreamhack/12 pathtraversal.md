#web-hacking 
# Payload
```text
burpsuite를 사용해도 되고, 네트워크 요청을 수정해도 된다.
userid 칸에 입력한 것을 javascript를 사용하여 키-값 검색을 통해 guest, admin이 아니면 undefined로 가기 때문에 그냥 ../../../api/flag 를 입력하면 플래그가 나오지 않는다.
```

https://www.hahwul.com/cullinan/attack/xss/