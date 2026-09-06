# 🟡 MEDIUM — Custom Sorting
names = ["Ahmed", "Ali", "Mohamed", "Sara", "Omar"]

# Sort from shortest name to longest using sorted() and key.
sorted_names = []
sorted_names= sorted(names,key=lambda name:len(name))
print(sorted_names)
