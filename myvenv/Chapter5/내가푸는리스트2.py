count = []
a = int(input("1일차 턱걸이 횟수 >>>"))
count.append(a)
a = int(input("2일차 턱걸이 횟수 >>>"))
count.append(a)
a = int(input("3일차 턱걸이 횟수 >>>"))
count.append(a)
a = int(input("4일차 턱걸이 횟수 >>>"))
count.append(a)
a = int(input("5일차 턱걸이 횟수 >>>"))
count.append(a)
a = int(input("6일차 턱걸이 횟수 >>>"))
count.append(a)
a = int(input("7일차 턱걸이 횟수 >>>"))
count.append(a)

total = count[0] + count[1] + count[2] + count[3] + count[4] + count[5] + count[6]
avg = total / 7
print(int(avg))