#boolean practice
#any and expression that has a False is immediately False.
#any or expression that has a True is immediately True

people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats!"

if people > cats:
    print "Not many cats!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5 #adds 5 to whatever dogs was (15 here). Same as x = x + 1. Increment operator. -= too. 

if people >= dogs:
    print "People are greater than or equal to dogs"

if people <= dogs:
    print "Poeple are less than or equal to dogs"

if people == dogs:
    print "People are dogs"

if people >= dogs is True:
    print "people = dogs"
