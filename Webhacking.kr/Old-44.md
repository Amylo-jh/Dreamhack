## 2. Old-44 문제풀이
- 문제분류 : Command Injection
- 풀이환경 : Chrome 136.0.7103.93
### 키워드
- Command Injection (명령어 삽입)
- Linux Command Chaining
- 불충분한 입력 검증
### 문제 탐색
- 문제 메인 화면은 다음과 같다.
	- 이름을 입력할 수 있는 칸이 있고, submit 버튼으로 제출할 수 있다.
![[Pasted image 20250512192558.png]]
- view-source 버튼을 누르면 소스 코드를 볼 수 있다. 소스 코드는 다음과 같다.
```php
<?php
if ($_GET["view_source"]) {
    highlight_file(__FILE__);
    exit();
} ?>

<html>
<head>
  <title>Challenge 44</title>
</head>

<body>
  <?php if ($_POST["id"]) {
      $id = $_POST["id"];
      $id = substr($id, 0, 5);
      system("echo 'hello! {$id}'"); // You just need to execute ls
  } ?>
  <center>
    <form method=post action=index.php name=htmlfrm>
      name : <input name=id type=text maxlength=5><input type=submit value='submit'>
    </form>
    <a href=./?view_source=1>view-source </a>
    </center>
</body>
</html>
```

- 개발자 도구를 활용하여 원본 웹페이지 소스를 확인하면 다음과 같다.
```html
<html>
<head>
	<title>Challenge 44</title>
</head>
<body>
	<center>
		<form method="post" action="index.php" name="htmlfrm">
			name : 
			<input name="id" type="text" maxlength="5">
			<input type="submit" value="submit">
		</form>
		<a href="./?view_source=1">view-source</a>
	</center>
</body>
</html>
```

- 웹 화면 동작 및 소스 분석
	- 정상적인 상황이라면 id 입력 칸에 작성할 수 있는 내용은 5자리 이하 문자열만 입력 가능하다.
	- 5자를 초과하는 문자열을 입력 후 submit 버튼을 누르더라도, 5자 까지만 전송되며 화면 좌측 상단에 `hello! (입력한 문자 중 최대 5자)` 가 표기된다.
- 서버 측 php 코드 분석
	- POST 메소드로 전달된 파라미터 중 id 값이 전달되었을 때 내부 로직이 실행된다.
	- `$id` 변수에 id 입력값을 저장한다.
	- `$id` 변수 값을 substr 함수를 이용하여 처음 5글자만 남기고 나머지를 잘라낸다.
	- `system()` 함수를 사용해 `echo 'hello! (입력값)` 명령어를 실행한다.
		- 입력값은 앞서 5글자로 제한된 `$id`가 들어간다.
		- 주석에서는 ls 명령어를 실행해야 한다고 힌트를 주고 있다.
### 공격 지점 탐색
- HTML의 form에서 `maxlength` 속성으로 입력 길이를 제한한 것은 클라이언트 측의 단순 제어일 뿐이며, 공격자는 원한다면 브라우저 개발자 도구, 커스텀 HTTP 요청 도구(curl, Burp Suite, etc) 등을 이용하여 `maxlength` 속성을 무시하고 원하는 길이의 데이터를 서버로 전송할 수 있다.
	- 하지만 이는 서버 측 PHP 코드의 `substr($id, 0, 5)` 를 이용하여 길이 검증을 수행하고 있어 큰 의미가 없다.
	- 따라서 공격은 5자리 이내 입력값 이내에서 수행되어야 한다.
- 5글자 길이 제한이 있지만, 별도의 검증 없이 `system()` 함수를 이용하여 사용자의 입력값이 쉘 명령어의 일부로 직접 사용되고 있다.
- 길이만 제한하고, 입력 검증이 전혀 없으므로 쉘 메타문자(`&`, `;`, `|`)를 삽입하여 명령어 체이닝이 가능하다.
### 페이로드
- name 양식에 다음을 입력
```bash
'&ls'
```
- 이후 나온 플래그 경로로 접속
```text
http://webhacking.kr:10005/flag_29cbb98dafb4e471117fec409148e9386753569e
```
### 원리
- 사용자가 입력한 값을 쉘 명령어의 일부로 직접 사용하는 점을 이용하였다.
- 원래 의도된 동작은 다음과 같다.
```php
system("echo 'hello! {$id}'");
```
- 하지만 입력값을 검증하지 않고 바로 쉘 명령어에 사용한 것을 이용하여 임의 명령어 삽입을 할 수 있다.
- 따라서 페이로드와 같이 입력 양식에 입력하게 되면 실행하는 쉘 명령어가 다음과 같이 변경된다.
```bash
echo 'hello! '&ls''"
```
- 위 명령어가 실행되면, 시스템은 `echo 'hello! ` 명령어를 수행, 출력한 후, `&` 로 인해 `ls` 명령어가 실행된다.
- `ls`는 현재 디렉토리 목록을 출력하게 되므로, 공격자는 이를 통해 해당 경로에 존재하는 `flag_29cbb98dafb4e471117fec409148e9386753569e` 파일의 존재를 알 수 있다.
### 결과
![[Pasted image 20250512194944.png]]

![[Pasted image 20250512195605.png]]