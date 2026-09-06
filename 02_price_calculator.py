# 🔴 HARD — Price Calculator
# 1. map(): apply 10% discount
# 2. filter(): keep discounted prices >= 50
prices = [100, 40, 80, 30, 200]


discounted = []
discounted=list(filter(lambda x:x*0.9,prices))
final_prices = []
discounted=list(filter(lambda x:x>50,discounted))
print(discounted)   # [90.0, 36.0, 72.0, 27.0, 180.0]
print(final_prices) # [90.0, 72.0, 180.0]
