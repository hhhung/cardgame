class Card:
    def __init__(self, name, cardType, value):
        self.name = name
        self.cardType = cardType
        self.value = value        
    
    def __repr__(self):
        return f"{self.cardType} {self.name} [{self.value}]"
