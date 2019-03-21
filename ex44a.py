class Parent(object):

    def implicit(self):
        print "Parent implicit()"

class Child(Parent):
    pass #a placeholder when a statement is required syntactically,
    #but no code needs to be executed

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
