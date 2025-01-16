import sys,time,random

typing_speed = 101 #wpm
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
  def __init__(self, story, options, nextChoices):
    self.story = story
    self.options = options
    self.nextChoices = nextChoices

  def runChoice(self):
    print("********\n")
    slow_type(self.story)
    print("\n********\n")
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
    
    self.nextChoices[playerChoice].runChoice()
  