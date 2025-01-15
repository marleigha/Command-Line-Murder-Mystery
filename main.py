import sys,time,random

typing_speed = 70 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)


playerStrengthMod = 3
playerDexMod = 5
playerWisdomMod = -3
playerIntelligenceMod = 0


class Choice:
  def __init__(self, story, options, nextChoices, roll):
    self.story = story
    self.options = options
    self.nextChoices = nextChoices
    self.roll = roll

  def runChoice(self):
    print("********\n")
    slow_type(self.story)
    print("********\n")
    x = 1
    for option in self.options:
      print(str(x) + ".)", option + '\n')
      x+= 1
    if len(self.nextChoices) == 0:
      print("*** fin ***")
      return
    playerChoice = int(input("what do you choose: ")) -1
    #first need to parse and make sure it's numeric, so probably best to have a try catch

    #check and make sure the choice is an int, and in range of next choices
    while playerChoice not in range(len(self.nextChoices)):
      print("not very good input")
      playerChoice = int(input("what do you choose: ")) -1
    
    if self.nextChoices[playerChoice].roll:
       roll = random.randint(1, 20)
       print("you rolled:", roll)
       if roll <= 10:
          print("failed roll")
          return
    
    self.nextChoices[playerChoice].runChoice()
      
    # 	print("not very good input")
    #self.nextChoices[playerChoice].runChoice()
        
# c2 = Choice('c2', "Mystery is solved! Someone's cat is loose", [], True)
# c3 = Choice('c3', "Dude. rip you.", [c2], True)
# c1 = Choice('c1', "You are in a haunted mansion!\n 1. Solve the mystery!\n 2. Wait and let the killer get you", [c2, c3], False)

# c1.runChoice()

# class Player:
#     def __init__(self, name, description, strength, dexterity, constitution, intelligence, wisdom, charisma):
#         self.name = name
#         self.description = description
#         self.strength = strength
#         self.dexterity = dexterity
#         self.constitution = constitution
#         self. intelligence = intelligence
#         self.wisdom = wisdom
#         self.charisma = charisma

#     def __str__(self):
#         return self.name

# runner = Player("the runner", "won three highschool track medals", 20, 20, 10, 7, 12, 15)
# #print(runner)
