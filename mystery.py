from main import Choice
from main import Player

runner = Player("the runner", "won three highschool track medals", 3, 2, -5, 4, 0, 6)


arr = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']

end1 = Choice(["You creep slowly and arrive upon the kitchen. The floor is eerily clean, with the smell of chemicals in the air. Something knocks over and you turn to see a cat on a counter. It’s yowls must have been what you heard. You spend the rest of the night petting the cat till dawn breaks and all your friends, including Theodore find you.\n      |\      _,,,---,,_\nZZZzz /,`.-'`'    -.  ;-;;,\n"], [], [], [], [], False, 0, '')

end2 = Choice(["your footsteps echo throughout the creaky hall as you quickly arrive at the scene of the screams. Theordore lays bloodied on the floor of the kitchen. All of a sudden a hooded figure stands before you with a knife! Your loud steps made them aware of your arrival. The road ends here\n"], [], [], [], [], False, 0, '')

end3 = Choice(["You turn around and the hallway looks normal. Not a single thing out of place, and it’s too quiet. A pin drops and your vision goes black. Your hands go out looking for your assailant, but your hands find no purchase. Next you feel you losing feeling in your hands. Your fingers tingling cold and then completely numb. Slowly all of your limbs become numb and you begin to lose control. You feel your arms lifting, hands placing themselves on the sides of your head. Your mind is racing, you can’t stop the movement, it’s like you’re possessed. Your fingers dig into your skull, and in a moment you feel them twist and snap your neck.\n"], [], [], [], [], False, 0, '')

end4 = Choice(["Your hand touches the metal of the doorknob and luckily it turns. You open it as quickly as you can, barely noticing what’s going to be on the other side. The air feels fresh. You’re outside. You must have found a backdoor to get out of the mansion. Soon your friends tumble outside too– even Theodore!\n"], [], [], [], [], False, 0, '')

end5 = Choice(["You follow the cat out of the window, and see it sitting gracefully on the roof. You move to sit next to the cat, letting your legs hang off of the sides. The cat moves to sit in your lap and begins purring. You pet the cat comfortably until the sun rises\n"], [], [], [], [], False, 0, '')

simRejMeanderWalk = Choice(["You ignore the odd sensation at the back of your neck, keeping your head directly forward. You make it a few paces forward before you hear just the faintest whisper— why do you ignore me?\n"], ["turn around", "run for the closest door"], [], [end3, end4], [], False, 0, '')

simRejMeanderCatWalk = Choice(["You ignore both the cat and the odd sensation at the back of your neck, keeping your head directly forward. You make it a few paces forward before you hear just the faintest whisper— why do you ignore me?\n"], ["turn around", "run for the closest door"], [], [end3, end4], [], False, 0, '')

simRejMeanderTurn = Choice(["you turn around and see a window that wasn’t open before. A cat’s head pops up by the window, and quickly disappears\n"], ["follow the cat", "disregard the cat and keep walking"], [],  [end5, simRejMeanderCatWalk], [], False, 0, '')

simRejMeander = Choice(["You start to walk the hallways of the mansion. You feel a chill wind directly hit the back of your neck. The wind starts to have a twinge of warmth, is that someone’s breath or just a draft?\n"], ["turn around", "keep walking"], [], [simRejMeanderTurn, simRejMeanderWalk ], [], False, 0, '')

opt3 = Choice(["You follow the scream as best as you can. You think it came from the left wing of the haunted mansion, so you head there. Another scream is heard, this time more garbled.\n"], ["run fast toward the sound", "creep slowly towards the sound"], [], [end2, end1], [], False, 0, '')

simRej = Choice(["You: I don’t know. A little bit of mystery is fun isn’t it?\nSimon: Not when our friend might be in danger. I’m going to look for him. Alone.\n"], ["leave him alone, and walk towards the scream", "leave him alone, and meander throughout the halls"], [], [opt3, simRejMeander], [], False, 0, '')

simAgree = Choice(["You: I know… I shouldn’t have let Alvin force us to come.\nSimon: Exactly! Stay vigilant, if you hear something weird. Run!\nYou: Thanks for the advice, I’ll keep that in mind. Stay safe Simon.\n"], [], [], [], [], False, 0, '')

leftDoor = Choice()

rightOpen = Choice()
rightSneaky = Choice()

controlMonitorsRoll = Choice()
controlJustTheo = Choice()

rightDoor = Choice(["You approach the right door, the sliver of opening revealing that a light is on. A shadow soundlessly crosses the light.\n"], ["fully open the door and go in", "try to be sneaky and enter the room (dexterity check)"], [], [rightOpen, rightSneaky], [],False, 0, '')

lockPickRoll = Choice(["You grab a stray hairpin, and begin the process of lockpicking. A little twist here, and a small jab there, and suddenly... you hear the door click. You're in! You open the door to find a room with multiple monitors around-- each showcasing a room in this vast mansion.", "You grab a stray hairpin and make an attempt at picking the lock. You can't quite get it to work. The movies always make it look so easy. Throughout your struggle, you don't notice the soft footsteps behind you until too late. You call out for your friends, but it's no use. You're face to face with a masked figure. In a flash the figure takes a knife to your throat."], ["look through the cameras to find Theodore", "see if you can control anything"], [], [controlJustTheo, controlMonitorsRoll], [], True, 12, arr[3])

breakDownRoll = Choice()
breakDownRollHard = Choice()

centerDoorHard = Choice(["You cross the hallway to get to the center door, the footsteps on the ground seem larger, almost too large to be human. You go to open the door, but it’s locked.\n"], ["try to pick the lock (dexterity check)", "try, with the help of simon, to break the door down (strength check)"],[], [lockPickRoll, breakDownRollHard], [], False, 0, '')

centerDoorEasy = Choice(["You cross the hallway to get to the center door, the footsteps on the ground seem larger, almost too large to be human. You go to open the door, but it’s locked.\n"], ["try to pick the lock (dexterity check)", "try, with the help of simon, to break the door down (strength check)"],[], [lockPickRoll, breakDownRoll], [], False, 0, '')

soloStairs = Choice(["You begin your solo ascent up the stairs. There are three doors in the hallway. You think you hear water running behind the door to your left. Maybe that’s the bathroom. The door to your right is slightly ajar. Lastly, The door directly in front of you, at the end of the hall, has a series of footsteps leading to it.\n"], ["go to the left door", "go to the door to the right", "go to the door at the end of the hall"], [], [leftDoor, rightDoor, centerDoorHard], [], False, 0, '')

simStairs = Choice(["You and Simon begin the ascent up the stairs. There are three doors in the hallway. You think you hear water running behind the door to your left. Maybe that’s the bathroom. The door to your right is slightly ajar. Lastly, The door directly in front of you, at the end of the hall, has a series of footsteps leading to it.\n"], ["go to the left door", "go to the door to the right", "go to the door at the end of the hall"], [], [leftDoor, rightDoor, centerDoorEasy], [], False, 0, '')

simConvince = Choice(["You: Hey, it's never a good idea to split up in a situation like this. Let's stay together and watch each other's backs\nSimon: Solid plan, wherever you think we should go, I'll follow.\n", "You: uhhh hey, we could, i don't know. uh. we shouldn't split up\nSimon: Don't worry, you'll be fine. We'll cover more ground if we stay split up\n"], ["go with Simon up the stairs", "go with Simon towards the living room"],["head towards the hallway", "head towards where you heard the scream", "head up the stairs"], [], [simRejMeander,opt3, soloStairs], True, 10, arr[5])

simResponse = Choice(["You approach Simon to talk to him.\nSimon: I told you we shouldn’t have come here.\n"], ["gently disagree with him", "agree with him", "convince him to stay together (charisma roll)"], [], [simRej, simAgree, simConvince ], [], False, 0, '')

start = Choice(["You enter a haunted house with your friends, Alvin, Simon, and Theodore. It was on a dare, and you just needed to last the night. Ghosts don’t exist anyways. But as you walk through the front door, it slamming shut behind you with finality, Theodore is no longer by your side. Before you get the chance to ask Simon and Alvin if they’ve seen him, a shriek resounds throughout the room. Theodore’s voice.\n"], ["talk to Simon", "try to follow the scream"], [], [simResponse, opt3], [], False, 0, '')

start.player_stats(runner)
start.runChoice()