#web-hacking
# Payload
```sql
a' and extractvalue(rand(),concat(0x3a, (select substr(concat(0x3a,upw),1,32) from user limit 0,1)));#
a' and extractvalue(rand(),concat(0x3a, (select substr(concat(0x3a,upw),20,32) from user limit 0,1)));#
```

# 검색 키워드
- Error 기반 SQL Injection
- extractvalue() 함수
- substr(), substring() 함수
- LIMIT 함수
- concat() 함수

# 해설
## 배경지식
- 0x3a는 아스키 코드로 : 를 의미한다.
- extractvalue() 함수는 두 가지 인수를 받는다. xml_frag, xpath_expr
  - xml_frag는 xml을 받는다.
  - xpath_expr는 XPath 표현식을 받는다.
  - 두 개의 인수를 받아 XML에서 XPath 표현식에 일치하는 데이터를 추출하여 반환한다.
  - 이 과정에서 xpath_expr에 유효하지 않은 XPath 표현식이 사용되면 다음과 같은 오류가 발생한다.
  ```ERROR 1105 (HY000): XPATH syntax error: 'xpath_expr 인수의 값' ```
  - 그런데 xpath_expr 인수로 임의의 SQL 쿼리를 지정한다면 이 쿼리의 실행 결과가 오류 메시지에 포함된다.
- 이러한 점을 이용해 오류 기반의 SQL Injection을 수행할 수 있다.

## 인젝션 진행
- sql문의 작은 따옴표를 닫아야 하기 때문에 우선 앞에 아무 문자 + ' 를 넣어 준다.
- and 연산자로 이어준다.
- extractvalue 함수를 사용한다.
  - xml_frag에 rand() 함수를 넣어 준다.
  - xpath_expr에 내가 실행할 SQL 쿼리 문을 넣어 준다.
  - 단, 항상 유효하지 않은 XPath 표현식이 되도록 하기 위해 concat() 함수를 이용해 콜론(:, 0x3a)를 추가한다.
    - 그냥 콜론 문자를 넣으면 안 되고 0x3a로 넣어야 한다. 아직 이유는 모르겠다.
- 제공된 파일에서 init.sql에서는 users 테이블을 사용하고, 컬럼명으로 uid와 upw를 사용하고 있다.
- flag를 찾는 데 필요한 컬럼은 upw 컬럼이므로, `select upw from users` 를 작성한다.
- 오류 메시지는 단일 행으로 반환되므로, LIMIT 을 이용해 한 번에 하나의 행만 출력하도록 한다. 다른 행을 출력하려면 `LIMIT n, 1` 에서 n의 숫자를 바꿔 주면 된다.

## 왜 나오다 말아?
- XML 내장함수의 경우 에러가 출력되는 길이가 32글자의 제한이 존재한다.
- 따라서 데이터가 길 때는 잘려 나오므로, substr(), substring()의 함수를 이용해서 여러 번 분할하여 출력을 해 준다.
- 약간씩 겹쳐 나오게 하는 것이 좋다.

# 참조 링크
- [https://www.bugbountyclub.com/pentestgym/view/53](https://www.bugbountyclub.com/pentestgym/view/53)
- [https://johyungen.tistory.com/408](https://johyungen.tistory.com/408)