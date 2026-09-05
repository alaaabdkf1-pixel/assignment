"""
Python Loops Practice

Complete each function below.
Do not change the function names.
"""

# ==========================================
# Problem 1: Sum of Numbers
# ==========================================
def problem1():
    """
    Ask the user to enter a positive integer.
    Print the sum of all numbers from 1 to n.
    """
    n=int(input("enter positive integer:"))
    total=0
    for i in range(1,n+1):
        total+=i
        print (total)
    # Write your code here

    pass


# ==========================================
# Problem 2: Multiplication Table
# ==========================================
def problem2():
    """
    Ask the user to enter a number.
    Print its multiplication table from 1 to 10.
    """
    number=int(input("enter num:"))
    for i in range (1,11):
        print(f"{number*i}")
    # Write your code here
    pass


# ==========================================
# Problem 3: Count Even Numbers
# ==========================================
def problem3():
    """
    Ask the user to enter a positive integer.
    Count how many even numbers are between 1 and n.
    """
    n=int(input("enter pos integer:"))
    count =0
    for i in range (1,n+1):
        if i%2==0:
            count+=1
            print(count)

    # Write your code here
    pass


# ==========================================
# Problem 4: Guess the Secret Number
# ==========================================
def problem4():
    """
    The secret number is 15.

    Keep asking the user to guess the number
    until they enter the correct value.
    """
    secret_number=15
    guess=int(input("guess the number:"))
    while guess!=secret_number:
        print("wrong!try again.")
        guess=int(input("guess the number:"))
    print("correct the secret number 15")    
    # Write your code here
    pass


# ==========================================
# Problem 5: Draw a Square of Stars
# ==========================================
def problem5():
    """
    Ask the user to enter the size of a square.

    Print a square made of '*' characters.
    """
    size=int(input("enter the size of the square:"))
    for i in range (size):
        print("*"*size)
    # Write your code here
    pass


# ==========================================
# Main Menu
# ==========================================
if __name__ == "__main__":
    print("Python Loops Practice")
    print("1. Sum of Numbers")
    print("2. Multiplication Table")
    print("3. Count Even Numbers")
    print("4. Guess the Secret Number")
    print("5. Draw a Square of Stars")

    choice = input("\nChoose a problem to run (1-5): ")

    if choice == "1":
        problem1()
    elif choice == "2":
        problem2()
    elif choice == "3":
        problem3()
    elif choice == "4":
        problem4()
    elif choice == "5":
        problem5()
    else:
        print("Invalid choice.")