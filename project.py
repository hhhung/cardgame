import random
import time
from card import Card
from enemy import Enemy
from player import Player
while True:
    difficulty = input(f"Choose Your Difficulty: 1. Easy 2. Normal 3. Hard ")
    if difficulty == "1":
        goblin = Enemy('Goblin', 1)
        break
    elif difficulty == "2":
        goblin = Enemy('Orc', 2)
        break
    elif difficulty == "3":
        goblin = Enemy('Blackguard', 3)
        break
    else:
        print("Select a valid difficulty")
player = Player('Johan Von Generico', 30)

for i in range(15):
    player.deck.append(Card('Dagger', 'damage', 4))
for i in range(2):
    player.deck.append(Card('Dagger but poisoned', 'damage', 6))
for i in range(4):
    player.deck.append(Card('Healing Word', 'heal', 4))
for i in range(3):
    player.deck.append(Card('Shield', 'armour', 6))
if difficulty == "1":
    wave = 3
elif difficulty == "2":
    wave = 2
elif difficulty == "3":
    wave = 1
random.shuffle(player.deck)
for i in range(4):
    player.draw()
for i in range(int(wave)):
    goblin.health = goblin.total_health
    goblin.armour = goblin.original_armour
    print(f"{player.name} encountered {goblin.name}!")
    while player.health > 0 and goblin.health > 0:    
        print(f"{player.name}'s Turn")
        player.draw()
        player.showcard()
        played = int(input("Choose your card "))
        player.playcard(played, goblin)
        time.sleep(1)
        if goblin.health <= 0:
            break
        print(f"{goblin.name}'s Turn")
        goblin.chooseCard(player)
        time.sleep(1)
