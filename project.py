import random
import time
from card import Card
from enemy import Enemy
from player import Player

difficulty = input(f"Choose Your Difficulty:1. Easy 2. Normal 3. Hard type the corrosponding number to select")
if difficulty == "1":
    goblin = Enemy('Goblin', 7)
elif difficulty == "2":
    goblin = Enemy('Orc', 12)
elif difficulty == "3":
    goblin = Enemy('Blackguard', 20)
player = Player('Johan Von Generico', 20)

for i in range(15):
    player.deck.append(Card('Dagger', 'damage', 4))
for i in range(2):
    player.deck.append(Card('Dagger but poisoned', 'damage', 6))
for i in range(8):
    player.deck.append(Card('Healing Word', 'heal', 4))

random.shuffle(player.deck)
for i in range(4):
    player.draw()

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