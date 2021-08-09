class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.cards = []
        self.deck = []
        self.totalhealth = health
        
    def hit(self, amount):
        print(f"Hit for {amount}")
        self.health -= amount
        if self.health <= 0:
            print(f"Player has been killed, Game Over")
        print(f"Health is {self.health}")
    def heal(self, amount):
        print(f"Healed for {amount}")
        self.health += amount
        if self.health > self.totalhealth:
            self.health = self.totalhealth
        print(f"Health is {self.health}")
    def playcard(self, position, enemy):
#         print("Pre:\t"+"\n\t".join([x.__repr__() for x in self.cards]))
        played_card = self.cards.pop(position)
#         print("Post:\t"+"\n\t".join([x.__repr__() for x in self.cards]))
        print(f"Played {played_card.name}")
        if played_card.cardType == 'damage':
            enemy.hurt(played_card.value)
        elif played_card.cardType == 'heal':
            self.heal(played_card.value)
    def showcard(self):
        print("Your Hand Is: ")        
        for pos, card in enumerate(self.cards):
            print(f"\t{pos} contains {card.name}")
        

    def draw(self):
        added_card = self.deck.pop()
        self.cards.append(added_card)
            
    
    
