class Choice:
  def __init__(self, name, text, nextChoices):
    self.name = name
    self.text = text
    self.nextChoices = nextChoices

  def runChoice(self):
    print("**", self.text, "**")
    playerChoice = int(input("what do you choose: ")) -1
    #check and make sure the choice is an int, and in range of next choices
    # if playerChoice not in range(len(self.nextChoices)):
    # 	print("not very good input")
    print(self.nextChoices[playerChoice].text)
    #self.nextChoices[playerChoice].runChoice()
        
c2 = Choice('c2', "Mystery is solved! Someone's cat is loose", [])
c3 = Choice('c3', "Dude. rip you.", [c2])
c1 = Choice('c1', "You are in a haunted mansion!\n 1. Solve the mystery!\n 2. Wait and let the killer get you", [c2, c3])

c1.runChoice()