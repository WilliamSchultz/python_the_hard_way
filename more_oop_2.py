class Employee:
   'Common base class for all employees'
   empCount = 0 #class variable

   def __init__(self, name, salary): #a special method, which is called class
   #constructor or initialization method that Python calls when you create a new
   #instance of this class. (Initialize)
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self): #You declare other class methods like normal functions
   #with the exception that the first argument to each method is self
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000) #To create instances of a class, you call the class
#using class name and pass in whatever arguments its __init__ method accepts.
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

emp1.age = 7 #You can add, remove, or modify attributes of classes and objects at any time
