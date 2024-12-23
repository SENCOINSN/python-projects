from abc import ABC # permet de definir des classes bstraites

from typing import List
class Shape(ABC):
    
    def area(self):
        return 0 
    
class square(Shape):

    def __init__(self,length):
        self.length = length

    def area(self):
        return self.length * self.length
    

def highest(numbers: List[int]) -> int:
    return max(numbers)

def divide(a, b):
    assert b != 0
    return a / b