korean = int(input("국어 >>>"))
math = int(input("수학 >>>"))
english = int(input("영어 >>>"))
average = (korean + math + english) / 3


if 0 <= korean <= 100 and 0<= math <= 100 and 0<= english <= 100:
    if average >= 80:
     print("합격")
    else:
        print("불합격")
else:
    print("잘못입력하였습니다.")
   