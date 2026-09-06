# 🟢 EASY — Passing a Function
def double(number):
    return number * 2

def apply(function, number):
    x= []
    for num in number:
        x.append(function(num))
    return x
   
    
    # Return the result of calling function with number.
    

print(apply(double, [5,5,40,10,50,60,40]))  # 10
