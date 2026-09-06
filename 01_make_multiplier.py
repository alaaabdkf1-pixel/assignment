# 🟡 MEDIUM — Returning a Function
def make_multiplier(n):
    # Return a function that multiplies its input by n.
    def multiplier(x):
        return x*n
    return multiplier
    pass

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(7))  # 14
print(triple(7))  # 21
#return lambda x:x*n
