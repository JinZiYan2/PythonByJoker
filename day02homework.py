# 1.解一元二次方程
# import math
# a = float(input("请输入a的值："))
# b = float(input("请输入b的值："))
# c = float(input("请输入c的值："))
# p = float(b*b - 4 * a * c)
# d = (-b + math.sqrt(p)) / (2 * a)
# e = (-b - math.sqrt(p)) / (2 * a)
# if p > 0:
#     print('x1 = (-%f + math.sqrt(%f)/(2*%f) = %f'%(b,p,a,d))
#     print('x2 = (-%f - math.sqrt(%f)/(2*%f) = %f'%(b,p,a,e))
# elif p == 0:
#     print('x1 = x2 = (-%f + math.sqrt(%f))/(2*%f) = %f'%(b,p,a,d))
# else:
#     print('该方程没有实根')

# 2.学习加法
# import random
# num1 = random.randint(0,100)
# num2 = random.randint(0,100)
# print('num1 = %d'%num1)
# print('num2 = %d'%num2)
# sum = input('num1 + num2 =')
# if sum == '%d'%(num1+num2):
#     print('True')
# else :
#     print('false')

# 3.找未来数据
# today = int(input('Enter today*s day(星期天是0，星期一是1，...星期六是6):'))
# days = int(input('Enter the number of days elapsed since today:'))
# future = (days + today) % 7
# if today == 0 :
#     week = 'sunday'
# elif today == 1:
#     week = 'Monday'
# elif today == 2:
#     week = 'Tuesday'
# elif today == 3:
#     week = 'Wednesday'
# elif today == 4:
#     week = 'Thursday'
# elif today == 5:
#     week = 'Friday'
# elif today == 6:
#     week = 'Saturday'
# else:
#     print('error')
# if future == 0:
#     futureweek = 'sunday'
# if future == 1:
#     futureweek = 'Monday'
# if future == 2:
#     futureweek = 'Tuesday'
# if future == 3:
#     futureweek = 'Wednesday'
# if future == 4:
#     futureweek = 'Thursday'
# if future == 5:
#     futureweek = 'Friday'
# if future == 6:
#     futureweek = 'Saturday'
# print('Today is %s and the future day is %s'%(week,futureweek))

# # 4.对三个整数排序
# num1 = int(input('请输入第一个数：'))
# num2 = int(input('请输入第二个数：'))
# num3 = int(input('请输入第三个数：'))
# # numlist = [num1,num2,num3]
# if num1 > num2 > num3:
#     print('numlist = %d,%d,%d'%(num1,num2,num3))
# if num1 > num3 > num2:
#     print('numlist = %d,%d,%d'%(num1,num3,num2))
# if num2 > num1 > num3:
#     print('numlist = %d,%d,%d'%(num2,num1,num3))
# if num2 > num3 > num2:
#     print('numlist = %d,%d,%d'%(num2,num3,num2))
# if num3 > num1 > num2:
#     print('numlist = %d,%d,%d'%(num3,num1,num2))
# if num3 > num2 > num1:
#     print('numlist = %d,%d,%d'%(num3,num2,num1))

# 5.比较价钱
# A = float(input('请输入包装1的重量：'))
# B = float(input('请输入包装2的重量：'))
# C = float(input('请输入包装1的价格：'))
# D = float(input('请输入包装2的价格：'))
# if C / A > D / B:
#     print('包装2价钱更好')
# elif C / A > D / B:
#     print('包装1价钱更好')

# 6.找出一个月中的天数
# month = int(input('请输入月份：'))
# year = int(input('请输入年份'))
# month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) and month ==2:
#     print('29天')
# elif month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
#     print('31天')
# elif month == 2:
#     print('28天')
# else:
#     print('30天')


# 7.头或尾
# import numpy as np 
# computer = np.random.choice(['正面' , '反面'])
# user = input('请输入您的选择(正面或反面):') 
# if user == computer:
#     print('恭喜您！猜对了！')
# if user != computer:
#     print('抱歉，猜错了。')

# 8.石头剪刀布
# import numpy as np
# computer = np.random.choice(['石头','剪刀','布'])
# user = input('请输入[石头，剪刀，布]:')
# if computer == user :
#     print('平局');
# elif computer == '石头' and user == '剪刀':
#     print('你输了');
# elif computer == '剪刀' and user == '布' :
#     print('你输了');
# elif computer == '布' and user == '石头' :
#     print('你输了');
# else :
#     print('你赢了');


# 9.一周的星期几
# year = input('请输入年份：')
# m = input('请输入月份：')
# q = input('请输入一天:')
# k = year
# j = 'year' / 100
# h = { '%s' + [(26*('%s' + 1))/10] + '%s' + ['%s' / 4] + ['%s' / 4] + 5 * '%s'%(q,m,k,k,j,j)} % 7
# if h == 0 :
#     print('星期六')
# elif h == 1:
#     print('星期天')
# elif h == 2:
#     print('星期一')
# elif h == 3:
#     print('星期二')
# elif h == 4:
#     print('星期三')
# elif h == 5:
#     print('星期四')
# elif h == 6:
#     print('星期五')
# else:
#     print('error')

# 10.选出一张牌
# import random
# class Cards:
# def init(self,name,allcards):
# self.name = name
# self.allcards = allcards
# def shuffle_card(self):
#     print(list(set(self.allcards)))

# def take_card(self):
#   z1 = self.allcards
#   random.shuffle(z1)
#   print(f'{self.name}您随机抽取的牌为：{z1[0]}')

# def draw(self):
#     num = int(input('请输入指定的牌顺序：').strip())
#     print(f'{self.name}您抽取的第{num}张牌为：{self.allcards[num - 1]}')

# def sorting(self):
#     print(self.allcards)

# def end(self):
#     exit()
# print('1.洗牌\n2.随机抽取一张\n3.指定抽取一张\n4.从小到大排序\n5.退出\n')
# n = input('请输入用户名：').strip()
# while 1:
# allcards = []
# lis1 = ['红心', '草花', '黑桃', '方片']
# for i in lis1:
# for k in range(1, 14):
# if k == 1:
# allcards.append((i, 'A'))
# elif k == 11:
# allcards.append((i, 'J'))
# elif k == 12:
# allcards.append((i, 'Q'))
# elif k == 13:
# allcards.append((i, 'K'))
# else:
# allcards.append((i, k))
# num = int(input('请输入序号选择：').strip())
# s1 = Cards(n,allcards)
# dic = {1: s1.shuffle_card,2: s1.take_card,3: s1.draw,4: s1.sorting,5: s1.end}
# dicnum


# 11.回文数
# a = input('请输入一个三位数:')
# a1 = a[::-1]
# if a1 == a:
#     print('这是一个回文数')
# else :
#     print('这不是一个回文数')

# 12.计算三角形的周长
# l1 = float(input('请输入三角形的第一条边长：'))
# l2 = float(input('请输入三角形的第二条边长：'))
# l3 = float(input('请输入三角形的第三条边长：'))
# if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
#     print('%.2f + %.2f + %.2f = %.2f'%(l1,l2,l3,l1+l2+l3))
# else :
#     print('这个输入是非法的')

#1.统计正数和负数的个数然后计算这些数的平均值
# count1 = 0
# count2 = 0
# sum = 0
# num = int(input('请输入整数'))
# while num != 0:
#     if num > 0:
#         count1 +=1
#     else:
#         if num != 0 :
#             count2 +=1
#     sum =sum +num 
#     num = int(input('请输入一个整数：'))
# count = count1 +count2
# if count !=0:
#     avg = sum/count
#     print('负数个数为%d,正数个数为%d,和为%d,平均值为%.2f' %(count2,count1,sum,avg))


#2.计算未来学费
# n = 10000
# sum =0
# for i in range(1,14):
#     n = n * 0.05 + n
#     if i == 10:
#         print('十年后的学费是：%d'%n)
#     if i>9:
#         sum += n 
# print('十年后大学四年的学费是：%d' %sum)

#4.找出可被5和6同时整除的数
# a = 0
# for i in range(100,1001):
#     if i % 5 == 0 and i % 6 == 0 :
#         a +=1
#         print(i,end='\t')
#         if a % 10 ==0:
#             print('\n',end='')

#5
# n = 0
# m = 0
# while n*n <= 12000:
#     n += 1
# print('n的平方大于12000的最小整数n为：%d'%n)
# while m * m * m < 12000:
#     m += 1
# print('n的立方大于12000的最大整数n为：%d'%(m-1))

#7.演示消除错误
# a = 0
# b = 0
# for i in range(1,50001):
#     a +=1/i
# for i in range(50000,0,-1):
#     b +=1/i
# print('从左到右计算数列和为：',a)
# print('从左到右计算数列和为：',b)


#8.数列求和
# i = 3
# sum = 0
# while i <99:
#     sum += (i-2)/i
#     i +=2
# print('和为：',sum)

#9.计算π
# pi = 0
# for i in range(1,100001):
#     pi +=4*((-1)**(1+i)/(2*i-1))
#     if i % 10000 ==0:
#         print('当i的值为%d时值为：' %i,pi)

# 10.完全数
# for i in range(1,1000):
#     s = 0
#     for k in range(1.i):
#         if i % k == 0:
#             s = s + K
#     if i == s:
#         print('i')

# 11.组合
# import math
# n = 0
# a = 0
# b = []
# c = 0
# for i in range(10):
# shu = float(input('请输入10个数字：'))
# b.extend([shu])
# a += shu
# n += 1
# mean = a / n
# print('均值：%d'%mean)
# for j in b:
# c += (mean - j) **2 / n
# deviation = math.sqrt(c / n)
# print('标准差：%d'%deviation)