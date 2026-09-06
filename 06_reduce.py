from functools import reduce

numbers = [1, 2, 3, 4, 5]
num=[40,58,45,67]
print(reduce(lambda a, b: a + b, numbers))
print(reduce(lambda a, b: a * b, numbers))
print(reduce(lambda a,b,c,d,e : (a+b+c+d+e)/2))
nums =[1,1,1]
print(reduce(lambda a, b: a > 0 and b > 0,nums))


