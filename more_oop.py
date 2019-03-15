class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("bark bark")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old.")

    def birthday(self):
        self.age += 1

    def setBuddy(self, buddy):
        self.buddy = buddy
        buddy.buddy = self

'''
ozzy = Dog("Ozzy", 2)
skippy = Dog("Skippy", 12)
filou = Dog("Filou", 8)

print(ozzy.age)
ozzy.birthday()
print(ozzy.age)
ozzy.doginfo()
skippy.doginfo()
filou.doginfo()
'''
ozzy = Dog("Ozzy", 2)
filou = Dog("Filou", 8)

ozzy.setBuddy(filou)

print(ozzy.buddy.name)
print(ozzy.buddy.age)
print(filou.buddy.age)
print(filou.buddy.name)
ozzy.buddy.doginfo()
