

10 % 3

number = 123456
split_number = number % 10
print(split_number)


# 각 자리수 분리해서 더한뒤에 출력하시오

def sum_digit(num):
    result = 0
    for i in str(num):
        result = result + int(i)
    return result


sum_digit(123456)

print("결과 : {}".format(sum_digit(123456)));

def num_sum(num):
    sum = 0
    for i in range(1,num+1):
        sum=sum+i
    return sum

num_sum(10)

for m in range(1,10):
    for k in range(1,10):
        print(m,'*',k,'=',m*k)

year = 2028
if((year%4==0 and year%100 !=0) or year%400 == 0):
    print(year,"년은 윤년입니다.")
else:
        print(year, "년은 윤년이 아닙니다.")

import datetime


def getMonthName(month):
    li = ['January', 'February', 'March', 'April', 'May', 'June',

          'July', 'August', 'Setember', 'October', 'November', 'December']

    monthName = li[month - 1]

    return monthName


def title(year, month):
    print('    ', getMonthName(month), ' ', year)

    print('-' * 50)

    print('일  월  화  수  목  금  토')


def getStartDay(year, month):
    d = datetime.date(year, month, 1)

    return d.weekday()  # 월요일 0


def getLastDay(year, month):
    if month == 12:

        year = year + 1

        month = 1

    else:

        month = month + 1

    d = datetime.date(year, month, 1)

    t = datetime.timedelta(days=1)

    k = d - t

    return k.day


def body(year, month):
    startday = getStartDay(year, month)

    lastday = getLastDay(year, month)

    if startday == 6:

        s = 1

    else:

        s = startday + 2

    c = 0

    m = 0

    for k in range(6):

        for i in range(7):

            c = c + 1

            if c < s:

                print('{:>2}'.format(' '), end='  ')

            else:

                if lastday > m:
                    m = m + 1

                    print('{:>2}'.format(m), end='  ')

        print()


def Dal(year, month):
    title(year, month)

    body(year, month)


def main():
    year = eval(input('연도를 입력하세요(ex. YYYY):'))

    month = eval(input('월을 입력하세요(1~12):'))

    Dal(year, month)


main()

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





