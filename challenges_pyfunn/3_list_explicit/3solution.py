from dyntaint import *

raw_input = untrusted(raw_input)

@untrusted
def capture_input():
    n = raw_input("please write your input here: ")
    return n


@ssink()
def set_variable(value):
    return value


def print_output(n):
    #add code here?
    
    # this code you will not be able to modify
    msg = set_variable(n)
    print(msg)

    
if __name__ == "__main__":
    i = capture_input()
    print_output(i)
    

#explicit flows except with the list
# would need to change the dyntaint code.
