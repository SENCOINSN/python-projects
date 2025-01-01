import random
import string


class Client:
    def __init__(self,nom,prenom,date_naissance,adresse,telephone,email):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.adresse = adresse
        self.telephone = telephone
        self.email = email
        
    
    def __str__(self):
        return f"{self.nom} {self.prenom} : {self.email} - {self.telephone} - {self.adresse}"
    
    def generate_username_password(self):
        self.username = "USER"+str(random.randint(1,999))
        return self.username
    
    def generate_password(self,length):
        all_chars = string.ascii_letters + string.digits + string.punctuation
        if(length<8):
            print("Password length must be at least 8 characters")
            return None
        
        self.password = ''.join(random.choice(all_chars) for i in range(length))
        return self.password
        


class Compte:
    
    def __init__(self,solde,account_number,client,accountType='courant',rate=0):
        self.solde = solde
        self.account_number = account_number
        self.client = client
        self.accountType = accountType
        self.rate = rate
        
    
    def __str__(self):
        return f"Compte {self.account_number} : {self.solde} FCFA - Client:
      {self.client.nom} {self.client.prenom} - {self.client.email}"
      
    def getAccountType(self):
        return self.accountType
    
    def getSolde(self):
        return self.solde
    
    def setSolde(self,solde):
        self.solde = solde
        
    
    def getAccountNumber(self):
        return self.account_number
    
    def getClient(self):
        return self.client
    


    
    