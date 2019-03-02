def add(a, b):
    print "Adding %d + %d" % (a, b) #function is "called" with two "arguments"
    return a + b #so you can assign the result to a vaiable

def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d/%d" % (a, b)
    print a/b
    return a/b

print  "Let's do some math with just functions"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

#puzzle

#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#print "That becomes: ", what, "Can you do it by hand?"
#Python prints inside out here
