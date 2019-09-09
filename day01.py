# 1.
# C = float(input("请输入摄氏温度：>>"))
# F = (9 / 5) * C + 32
# print("摄氏温度为：%.1f"%F)
# 2.
# import math
# radius = float(input("请输入圆柱的半径:>>"))
# length = float(input("请输入圆柱的高:>>"))
# area = radius * radius * math.pi
# print("该圆柱的底面积为:%.4f"%area)
# volume = area * length
# print("该圆柱的体积为：%.4f"%volume)
# 3.
# feet = float(input("请输入一个英尺数：>>"))
# metres = 0.305 * feet
# print("%f英尺等于%f米" %(feet,metres))
# 4.
# M = float(input("Enter the amount of water in kilograms:>>"))
# initialTemperature = float(input("Enter the initial temperature:>>"))
# finalTemperature = float(input("Enter the final temperature:>>"))
# Q = M * (finalTemperature - initialTemperature) * 4184
# print("The energy needed is %.1f"%Q)
# 5.
# balance = float(input("Enter balance:>>"))
# rate_interest = float(input("Enter rate_interest(e.g., 3 for 3%):>>"))
# interest = balance * (rate_interest / 1200)
# print("The interest is %f"%interest)
# 6.
# v0 = float(input("请输入初始速度v0:"))
# v1 = float(input("请输入末速度v1:"))
# t = float(input("请输入时间t:"))
# a = (v1 - v0) / t
# print("平均加速度为：%.4f"%a)
# 7.
# monthly_saving_amount = float(input("请输入每月存款金额/元："))
# i = 6
# rate_month = 1 + 0.00417
# sum = 0
# for x in range(i):
#     sum = (monthly_saving_amount + sum) * rate_month
# print("六个月后，账户里的数目为：%f"%sum)
# 8.
# number = int(input("请输入一个在0~1000之间的正整数:"))
# number = str(number)                  
# # 必须先转化为字符串形式
# sum = 0
# for digit in number:                      
# # digit在字符串中
#     sum += int(digit)
# print("数字的和为：%d"%sum)
