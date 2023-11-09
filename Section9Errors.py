# Error handling

"""while True:
    try:
        age = int(input("What is your age?"))
        10/age
    except ValueError:
        print("please enter a number")
    except ZeroDivisionError:
        print("Please enter age higher than 0")
    else:
        print("Thank you!")
        break"""

# 160. Error handling 2

"""def sum(num1, num2):
    try:
        return num1 + num2/num1
    except (TypeError, ZeroDivisionError) as err:
        print(f"Please enter numbers and don't divide by zero {err}")


print(sum(0, 2))"""

# 161. Error handling Exercise 

while True:
    try:
        age = int(input("What is your age?"))
        10/age
        raise ValueError("Hey cut it out")
    except ZeroDivisionError:
        print("Please enter age higher than 0")
        break
    else:
        print("Thank you!")
    finally:
        print("ok, I am finally done")
    print("can you hear me?")