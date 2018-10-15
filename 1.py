#tempstr.py
#UTF-8
tempstr = input("请输入温度值：")
if   tempstr[-1] in ['F','f']:
    C = eval(tempstr[0:-1])*32
    print(C)
elif tempstr[-1] in ['C','c']:
    F = eval(tempstr[0:-1])/32
    print(F)
else :
    print("格式错误")
