origin_password = "1234"
input_password = input("비밀번호를 입력하세요 >>>")



if input_password == origin_password:
 print("올바른 비밀번호 입니다.")
elif input_password == "":
 print("아무것도 입력하지 않았습니다.")
else:
 
 print("틀린 비밀번호 입니다.")