Korean = ["사랑해", "귀엽다", "고마워", "행복해"]
score = 0
print("Let's Learning Korean")
for x in Korean:
    print(x)
    y = input("입력하세요 >>>")
    if x == y:
        score += 1
    else:
        score += 0

        
           
 
print("전체 문제 개수: 4 개")
print("맞힌 문제 개수:", score, "개")
print("틀린 문제 개수:", 4-score, "개")
    