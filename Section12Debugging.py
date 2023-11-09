# debugging

# linting
# allows us to find errors without running the code.

# ide/ editor

# read errors. Learn how to read different errors and know what they mean.

# pdb, python debugger
import pdb

def add(num1,num2):
    pdb.set_trace()
    t = 4*5
    return num1 + num2

add(4, "ashd")