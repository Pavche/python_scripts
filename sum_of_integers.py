#!/usr/bin/python

def sum(start, end):
    result = 0
    for i in range(start, end+1):
        result+=i
    print(result)

def sum2(start, end):
    if(start>end):
        print("Start should be less than end")
        return
    result=0
    for i in range(start, end + 1):
        result += i
    return result

sum(10,50)
s = sum2(50,110)
print(s)
