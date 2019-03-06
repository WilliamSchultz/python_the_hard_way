
def while_func(upper_limit, increment):
    i = 0
    numbers = []

    while i < upper_limit:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


#print "The numbers: "

#for num in numbers:
    #print num

#while_func(10, 2)


def for_version():
    for i in range(0, 10):
        numbers = []
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + i
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i


for_version()
