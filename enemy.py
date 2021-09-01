class Enemy:
    def __init__(self, name, difficulty):
        self.name = name
        if difficulty == 1:
            self.health = 7
            self.armour = 0
            self.damage = 3
        elif difficulty == 2:
            self.health = 12
            self.armour = 2
            self.damage = 4
        elif difficulty == 3:
            self.health = 18
            self.armour = 5
            self.damage = 5
        self.cards = []
        self.original_armour = self.armour
        self.total_health = self.health
        self.fatigue = False
        self.pause = True
        if difficulty >= 2:
            self.spare_armour = True
        
    def hurt(self, amount):
        if self.armour == 0:
            pass
        elif amount >= self.armour:
            amount -= self.armour
            self.armour = 0
            print(f"{self.name}'s armour blocked the attack")
            print(f"{self.name}'s armour has broken")
        elif amount <= self.armour:
            self.armour -= amount
            amount = 0
            print(f"{self.name}'s armour completely blocked the attack")
        print(f"{self.name} hit for {amount}")
        self.health -= amount
        if self.health <= 0:
            print(f" {self.name} has been killed")
    def restore(self, amount):
        print(f"{self.name} heals for {amount}")
        self.health += amount
    def armoured(self, amount):
        print(f"{self.name} gains armour.")
        self.armour += amount
        
    def chooseCard(self, player):
        if self.health <= (self.total_health / 2) and self.health >= (self.total_health / 3):
            player.hit(self.damage - 2)
            self.fatigue = False
            self.pause = False
        elif self.health <= (self.total_health / 3) and self.fatigue == False:
            self.restore(self.damage)
            self.fatigue = True
            self.pause = False
        elif difficulty >= 2 and self.armour <= 0 and self.spare_armour == True and self.pause == False:
            self.armoured(self.original_armour)            
            self.spare_armour = False
            self.fatigue = False
        else:
            player.hit(self.damage)
            self.fatigue = False
            self.pause = False
            
            
