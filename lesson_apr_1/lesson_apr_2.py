# -*- coding: utf-8 -*-

# function

# def my_first_function(num1, num2 = 10):
#     a = num1 + num2
#     return a
# print(my_first_function(0, 0))
#
# def my_second_function():
#     a = 2 + 2
#     return a
# print(my_second_function())
#
# num = my_first_function(3) + my_second_function()
# print(num)

# def sum_nums(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
# x = sum_nums(2, 2, 10, 20)
# print(x)


def my_test(**kwargs):
    for i in kwargs:
        print(i)

my_test(p1='test', arg2=22,a=[1,2,3,])
