class Other(object):

    def override(self):
        print "Other override"

    def implicit(self):
        print "Other implicit"

    def altered(self):
        print "Other altered"

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit() #prints other implicit

    def override(self):
        print "Child override"

    def altered(self):
        print "Child before other altered"
        self.other.altered() #prints other altered
        print "Child after other altered"

son = Child()

son.implicit()
son.override()
son.altered()

#composition: calling functions in another class

#“In Python, however, classes act as templates that “mint” new objects,
#similar to how coins were minted using a die (template).”
