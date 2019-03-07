from sys import exit

def gold_room():
    print "This room is full of gold. How much can you take?"

    next = raw_input(">")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print "Nice, your're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard")

def bear_room():
    print "There is a bear here"
    print "The bear has a bunch of honey"
    print "The bear is in front of another door"
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input(">")

        if next == "take honey":
            dead("The bear looks at you then slaps your face")
        elif next == "taunt bear" and not bear_moved:
            dead("The bear moved")
            bear_moved = True
        elif next == "open door" and not bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."

def cthulhu_room():
    print "Here you see the great evel Cthuhu."
    print "He, it, whatever stares at you and you go insane"
    print "Do you flee for your life or eat your head?"

    next = raw_input(">")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty")
    else:
        cthulhu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start(): #beginning
    print "You are in a dark room."
    print "There is a door to your right and left"
    print "Which one do you take?"

    next = raw_input(">")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stubmble around the room until you starve")

start()

#CTRL c to exit in terminal
