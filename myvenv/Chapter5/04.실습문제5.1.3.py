have_money = int(input("현재 가진 금액을 입력 >>>"))

if have_money >= 20000:
    print("오늘 저녁은... 치킨!")
elif have_money >= 10000:
    print("오늘 저녁은... 떡볶이!")
elif have_money >= 2000:
    print("오늘 저녁은... 편의점 김밥!")
else:
    print("돈 부족!!!")