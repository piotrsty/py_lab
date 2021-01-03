class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
point.x = 11
print(point.x)

#exercise
class Person:
    #we call this new method a constructor; 'name' is parameter
    def __init__(self, name):
        #self references the current object we're setting the name attribute of the current object, to the name argument passed to this method 
        self.name = name 


    def talk(self):
        print(f"Hi, I am {self.name}")


#john = Person()
john = Person("John Smith")
#print(john.name)
john.talk()
#each object is a different instance of a person class
bob = Person("Bob Smith")
bob.talk()
