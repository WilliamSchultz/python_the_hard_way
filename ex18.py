#Functions:
#1. They name pieces of code the way variables name strings and numbers
#2. They take arguments the way scripts take argv
#3. Using 1 and 2, they let you make your own tiny commands
# Create a function by using def

def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

def print_none():
    print "I got nothing"


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First")
print_none()

# to run, call or use a function, all mean the same thing
