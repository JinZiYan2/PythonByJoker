# 1.五角数
# n = 1
# def getPentagonalNumber(n):
#     for n in range(1,101):
#         star = n*(3*n-1)/2
#         print('%d'%star,end='\t')
#         if n % 10 == 0:
#             print('')
# getPentagonalNumber(n)

# 2.求一个整数各个数字的和
# def sumDigits(n):
#     n = str(input('请输入一个整数：>>'))
#     sum = 0
#     for i in range(len(n)):
#         sum = int(n[i]) + sum
#     print('%s中各个数字的和为：%s'%(n,sum))
# sumDigits('n')

# 3.对三个数排序
# def displaySortedNumbers(num1,num2,num3):
#     num1 = int(input('请输入第一个整数：>>'))
#     num2 = int(input('请输入第二个整数: >>'))
#     num3 = int(input('请输入第三个整数：>>'))
#     numlist = [num1,num2,num3]
#     if num1 > num2 > num3:
#         print('numlist = %d,%d,%d'%(num1,num2,num3))
#     if num1 > num3 > num2:
#         print('numlist = %d,%d,%d'%(num1,num3,num2))
#     if num2 > num1 > num3:
#         print('numlist = %d,%d,%d'%(num2,num1,num3))
#     if num2 > num3 > num2:
#         print('numlist = %d,%d,%d'%(num2,num3,num2))
#     if num3 > num1 > num2:
#         print('numlist = %d,%d,%d'%(num3,num1,num2))
#     if num3 > num2 > num1:
#         print('numlist = %d,%d,%d'%(num3,num2,num1))
# displaySortedNumbers('num1','num2','num3')

# 4.计算未来投资值  (结果)
# def futureInvestmentValue(investmentAmount,monthlyInterestRate,years):
#     investmentAmount = float(input('请输入投资额： >>'))
#     monthlyInterestRate = float(input('请输入百分比格式的月利率： >>'))
#     # year = input('请输入年数')
#     for i in range(1,31):
#         years = (i * 12) 
#         futureInvestmentValue = '%f * (1 + %f) ** %f '%(investmentAmount,monthlyInterestRate,years)
#         print(i,futureInvestmentValue)
# futureInvestmentValue('investmentAmount','monthlyInterestRate','years')

# 5.显示字符
# def printChars(ch1,ch2,numberPerLine):
#     ch1 = input('请输入L~Z之间的字符：')
#     ch2 = input('请输入L~Z之间的字符：')
#     numberPerLine = ['L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#     for i in range(ch1,ch2):
#         j = chr(i)
#         print(j,end = ' ')
#         if j % 10 == 0:
#            print()
# printChars('ch1','ch2','numberPerLine')

# 6.一年的天数
# def numberOfDaysInAYear(year):
#     # year = int(input('请输入您想查询的年份：'))
#     for year in range(2010,2021):
#         if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
#             print('366天')
#         else:
#             print('355天')
# numberOfDaysInAYear('year')

# 7.显示角
# import math
# def distance(x1,y1,x2,y2):
#     x1 = float(input('x1 = '))
#     y1 = float(input('y1 = '))
#     x2 = float(input('x2 = '))
#     y2 = float(input('y2 = '))
#     distance = float(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))
#     print(distance)
# distance('x1','y1','x2','y2')

# 8.梅森素数  
# print(1)
# print(2)
# for i in range(3，11):
#     for j in range(2,i):
#             if i % j == 0:
#                 break    
#     else ：
#     print(i)             
# for i in range(1,32):
        
# 9.当前时间和日期
# def time_():
#     import time
#     t = time.localtime(time.time())
#     format_time='%a  %Y-%m-%d  %H:%M:%S'
#     cur_time = time.strftime(format_time,t)
#     print (cur_time)
# time_()

# 10.掷骰子
import random
a = random.randint(1,6)
b = random.randint(1,6)
sum = a + b
if sum == 2 or sum == 3 or sum == 12:
    print('you rolled %d + %d = %d'%(a,b,sum))
    print('你输了')
elif sum == 7 or sum == 11:
    print('you rolled %d + %d = %d'%(a,b,sum))
    print('你赢了')
else:
    print('you rolled %d + %d = %d'%(a,b,sum))
    print('point is %d'%sum)
    for i in range():
        c = random.randint(1,6)
        d = random.randint(1,6)
        sum2 = c + d
        if sum2 == 7 or sum2 == sum:
            print('you rolled %d + %d = %d'%(c,d,sum2))
        if sum2 == 7:
            print('you win')
        else:
            print('you lose')