from dyntaint import *

raw_input = untrusted(raw_input)

@untrusted
def capture_input():
    n = raw_input("please write your input here: ")
    return n


def print_output(n):
    msg = n
    print(msg)

    
if __name__ == "__main__":
    i = capture_input()
    print_output(i)


#comment
# the goal of this exercise is just to make sure the solver
# knows what is happening. it's also to get used to python2
# :⁾
# 
# pyfunn