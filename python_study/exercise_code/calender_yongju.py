#### 2019 calender maker


month = eval(input('월을 입력하세요(1~12):'))
print("\n\n")
print("%35d 월\n\n" % month)
m_num = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum = 0
count = 0
month -= 1
for i in m_num:
    if (count >= month): break;
    sum += i
    count = count + 1

st = (2 + sum) % 7

li = ["일", "월", "화", "수", "목", "금", "토"]

for i in li:
    print('%8s' % i, end=" ")
print("\n")

days = range(0, m_num[month])
week = [0, 1, 2, 3, 4, 5, 6]
a = 0

while a < st:
    a += 1
    print("         ", end=" ")

for i in days:
    if (i >= 1) & ((i + st) % 7 == 0): print("\n")
    print('%9d' % (i + 1), end=' ')

