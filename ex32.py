the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#first for loop goes through a list
for number in the_count:
    print "This is count %d" % number

for fruit in fruits:
    print "A fruit of type: %s" % fruit

#mixed lists
#%r because we don't know what the data type is
for i in change:
    print "I got %r" % i

#build lists
elements = []

#use range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list" % i
    #append is a function that lists Understand
    elements.append(i)
#elements.append(range(0, 6))

#now we print them
for i in elements:
    print "Element was: %d" % i
