class Parent(object):

    def altered(self):
        print "Parent altered()"

class Child(Parent):

    def altered(self):
        print "Child before Parent altered" #chid.altered runs
        super(Child, self).altered() #call super with arguments Child and self and
        #then call the function altered on whatever on whatever it returns
        print "Child, after parent altered"

dad = Parent()
son = Child()

dad.altered()
son.altered()
