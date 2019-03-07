#Doing things to lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ') #turns into list
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn",
"banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #last on the list more_stuff
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff"

print stuff[1] #oranges
print stuff [-1] #corn
print stuff.pop() #corn
print ''.join(stuff) #all items of stuff become a one-word string
# actually: print join(' ', things)
print '#'.join(stuff[3:5]) #element 3 and 4
