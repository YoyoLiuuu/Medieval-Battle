
#This program is by Yoyo Liu. 
#Completed 6/18/2022
#Uploaded to Github 1/21/2024

class Warrior: 
  def __init__(self):
    health = 50 #assign health 
    attack = 5 #assign attack value 
    self.init_health = health 
    self.health = health  
    self.attack = attack #make it specific to the warrior
    self.identity = "Warrior"
    self.is_alive = True
  def fight(warrior1, warrior2): #fight is two warrior, one is self (aka warrior1), the other one is warrior2
    a = warrior1
    b = warrior2#initialize them for looping purposes 
    for i in range(0, 2): #loop twice so both warrior gets attacked
      b_init_health = b.health #remember the health when this round started so calculate health points lost
      if b.identity == "Defender":
        b.health -= a.attack-b.defense #decrease attack point when defender 
      else: 
        b.health -= a.attack 
      # warrior attack second warrior, secon warrior lose the amount of health as the attack of the first warrior
      if a.identity == "Vampire":
        a.health += a.vampirism * (b_init_health-b.health) #restore health points base on other warrior's decreased amount
      elif a.identity == "Lancer":
        b.health -= a.lance * (b_init_health - b.health) #damage another 50% off of original 
      if a.health > a.init_health: 
        a.health = a.init_health #restore health point if health points exceeds max amount
      if b.health <= 0:
        b.is_alive = False
      if a.health <= 0: 
        a.is_alive = False #see if the two fighters are still alive
      a = warrior2
      b = warrior1 #switch role and loop back so both warriors get to attack
      
    if warrior1.is_alive == True and warrior2.is_alive == False: #if the first warrior is alive and second one is dead
      return True #the initiator wins 
    else: 
      return False #the initiator does not win

class Knight(Warrior):
  def __init__(self):
    super().__init__()#same __init__ as super class Warrior 
    self.attack = 7 #knight attack is stronger
    self.identity = "Knight"

class Defender(Warrior): 
  def __init__(self): 
    super().__init__()#extra defense parameter 
    defense = 2 #assign defense
    self.health = 60
    self.init_health = 60
    self.attack = 3
    self.defense = defense #reassign value according to defense 
    self.identity = "Defender"
    
class Vampire(Warrior):
  def __init__(self):
    super().__init__()#extra vampirism parameter 
    vampirism = 0.5
    self.health = 40
    self.init_health = 40
    self.attack = 4
    self.vampirism = vampirism 
    self.identity = "Vampire"

class Lancer(Warrior):
  def __init__(self): 
    super().__init__()
    lance = 0.5 #extra lance value
    self.health = 50 
    self.init_health = 50
    self.attack = 6 
    self.lance = lance #lance value
    self.identity = "Lancer"

class Healer(Warrior):
  def __init__(self, ally):
    super().__init__()
    self.health = 60
    self.init_health = 60
    self.attack = 0 #cannot attack 
    self.identity = "Healer"

  def heal(self, ally): #heal tha ally
    ally.health += 2
    if ally.health > ally.init_health: 
      ally.health = ally.init_health

Walter = Warrior() #John is a warrior 
Kitty = Knight()
Den = Defender()
Venessa = Vampire()
Laura = Lancer()
Helen = Healer(Kitty) #initiate Helen with Knight, will change later once player choose character

character_list = [Walter, Kitty, Den, Venessa, Laura, Helen] #store all characters in a list, so it's easier to call when player picks an character

confirm = "n" #confirm the characters chosen   
no_healer = True 

while confirm == "n": 
  print("Hello! Welcome to Medieval Battle!")
  print("This is a three player game. Here are all the characters: \n1 - Walter: Warrior \n2 - Kitty: Knight \n3 - Den: Defender \n4 - Venessa: Vampire \n5 - Laura: Lancer \n6 - Helen: Healer \nNote: Helen cannot attack, she can only heal her ally.") #introduce characters 
  instruction = input("Do you want to see the instructions? [y/n]")
  if instruction == "y": 
    print("\n\n\n")
    print("Welcome to the Medieval Battle, a 3 player game with only 1 winner.")
    print("There are 6 characters you can choose from, listed above. Each of them have different initial health points and level of attacks. Here are the specifics:\n")
    print("Warrior: Initial Health - 50; Attack - 5")
    print("Knight: Initial Health - 50; Attack - 7")
    print("Defender: Initial Health - 60; Attack - 3; Defense - 2")
    print("Vampire: Initial Health - 40; Attack: 4; Special Trait: Restore Damage*")
    print("Lancer: Initial Health - 50; Attack - 6; Special Trait: Lance**")
    print("Healer: Initial Health = 60; Attack - 0; Special Trait: Ally with Another Player***")

    print("*: When the Vampire hits the other unit, he restores his health by +50% of the dealt damage (enemy defense makes the dealt damage value lower)")
    print("**: When the Lancer hits the other unit, he also deals a 50% of the deal damage to the enemy unit, standing behind the firstly assaulted one (enemy defense makes the deal damage value lower.)")
    print("***: Every time the allied soldier hits the enemy, the Healer will heal the allie by adding 2 health points to the current health. Note that the health after healing can't be greater than the maximum health of the unit.\n")

    print("How does the game work?")
    print("Each player will battle with the two other players. Player 1 will initiate a battle against player 2, player 2 will initiate a battle against player 3, and player three will initiate a battle with player 1. A player can only win if they initiate the battle (For example, for a battle between player 1 and player 3, only player three is able to win). The winner of each battle is determined by the death (health point less than or equal to 0) of the opponent. For each battle, the players can enter the number of rounds they want to fight the other players. Each round, the player will loss certain health point (the attack point of their opponent). The more round per battle, the more health points lost. By the end of each battle, player may be alive or dead. If the player is dead, the initiator of the battle is the winner. If multiple players died during the same battle, there will be two winners. If all player is dead, there will be no winner. If no player is dead, another battle will begin, and the players can pick how many rounds they want to fight the other two players once again.")
    print("\n\n\n")

  #associate players with characters
  player1 = input("Player 1 please choose a character.")
  player1_chara = character_list[int(player1)-1] 
  player2 = input("Player 2 please choose a character.")
  player2_chara = character_list[int(player2)-1]
  player3 = input("Player 3 please choose a character. ")
  player3_chara = character_list[int(player3)-1]
  print("Please confirm, Player one's identity is", player1_chara.identity, "\nPlayer two's identity is", player2_chara.identity, "\nPlayer three's identity is", player3_chara.identity, "[y/n]") # confirm characters 
  confirm = input()
  if player1 == player2 or player1== player3 or player2 == player3: 
    #if the characters are the same, for a better gaming experience, ask the players to re-select 
    confirm = "n"
    print("Wait a second, it seems all three characters are the same, please choose another character!")

healing = '' #no object associate with the healing ally 

if player1 == "6" or player2 == "6" or player3 == "6": 
  alliance = input("Who is your ally? (Please enter the number associated with the ally you want to heal, for instance '4' for Venessa. ")
  healing = character_list[int(alliance)-1] #find who is ally of Helen 
  
print("Awesome! Let's start the game.")

game_stop = False  

battle = 1

while game_stop == False: #continue with more battles until the death of a player  
  print("Battle", battle) #battle number 
  
  onevtwo = int(input("Player one and two, how many rounds do you want to fight?"))
  twovthree = int(input("Player two and three, how many rounds do you want to fight?"))
  onevthree = int(input("Player three and one, how many rounds do you want to fight?")) #pick rounds 
  
  print("The battle has begun!")

  for i in range(1, onevtwo+1): #loop for how many rounds the player entered
    player1_win = player1_chara.fight(player2_chara) #player 1 vs player 2
    if player1_chara == healing: 
      Helen.heal(healing)
    elif player2_chara == healing: 
      Helen.heal(healing)  
    if player1_win: 
      print("Wow! Player 1, you have successfully won the battle against player 2 and caused player 2's death.")
  for i in range(1, onevthree+1):
    player3_win = player3_chara.fight(player1_chara) #player 3 vs player 1
    if player1_chara == healing: 
      Helen.heal(healing)
    elif player3_chara == healing: 
      Helen.heal(healing)
    if player3_win: 
      print("Wow! Player 3, you have successfully won the battle against player 1 and caused player 1's death.")
      break
  for i in range(1, twovthree+1):
    player2_win = player2_chara.fight(player3_chara) #player 2 vs player 3
    if player2_chara == healing: 
      Helen.heal(healing)
    elif player3_chara == healing: 
      Helen.heal(healing)
    if player2_win: 
      print("Wow! Player 2, you have successfully won the battle against player 3 and caused Player 3's death.")
      break
  if player1_win == False and player2_win == False and player3_win == False: 
    print("Now, player 1's health point is", player1_chara.health, "\nPlayer 2's health point is", player2_chara.health, "\nPlayer 3's health point is", player3_chara.health) #if no one dies, display health points left 
    battle += 1 #move on to the next battle 
  else: 
    game_stop = True #if someone died 
    print("Game end! A player's death has caused the game to stop!") #game end 
    
if player1_win and player2_win == False and player3_win == False: 
  print("Player 1 is the winner!")
elif player2_win and player1_win == False and player3_win == False: 
  print("Player 2 is the winner!")
elif player3_win and player2_win == False and player1_win == False: 
  print("Player 3 is the winner!") #print single winner 
elif player1_win == False and player2_win ==False and player3_win == False: 
  print("Oh no! Looks like everyone's dead... Seems like we don't have a winner.") #print no winner
else: 
  print("Looks like we have two winners!")
  if player1_chara.health <= 0: 
    print("Player 1 is the only loser...")
  if player2_chara.health <= 0: 
    print("Player 2 is the only loser...") 
  if player3_chara.health <= 0: 
    print("Player 3 is the only loser...") #print multiple winners 

print("Thanks for playing the game!") #End game