#modules are like dictionaries with key: value relationship
#module: get python code and use it with the . operator
#class: a way to take a grouping of functions and data
#and place them inside a container to access with . operator
#class: mini module
#OOP: means there is a contruct called a class
#instatiate (create) a class, you get an object
#Instantiation is create and import at the same time
#Python creates an empty object with all the functions in the class with def
#self is the empty object python made, and you can set variables on it
#

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",   #list 0
                   "I don't want to get sued", #list 1
                   "So I'll stop right there"]) #list 2

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
