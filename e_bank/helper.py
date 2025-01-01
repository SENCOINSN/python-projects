"""cette classe permet de gérer la tracabilité des operations en les mettant sur un fichier

"""

class Helper:
    
    def __init__(self,filename:str):
        self.filename = filename
        
    
    def write(self,operation):
        with open(self.filename,'a') as file:
            file.write(str(operation))
            file.write("\n")
        
        print(f"Operation enregistree avec succes!!!")
            
    
    def read(self):
        with open(self.filename,'r') as file:
            for line in file:
                print(line)
            