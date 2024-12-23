class Person:
    def __init__(self,name):
        self.name = name
    

    def walk(self):
        print(self.name + " is walking")
        

class Fish(Person):
    def __init__(self,name):
        super().__init__(name)
    def swim(self):
        print(self.name + " is swimming")
        

volunteers = [Person("John"),Person("Jack"),Person("Jim"),Fish("Bob")]

for person in volunteers:
    if(isinstance(person,Person)):  # equivalent need to know if has walk method if hasattr(person,"walk")
        person.walk()
    
    if(isinstance(person,Fish)):
        person.swim()