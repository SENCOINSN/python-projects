class Rectangle:
   
    desc = "description d'un rectangle"
    el=2
    
    def __init__(self,lenght,width,color='red'):
        self.length = lenght
        self.width = width
        self.color = color
        
        
            
    
    def caculate_area(self):
        return self.width * self.length
    
    @classmethod
    def description(cls,el):
        return f"cette méthode est une classe de methode {cls.el}"
    
    
rectangle = Rectangle(12,3,"yellow")

print(" calcul area is ", rectangle.caculate_area())

print(" lenght  ", rectangle.length)

print(Rectangle.desc)

print(Rectangle.description(3))
