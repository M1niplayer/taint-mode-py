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
    
    del n.taints
    
    msg = set_variable(n)
    print(msg)

    
if __name__ == "__main__":
    i = capture_input()
    print_output(i)


# also a warmup
# should not allow del?
# should be renaming but uhhhh
# a bit hard to do that?
# could just remove this for now
