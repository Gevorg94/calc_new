
def my_func():
    num_one = int(input("Enter your first number: "))
    num_sec = int(input("Please enter second number: "))

    operation = input("Please choose preferred operator '+','-','*','/', '%'")
    print("===============================================")
    if operation == "+":
        return num_one + num_sec
    elif operation == "-":
        return num_one - num_sec
    elif operation == "*":
        return num_one * num_sec
    elif operation == "/":
        return num_one / num_sec
    elif operation == "%":
            return num_one % num_sec
    else:
        print("Run the program again")



print(my_func())
