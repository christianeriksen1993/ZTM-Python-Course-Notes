def do_stuff(num=0):
    try:
        if type(num) == str:
            return int(num) + 5
        elif type(num) == list:
            for i in num:
                num[num.index(i)] += 5
            return num
        elif num:
            return num + 5
        else:
            return "Please enter number"
    except ValueError as err:
        return err
        

from random import randint
import sys

def guess_func(guess, answer):
    if  0 < guess < 11:
        if guess == answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')
        return False


if __name__ == '__main__':
    answer = randint(1, 10)
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if guess_func(guess, answer):
                break
        except ValueError:
            print('please enter a number')
            continue    



