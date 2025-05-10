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
- 중사 박민철
- 중사(진) 박병준
- 8급 금한울
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
- 중사 박민철
- 중사(진) 박병준
- 8급 금한울
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

- 정상적인 상황이라면 phone 입력 칸에 작성할 수 있는 내용은 10자리 이하 숫자로만 구성된 문자열만 입력이 가능하고, 그 외에는 `query error` 문구를 출력하며 입력값이 저장되지 않는다.
- form에서 전화번호 입력 사이즈는 11이라고 작성되어 있지만, 보통은 010 으로 시작하는 번호를 입력하고, 맨 앞의 0은 사라지기 때문에 10자리로 인식된다.
- 또한, form에서 add 버튼을 누르면 입력한 전화번호 값과 함께, `type="hidden"`으로 작성된 `id=guest` 값도 서버로 전달된다.
- 