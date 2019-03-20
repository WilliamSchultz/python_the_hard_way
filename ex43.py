from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n---------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print "Central Corridor text. Shoot or dodge or tell a joke?"

        action = raw_input("> ")

        if action == "shoot":
            print "You are dead"
            return 'death'

        elif action == "dodge":
            print "Still death"
            return 'death'

        elif action == "tell a joke":
            print "Nice"
            return 'laser_weapon_armory'

        else:
            print "Does not compute"
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print "LaserWeaponArmory class, entering the armory, guess the code, 3 digits"
        code = "123"
        guess = raw_input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 4:
            print "Wrong"
            guesses += 1
            guess = raw_input("[keypad]> ")

            if guess == code:
                print "going to the bridge"
                return 'the_bridge'
            else:
                print "going to death"
                return 'death'

class TheBridge(Scene):

    def enter(self):
        print "you have a bomb, now what?"

        action = raw_input("> ")

        if action == "throw the bomb":
            print "going to death"
            return 'death'

        elif action == "slowly place the bomb":
            print "go to escape pod"
            return 'escape_pod'

        else:
            print "doe not compute, to bridge"
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print "see 5 pods, which one do you take?"

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "pod %d sucks, to death." % guess
            return 'death'

        else:
            print "you in the good pod, pod %d" % guess
            print "you win"

            return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
      return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
