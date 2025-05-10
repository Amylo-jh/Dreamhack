# Payload
```text
123),('admin','117.111.28.138',123
```

# 검색 키워드
- SQL Injection
# 해설

![[Pasted image 20250510203752.png]]

# 서론 : Webhacking.kr 문제풀기

## 팀명 :
## 조원

## 조원 역할분담
-
## 팀명 선정이유
-

---
# 본론
## 1. Old-35 문제풀이
- 문제분류 : SQL Injection
- 풀이환경 : Chrome 136.0.7103.93
### 키워드
- SQL Inejction
- `$_SERVER['REMOTE_ADDR']`
- Regex
### 문제 탐색
- 문제 메인 화면은 다음과 같다.
	- 전화번호를 입력할 수 있는 칸이 있고, add 버튼으로 추가할 수 있다.
![[Pasted image 20250511024720.png]]

- view-source 버튼을 누르면 소스 코드를 볼 수 있다. 소스 코드는 다음과 같다.
```php
<?php
  include "../../config.php";
  if($_GET['view_source']) view_source();
?><html>
<head>
<title>Challenge 35</title>
<head>
<body>
<form method=get action=index.php>
phone : <input name=phone size=11 style=width:200px>
<input name=id type=hidden value=guest>
<input type=submit value='add'>
</form>
<?php
$db = dbconnect();
if($_GET['phone'] && $_GET['id']){
  if(preg_match("/\*|\/|=|select|-|#|;/i",$_GET['phone'])) exit("no hack");
  if(strlen($_GET['id']) > 5) exit("no hack");
  if(preg_match("/admin/i",$_GET['id'])) exit("you are not admin");
  mysqli_query($db,"insert into chall35(id,ip,phone) values('{$_GET['id']}','{$_SERVER['REMOTE_ADDR']}',{$_GET['phone']})") or die("query error");
  echo "Done<br>";
}

$isAdmin = mysqli_fetch_array(mysqli_query($db,"select ip from chall35 where id='admin' and ip='{$_SERVER['REMOTE_ADDR']}'"));
if($isAdmin['ip'] == $_SERVER['REMOTE_ADDR']){
  solve(35);
  mysqli_query($db,"delete from chall35");
}

$phone_list = mysqli_query($db,"select * from chall35 where ip='{$_SERVER['REMOTE_ADDR']}'");
echo "<!--\n";
while($r = mysqli_fetch_array($phone_list)){
  echo htmlentities($r['id'])." - ".$r['phone']."\n";
}
echo "-->\n";
?>
<br><a href=?view_source=1>view-source</a>
</body>
</html>
```

- 개발자 도구를 활용하여 원본 웹페이지 소스를 확인하면 다음과 같다.
```html
# Payload
```text
123),('admin','117.111.28.138',123
```

# 검색 키워드
- SQL Injection
# 해설

![[Pasted image 20250510203752.png]]

# 서론 : Webhacking.kr 문제풀기

## 팀명 :
## 조원

## 조원 역할분담
-
## 팀명 선정이유
-

---
# 본론
## 1. Old-35 문제풀이
- 문제분류 : SQL Injection
- 풀이환경 : Chrome 136.0.7103.93
### 키워드
- SQL Inejction
- `$_SERVER['REMOTE_ADDR']`
- Regex
### 문제 탐색
- 문제 메인 화면은 다음과 같다.
	- 전화번호를 입력할 수 있는 칸이 있고, add 버튼으로 추가할 수 있다.
![[Pasted image 20250511024720.png]]

- view-source 버튼을 누르면 소스 코드를 볼 수 있다. 소스 코드는 다음과 같다.
```php
<?php
  include "../../config.php";
  if($_GET['view_source']) view_source();
?><html>
<head>
<title>Challenge 35</title>
<head>
<body>
<form method=get action=index.php>
phone : <input name=phone size=11 style=width:200px>
<input name=id type=hidden value=guest>
<input type=submit value='add'>
</form>
<?php
$db = dbconnect();
if($_GET['phone'] && $_GET['id']){
  if(preg_match("/\*|\/|=|select|-|#|;/i",$_GET['phone'])) exit("no hack");
  if(strlen($_GET['id']) > 5) exit("no hack");
  if(preg_match("/admin/i",$_GET['id'])) exit("you are not admin");
  mysqli_query($db,"insert into chall35(id,ip,phone) values('{$_GET['id']}','{$_SERVER['REMOTE_ADDR']}',{$_GET['phone']})") or die("query error");
  echo "Done<br>";
}

$isAdmin = mysqli_fetch_array(mysqli_query($db,"select ip from chall35 where id='admin' and ip='{$_SERVER['REMOTE_ADDR']}'"));
if($isAdmin['ip'] == $_SERVER['REMOTE_ADDR']){
  solve(35);
  mysqli_query($db,"delete from chall35");
}

$phone_list = mysqli_query($db,"select * from chall35 where ip='{$_SERVER['REMOTE_ADDR']}'");
echo "<!--\n";
while($r = mysqli_fetch_array($phone_list)){
  echo htmlentities($r['id'])." - ".$r['phone']."\n";
}
echo "-->\n";
?>
<br><a href=?view_source=1>view-source</a>
</body>
</html>
```

- 개발자 도구를 활용하여 원본 웹페이지 소스를 확인하면 다음과 같다.
```html
<html>
    <head>
        <title>Challenge 35</title>
    </head>
    <body>
        <form method="get" action="index.php">
            phone : <input name="phone" size="11" style="width:200px">
            <input name="id" type="hidden" value="guest">
            <input type="submit" value="add">
        </form>
        <!--    -->
        <br><a href="?view_source=1">view-source</a>
    </body>
</html>
```

- 웹 화면 동작 및 소스 분석
	- 정상적인 상황이라면 phone 입력 칸에 작성할 수 있는 내용은 10자리 이하 숫자로만 구성된 문자열만 입력이 가능하고, 그 외에는 `query error` 문구를 출력하며 입력값이 저장되지 않는다.
	- form에서 전화번호 입력 사이즈는 11이라고 작성되어 있지만, 보통은 010 으로 시작하는 번호를 입력하고, 맨 앞의 0은 사라지기 때문에 10자리로 인식된다.
	- 또한, form에서 add 버튼을 누르면 입력한 전화번호 값과 함께, `type="hidden"`으로 작성된 `id=guest` 값도 서버로 전달된다.
- 서버 측 php 코드 분석
	- GET 메소드로 전달된 파라미터 중 phone과 id 값이 모두 전달되었을 때 내부 로직이 실행된다.
	- phone 파라미터에 다음과 같은 필터링을 수행한다.
		- 대소문자 구분 없이(`/i` 옵션 사용) 검사
		- `*`, `/`, `=`, `select`, `-`, `#`, `;` 문자가 포함되어 있는지 정규식을 활용하여 검사한다.
			- php에서 정규식 패턴 표현은 `/ ... /` 와 같이 슬래시로 감싼다.
			- `*`, `/` 기호는 정규식에서 메타문자이기 때문에, 문자 앞에 역슬래시로 이스케이프 처리한다.
		- 만약 조건에 맞으면, `no hack` 문구를 출력하고 이후 로직을 수행하지 않는다.
	- id 파라미터에 다음과 같은 필터링을 수행한다.
		- id 파라미터 값이 5자를 초과하면 차단한다.
		- 대소문자 구분 없이(`/i` 옵션 사용) `admin` 문구를 포함하면 차단한다.
	- chall35 테이블에 레코드를 삽입한다.
		- id값, 클라이언트 IP, 입력한 전화번호 값을 삽입한다.
		- 만약 오류 발생시, `query error` 값을 출력한다.
		- 삽입 성공시, `Done` 문구를 출력한다.
	- `$isAdmin` 변수에 `admin` 계정이 현재 클라이언트 IP로 등록되어 있는지 조회 및 결과 저장
	- 조회된 ip가 현재 웹에 접속한 ip와 일치하면 클리어 함수`solve(35)` 호출 및 DB 초기화
	- 조회 결과를 HTML 주석 형태로 감싸 출력한다.
		- id 값 + "-" + 전화번호 형태로 출력한다.
### 공격 지점 탐색
- 가장 쉽게 생각해 볼 수 있는 form의 hidden값인 guest를 admin으로 바꿔 제출하는 것은 차단된다.
	- 서버 측 php 코드에서 id값이 admin으로 전달되었다면 `you are not admin`문구 출력과 함께 더이상 진행되지 않는다.
	- 따라서 guest 값은 그대로 둔다.
- 서버 측 php 코드에서, mysql에 insert 구문 실행시, 사용자가 입력한 값을 prepared