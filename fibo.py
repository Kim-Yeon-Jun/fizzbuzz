from math import sqrt
def fibo(num):

#   if num < 2 :
#       return num
#   else:
#       return fibo(num-1) + fibo(num-2)
#
# print(fibo(5))

    root_5 = 5 ** 0.5
    phi = ((1+root_5)/2)
    
    a = ((phi**num) - ((-phi)**-num))/root_5
    return round(a)

print(fibo(5))
