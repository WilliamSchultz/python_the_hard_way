# format specifiers
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %r - representation of a string (exactly as is)

x = "There are %d types of people." % 10
binary = 'binary'
do_not = "don't"
y = "Those who konw %s and those who %s" % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: %s" % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious

w = "This is the left side of the..."
e = "a string with a right side"

print w + e
