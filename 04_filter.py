

numbers=[1,1,0,1,0]
def num(x):
    return x==1
print (list(map(num,numbers)))


numbers=[1.0,1.0]
x=list(map(lambda y:y==1,numbers))
print(x)