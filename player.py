class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.cards = []
        self.deck = []
        self.totalhealth = health
        self.armour = 0
        
    def hit(self, amount):
        if self.armour == 0:
            pass
        elif amount >= self.armour:
            amount -= self.armour
            self.armour = 0
            print("Damage blocked by armour")
            print("Armour has broken")
        elif amount < self.armour:
            self.armour -= amount
            amount = 0
            print("Damage blocked completely by armour")
            print(f"Armour is now {self.armour}")        
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
        elif played_card.cardType == 'armour':
            self.armour += played_card.value
            print(f"{self.name} has {self.armour} armour")
    def showcard(self):
        print("Your Hand Is: ")        
        for pos, card in enumerate(self.cards):
            print(f"\t{pos} contains {card.name}")
        

    def draw(self):
        added_card = self.deck.pop()
        self.cards.append(added_card)
