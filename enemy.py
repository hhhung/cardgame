class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.cards = []
        self.total_health = health
        self.fatigue = False
        
    def hurt(self, amount):
        print(f"{self.name} hit for {amount}")
        self.health -= amount
        if self.health <= 0:
            print(f" {self.name} has been killed")
    def restore(self, amount):
        print(f"{self.name} heals for {amount}")
        self.health += amount
        
    def chooseCard(self, player):
        if self.health <= (self.total_health / 2) and self.health >= (self.total_health / 3):
            player.hit(3)
            self.fatigue = False
        elif self.health <= (self.total_health / 3) and self.fatigue == False:
            self.restore(5)
            self.fatigue = True
        else:
            player.hit(5)
            self.fatigue = False
            