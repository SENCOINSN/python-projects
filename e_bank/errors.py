

class BusinessError(Exception):
    """Exception raised for errors for the transaction."""
    
    def __init__(self, message="Transaction error"):
        self.message = message
        super().__init__(self.message)
        

class InsufficientFundsError(Exception):
    """Exception raised for errors in the amount of funds."""

    def __init__(self, message="Insufficient funds"):
        self.message = message
        super().__init__(self.message)