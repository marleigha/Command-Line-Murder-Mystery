import sys,time,random

typing_speed = 101 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)


# playerStrengthMod = 3
# playerDexMod = 5
# playerWisdomMod = -3
# playerIntelligenceMod = 0


class Choice:
  def __init__(self, story, succOptions, failOptions, succNextChoices, failNextChoices, roll, DC):
    self.story = story # [] of strings
    self.succOptions = succOptions
    self.failOptions = failOptions
    self.succNextChoices = succNextChoices
    self.failNextChoices= failNextChoices
    self.roll = roll
    self.DC = DC

  def runChoice(self):
     if self.roll:
        roll = random.randint(1,20)
        print("\n your roll was:", roll, "\n")
        if roll < self.DC:
          print("********\n")
          slow_type(self.story[1])
          print("\n********\n")
          x = 1
          for option in self.failOptions:
            print(str(x) + ".)", option + '\n')
            x+= 1
            if len(self.failNextChoices) == 0:
              print("*** fin ***")
              return
          playerChoice = int(input("what do you choose: ")) -1
  #   #first need to parse and make sure it's numeric, so probably best to have a try catch

  #   #check and make sure the choice is an int, and in range of next choices
          while playerChoice not in range(len(self.failNextChoices)):
            print("not very good input")
            playerChoice = int(input("what do you choose: ")) -1
    
          self.failNextChoices[playerChoice].runChoice()

    #the success path
     if (not self.roll or roll >= self.DC):
        print("********\n")
        slow_type(self.story[0])
        print("\n********\n")
        x = 1
        for option in self.succOptions:
            print(str(x) + ".)", option + '\n')
            x+= 1
        if len(self.succNextChoices) == 0:
            print("*** fin ***")
            return
        playerChoice = int(input("what do you choose: ")) -1
          #first need to parse and make sure it's numeric, so probably best to have a try catch

          #check and make sure the choice is an int, and in range of next choices
        while playerChoice not in range(len(self.succNextChoices)):
            print("not very good input")
            playerChoice = int(input("what do you choose: ")) -1
          
        self.succNextChoices[playerChoice].runChoice()

class Player:
  def __init__(self, name, description, strength, dexterity, constitution, intelligence, wisdom, charisma):
      self.name = name
      self.description = description
      self.strength = strength
      self.dexterity = dexterity
      self.constitution = constitution
      self. intelligence = intelligence
      self.wisdom = wisdom
      self.charisma = charisma
       
  def __str__(self):
        return self.name

runner = Player("the runner", "won three highschool track medals", 20, 20, 10, 7, 12, 15)
print(runner)

     
c4 = Choice(["you go home and eat with your family"], [], [], [], [], False, 0)
c5 = Choice(["you take a nap and the killer gets you"], [], [], [], [], False, 0)
c6 = Choice(["the cat becomes your friend! yippee"], [], [], [], [], False, 0)
c3 = Choice(["you look elsewhere and find a cat"], ["pet cat"], [], [c6], [], False, 0)
c7 = Choice(["you make the door worse and the killer gets you"], [], [], [], [], False, 0)
c2 = Choice(["you break the door down! you're safe", "hit the gym, the door didn't budge."], ["go home", "take a nap"], ["try to break the door again", "look elsewhere"], [c4, c5], [c7, c3], True, 19)
c1 = Choice(["the door is locked"], ["break the door (you have to roll!)", "look elsewhere"], [], [c2, c3], [], False, 0)
     
c1.runChoice()
  