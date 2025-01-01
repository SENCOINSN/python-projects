import datetime
from .errors import BusinessError,InsufficientFundsError
from .helper import Helper

class Operation:
    def __init__(self,account,amount):
        self.account = account
        self.amount = amount
        self.dateOperation = datetime.datetime.now()
        self.helper = Helper("operations.txt")
        
    def __str__(self):
        return f"Operation de {self.amount} FCFA sur le compte {self.account} le {self.dateOperation}"
    
class Deposit(Operation):
    def __init__(self, account, amount):
        super().__init__(account, amount)
        
    
    def deposit(self,amount):
        # verifier d'abord si le montant est positif
        if amount < 0:
            raise BusinessError("Le montant doit etre positif")
        
        self.account.setSolde(self.account.getSolde() + amount)
        
        print(f"Depot de {amount} FCFA effectue avec succes sur le compte {self.account.getAccountNumber()}")
        #enregistrer l'operation dans le fichier
        self.helper.write(self) 
        
        
        
       
class WithDrawal(Operation):
    def __init__(self, account, amount):
        super().__init__(account, amount)

    
    def execute(self,amount):
        """Effectuer un retrait"""
        
        if amount <0:
            raise BusinessError("Le montant doit etre positif")
        
        if self.account.getSolde() < amount:
            raise InsufficientFundsError("Solde insuffisant pour effectuer cette operation")
        
        self.account.setSolde(self.account.getSolde() - amount)
        print(f"Retrait de {amount} FCFA effectue avec succes sur le compte {self.account.getAccountNumber()}")
        #enregistrer l'operation dans le fichier
        self.helper.write(self)
        


class Transfer(Operation):
    def __init__(self,account,amount,recipient_account):
        super().__init__(account,amount)
        self.recipient_account = recipient_account
        
    
    def execute(self,amount):
        """Effectuer un transfert"""
        if amount <0:
            raise BusinessError("Le montant doit etre positif") 
        
        if self.account.getSolde() < amount:
            raise InsufficientFundsError("Solde insuffisant pour effectuer cette operation") 
        
        # on verifie si le compte du receveur existe
        if self.recipient_account == None:
            raise BusinessError("Compte destinataire invalide") 
        
        self.account.setSolde(self.account.getSolde() - amount) 
        self.recipient_account.setSolde(self.recipient_account.getSolde() + amount)
        
        print(f"Transfert de {amount} FCFA effectue avec succes sur le compte {self.account.getAccountNumber()} vers le compte {self.recipient_account.getAccountNumber()}")
        #enregistrer l'operation dans le fichier
        self.helper.write(self)
        
        


