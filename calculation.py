from math import *

'''
可以使用 pi E 关键词，也可以使用ans表示上一次的答案
可以使用科学计数法，如1e4=10000 ,1e-1=0.1，注意小写e不能直接作为自然常数使用，如要请使用E.
制作by 零殇_Fan
'''


def cal_binary(l, sign, r):
    l = l.replace("em", "e-")
    r = r.replace("em", "e-")
    if l.find("m") == -1:
        left = float(l)
    else:
        left = -float(l[1:])
    if r.find("m") == -1:
        right = float(r)
    else:
        right = -float(r[1:])
    if sign == "^":
        return pow(left, right)
    if sign == "*":
        return left * right
    if sign == "/":
        return left / right
    if sign == "+":
        return left + right
    if sign == "-":
        return left - right
    return 0


def find_first_sign(string):
    index = -1
    max_priority = 0
    cnt = 0
    for i in string:
        if cnt == 0:
            cnt = cnt + 1
            continue
        if i == '^' and max_priority < 10:
            max_priority = 10
            index = cnt
        if (i == "*" or i == '/') and max_priority < 8:
            max_priority = 8
            index = cnt
        if (i == '+' or i == '-') and max_priority < 6:
            max_priority = 6
            index = cnt
        cnt = cnt + 1
    if index > 0:
        return index
    else:
        return -1


def calculate(string):
    find = find_first_sign(string)
    while find != -1:
        string_sign = string
        string_sign = string_sign.replace("e-", "ee")
        string_sign = string_sign.replace("*", "#")
        string_sign = string_sign.replace("/", "#")
        string_sign = string_sign.replace("+", "#")
        string_sign = string_sign.replace("-", "#")
        string_sign = string_sign.replace("^", "#")
        l = int(string_sign.rfind("#", 0, find)) + 1
        r = int(string_sign.find("#", find + 1))
        if l == -1 or l == 1:
            l = 0
        if r == -1:
            r = len(string)
        string = string[0:l] + str(cal_binary(string[l: find], string[find], string[find + 1: r])) + string[
                                                                                                     r:len(string)]
        find = find_first_sign(string)
    string = string.replace("-", "m")
    string = string.replace("em", "e-")
    return string


ans = 0.0
while True:

    str1 = input("Please Input A Formula:\n")
    if str1.lower() == "exit" or str1.lower() == "":
        break
    strL = ""
    str1 = str1.replace("Ans", str(ans))
    str1 = str1.replace("ans", str(ans))
    str1 = str1.replace("pi", str(pi))
    str1 = str1.replace("PI", str(pi))
    str1 = str1.replace("E", str(e))
    str1 = str1.replace("e-", "em")
    while str1.find(")") != -1:
        strL = str1[0:str1.find(")")]
        strSub = str1[strL.rfind("(") + 1:len(strL)]
        str1 = str1[0:strL.rfind("(")] + calculate(strSub) + str1[str1.find(")") + 1:len(str1)]
    str1 = calculate(str1)
    str1 = str1.replace("m", "-")

    num = float(str1)
    ans = num
    _e = 0
    if num > 10000:
        while abs(num) > 10:
            num = num / 10
            _e += 1
    if num < 0.00001 and num != 0:
        while abs(num) < 1:
            num = num * 10
            _e -= 1
    if _e == 0:
        print("Ans=" + str(num))
    else:
        print("Ans=" + str(num) + "e" + str(_e))
    print("----------------------")
