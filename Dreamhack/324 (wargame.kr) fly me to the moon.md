#web-hacking

# Payload
```javascript
var keywords = [
    "killPlayer", 
    "checkLife", 
    "getScore", 
    "BincScore", 
    "shrinkTunnel", 
    "widthTunnel", 
    "object", 
    "Do cheating, if you can", 
    "warn", 
    "offsetLeft", 
    "tunnel", 
    "getElementById", 
    "top", 
    "", 
    "px", 
    "css", 
    "display", 
    "block", 
    "each", 
    "img.left_wall", 
    "img.right_wall", 
    "#high_scores", 
    "remove", 
    "table", 
    "none", 
    "div#score_table", 
    "click", 
    "text", 
    "span#score", 
    "left", 
    "img#ship", 
    "slow", 
    "fadeIn", 
    "background-position", 
    "50% ", 
    "div#tunnel", 
    "random", 
    "floor", 
    "updateTunnel()", 
    "fadeOut", 
    "POST", 
    "high-scores.php", 
    "token=", 
    "&score=", 
    "ajax", 
    "html", 
    "p#welcome", 
    "updateToken()", 
    "thx, Christian Montoya", 
    "mouseover", 
    "#christian", 
    "mouseout", 
    "ready", 
    "pageX", 
    "mousemove", 
    "temp", 
    "get", 
    "token.php"
];

function secureGame() {
    var _this = this;
    var isAlive = true;

    function killPlayer() {
        isAlive = false;
        return true;
    }

    function checkLife() {
        return isAlive;
    }

    this.killPlayer = function() {
        killPlayer();
        return true;
    };

    this.checkLife = function() {
        return checkLife();
    };

    var score = 31337;

    function getScore() {
        return score;
    }

    function incrementScore() {
        if (isAlive) {
            score++;
        }
        return true;
    }

    this.getScore = function() {
        return getScore();
    };

    this.BincScore = function() {
        incrementScore();
        return true;
    };

    var tunnelWidth = 320;

    function shrinkTunnel() {
        tunnelWidth -= 20;
        return true;
    }

    function getTunnelWidth() {
        return tunnelWidth;
    }

    this.shrinkTunnel = function() {
        shrinkTunnel();
        return true;
    };

    this.widthTunnel = function() {
        return getTunnelWidth();
    };
}
```
중간에 `var score = 31337;` 가 핵심이다.
# 검색 키워드
- Javascript Beautifier
- ChatGPT
- Burp Suite
- Chrome Developer Tool
# 해설
- 우선 이 문제는 여러 가지 방법으로 풀 수 있음을 알린다.
	- 난독화 해제 후 score값이 변조된 코드로 덮어씌우기
	- Burp Suite를 이용하여 패킷 값 변조
	- 일부 함수를 변조, 덮어씌워 스코어 값이 31337보다 높아지도록 변조
## 코드 분석
- 솔직히 난독화된 자바스크립트 코드를 생짜로 분석하는건 미친 짓인것 같다.
- 두 개의 서비스를 이용해 볼 수 있다.
	- [https://beautifier.io/](https://beautifier.io/)
	- [https://chatgpt.com/](https://chatgpt.com/)
- 우선 코드는 문제 웹페이지에서 개발자 도구를 열면 콘솔에 찍히는 메시지를 보고 코드를 확인할 수 있다.![[Pasted image 20240717202812.png]]![[Pasted image 20240717202825.png]]
- 딱봐도 변수명과 함수명이 난독화되어 있다. 이걸 전부 다 복사해 온다.
- beautifier.io에 복사해온 코드를 붙여 넣고, 아래와 같이 난독화, 패커를 해제하는 옵션을 선택해 준다.![[Pasted image 20240717203023.png]]
- 이제 그나마 좀 읽어볼 마음이 들게 변했을 것이다.
- 여기에서 200번째 줄보다 밑에 쪽을 살펴 보면 ajax로 POST를 보내는 것을 찾을 수 있다.
- 이 함수에서 토큰과 스코어를 POST로 보내는 것을 보아 Burp Suite로 점수를 변조해 볼 수 있겠다.

- 또 다른 방법으로는 ChatGPT를 사용하는 것이다.
- 원본 코드를 들고, 코드 해석을 해 달라고 한다. 난독화가 되어 있다면 해독해서 함수별로 무슨 역할을 하는지 알려 달라고 해 보자.
- 그러면 어떻게 했는지는 몰라도 난독화된 코드의 변수명까지 전부 다 복구해서 코드를 준다.
- 여기에서 score 변수가 있는데, 이걸 31337로 바꾼 후 모두 복사하여 크롬 개발자 도구 콘솔에 붙여넣은 뒤, 게임을 실행하고 죽으면 플래그를 얻을 수 있다.
![[Pasted image 20240717194634.png]]

- 솔직히 아직도 난독화 되어 있는 코드는 접근하기가 어려운 것 같다.