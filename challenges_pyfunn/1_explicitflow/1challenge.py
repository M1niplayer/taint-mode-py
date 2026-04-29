from dyntaint import *

raw_input = untrusted(raw_input)

@untrusted
def capture_input():
    n = raw_input("please write your input here: ")
    return n


def print_output(n):
    # write some code here
    ...
    
    
if __name__ == "__main__":
    i = capture_input()
    print_output(i)
    