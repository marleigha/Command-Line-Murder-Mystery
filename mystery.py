from main import Choice
from main import Player

runner = Player(0, 0, 0, 0, 0, 0)


arr = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']

end1 = Choice(["You creep slowly and arrive upon the kitchen. The floor is eerily clean, with the smell of chemicals in the air. Something knocks over and you turn to see a cat on a counter. It’s yowls must have been what you heard. You spend the rest of the night petting the cat till dawn breaks and all your friends, including Theodore find you.\n"], [], [], [], [], False, 0, '')

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

simAgree = Choice(["You: I know… I shouldn’t have let Alvin force us to come.\nSimon: Exactly! Stay vigilant, if you hear something weird. Run!\nYou: Thanks for the advice, I’ll keep that in mind. Stay safe Simon.\n"], ["leave him alone, and walk towards the scream", "leave him alone, and meander throughout the halls"], [], [opt3, simRejMeander], [], False, 0, '')

poolConSave = Choice(["ou make it out of the pool and look back in. A cat is swimming in the pool and eating a fish. You spend the rest of the night feeding the cat.\n", "You struggle to breathe and flail around frantically. Your lungs burn as you start to inhale water and then everything goes black.\n"], [], [], [], [], True, 10, arr[2])

poolJump = Choice(["You jump into the pool to investigate the streaks, but you can't make anything else out in the water. You can't even see the bottom of the pool. Suddenly, you feel something strong pulling on your leg, and you slip under the water.\n"], ["try to swim as hard as you can (constitution check)"], [], [poolConSave], [], False, 0, '')

poolFall = Choice(["You slip on some water as you approach the pool closet. Flailing your arms, you fall and hit your head.\n"], [], [], [], [],False, 0, '')

leftDoor = Choice(["You cautiously approach the door and peek your head in. A large swimming pool fills the room. You spot strange streaks of red floating in the water and hear a splashing noise.\n"], ["Go into the pool to investigate the red streaks", "Explore the surroundings around the pool"], [], [poolJump, poolFall], [], False, 0, '')

controlMonitorsRoll = Choice(["You figure out how the system works. This whole mansion is filled with trap doors, false walls, and is all being controlled from here. With a few simple tests, you figure out how to turn out specific lights, play audio into rooms, to lock doors, and make walls appear. You see the shadowy figure passing through a secret passageway and time everything just right to trap them in place. From there you find your friends on the monitors and manage to speak to them. You unlock the front door and give them directions on how to get out. You’re all safe and together again\n", "You can’t quite figure out how the system works. There are too many options and possibilities. You think you might have finally figured it out when the power shuts off. The room is pitch black, until a single monitor lights up again. Staring directly at you is a masked figure. They know you’re here. They will find you, and they will kill you."], [], [], [], [], True, 10, arr[3])

controlJustTheo = Choice(["You spot Theodore on a couch in the living room! Asleep? Behind you there’s a cork board, with a map of the mansion showcasing secret passages throughout the mansion. You follow it as best as you can, and luckily find Theodore! You wake him up, relieved to find your friend. Soon all your friends are reunited, and you wait in the living room till the morning.\n"], [], [], [], [], False, 0, '')

rightOpen = Choice(["You enter the room, just wanting to find your friend. You scan the room but don’t see Theodore. What you do see is a lamp start to rattle, and then levitate? Soon everything in the room begins to defy gravity– even you. You feel almost like there’s an invisible force holding you up, raising you. Your body reaches the top of the ceiling, being pressed against it. The press begins to feel more intense. You wouldn’t even be able to describe it as a press, it’s crushing. Your bones can’t handle this kind of pressure. You feel the snap of your ribs, the squeeze in your lungs, and the collapse of your heart.\n"], [], [],[],[],False, 0, '')

supriseTheo = Choice(["You sneak up to Theodore and tap him on the shoulder. There’s no response. “Theodore?” Walking in front of the couch, you observe him more closely. Part of his skull has been dented in. There are shards of bones and splatters of blood around the middle of a crater in his forehead. Screaming, you trip backwards over your own feet. The last thing you see is Theodore’s face frozen in a rictus grin.\n"], [], [], [], [], False, 0, '')

creak = Choice(["You walk over to the curtains and peel them aside. The killer jumps out and stabs you, making you shriek. It sounds eerily similar to the one you heard when Theodore disappeared.\n"], [], [], [], [], False, 0, '')
run = Choice(["You glance over at Theodore in a shared look of fright before backing away slowly. Reaching the stairs, you both run back to the entry hall and decide to stay there for the rest of the night.\n"], [], [], [], [], False, 0, '' )

askTheo = Choice(["You: Theodore! What happened? You just disappeared! \nTheodore: I told you earlier that I wanted to explore on my own. I didn’t disappear… \nYou: What about the scream? \nTheodore: Huh? What scream? \n\nA creak behind the curtains interrupts your conversation."], ["investigate the creak", "run away"], [], [creak, run], [], False, 0, '')

rightSneaky = Choice(["You're incredibly careful as you enter the room. You see the back of a figure sitting on a couch by the window. Wait, you recognize that baseball cap! It’s Theodore!\n", "You make your best attempt to be sneaky, but as you push the door it makes the loudest creak. Uh oh. The sound resounds throughout the room and echoes down the hallway. You quickly hear footsteps, thump, thump, thumping. Before you know it the killer is before you with a baseball bat. One quick hit to the head and you're out\n"], ["ask Theodore what happened", "suprise Theodore"], [], [askTheo, supriseTheo], [], True, 12, arr[1])

rightDoor = Choice(["You approach the right door, the sliver of opening revealing that a light is on. A shadow soundlessly crosses the light.\n"], ["fully open the door and go in", "try to be sneaky and enter the room (dexterity check)"], [], [rightOpen, rightSneaky], [],False, 0, '')

lockPickRoll = Choice(["You grab a stray hairpin, and begin the process of lockpicking. A little twist here, and a small jab there, and suddenly... you hear the door click. You're in! You open the door to find a room with multiple monitors around-- each showcasing a room in this vast mansion.\n", "You grab a stray hairpin and make an attempt at picking the lock. You can't quite get it to work. The movies always make it look so easy. Throughout your struggle, you don't notice the soft footsteps behind you until too late. You call out for your friends, but it's no use. You're face to face with a masked figure. In a flash the figure takes a knife to your throat.\n"], ["look through the cameras to find Theodore", "see if you can control anything (intelligence check)"], [], [controlJustTheo, controlMonitorsRoll], [], True, 12, arr[1])

breakDownRoll = Choice(["You and Simon work together to break down the door. Heave, ho, heave, ho! With a glorious flourish the door comes crashing down. You're in! You open the door to find a room with multiple monitors around-- each showcasing a room in this vast mansion.\n", "You and Simon try to work together to get the door knocked down. Either it's incredibly reinforced, or you guys need to hit the gym. You're not one to give up, so you keep trying. The thuds from hitting the door over and over mask the sound of gentle footsteps behind you. Even if you noticed them, it would be too late. You look to Simon for help but it's no use. You're face to face with a masked figure. In a flash the figure takes a knife to your throat.\n"], ["look through the cameras to find Theodore", "see if you can control anything (intelligence check)"], [], [controlJustTheo, controlMonitorsRoll], [], True, 7, arr[0])

breakDownRollHard = Choice(["You know how to manage your strength, and with one smooth kick, you knock the door in. With a glorious flourish the door comes crashing down. You're in! You open the door to find a room with multiple monitors around-- each showcasing a room in this vast mansion.\n", "You try to work to get the door knocked down. Either it's incredibly reinforced, or you need to hit the gym. You're not one to give up, so you keep trying. The thuds from hitting the door over and over mask the sound of gentle footsteps behind you. Even if you noticed them, it would be too late. You call to your friends for help but it's no use. You're face to face with a masked figure. In a flash the figure takes a knife to your throat.\n"], ["look through the cameras to find Theodore", "see if you can control anything (intelligence check)"], [], [controlJustTheo, controlMonitorsRoll], [], True, 15, arr[0])

centerDoorHard = Choice(["You cross the hallway to get to the center door, the footsteps on the ground seem larger, almost too large to be human. You go to open the door, but it’s locked.\n"], ["try to pick the lock (dexterity check)", "try, with the help of simon, to break the door down (strength check)"],[], [lockPickRoll, breakDownRollHard], [], False, 0, '')

centerDoorEasy = Choice(["You cross the hallway to get to the center door, the footsteps on the ground seem larger, almost too large to be human. You go to open the door, but it’s locked.\n"], ["try to pick the lock (dexterity check)", "try, with the help of simon, to break the door down (strength check)"],[], [lockPickRoll, breakDownRoll], [], False, 0, '')

soloStairs = Choice(["You begin your solo ascent up the stairs. There are three doors in the hallway. You think you hear water running behind the door to your left. Maybe that’s the bathroom. The door to your right is slightly ajar. Lastly, The door directly in front of you, at the end of the hall, has a series of footsteps leading to it.\n"], ["go to the left door", "go to the door to the right", "go to the door at the end of the hall"], [], [leftDoor, rightDoor, centerDoorHard], [], False, 0, '')

simStairs = Choice(["You and Simon begin the ascent up the stairs. There are three doors in the hallway. You think you hear water running behind the door to your left. Maybe that’s the bathroom. The door to your right is slightly ajar. Lastly, The door directly in front of you, at the end of the hall, has a series of footsteps leading to it.\n"], ["go to the left door", "go to the door to the right", "go to the door at the end of the hall"], [], [leftDoor, rightDoor, centerDoorEasy], [], False, 0, '')

simConvince = Choice(["You: Hey, it's never a good idea to split up in a situation like this. Let's stay together and watch each other's backs\nSimon: Solid plan, wherever you think we should go, I'll follow.\n", "You: uhhh hey, we could, i don't know. uh. we shouldn't split up\nSimon: Don't worry, you'll be fine. We'll cover more ground if we stay split up\n"], ["go with Simon up the stairs"],["head towards the hallway", "head towards where you heard the scream", "head up the stairs"], [simStairs], [simRejMeander,opt3, soloStairs], True, 10, arr[5])

simResponse = Choice(["You approach Simon to talk to him.\nSimon: I told you we shouldn’t have come here.\n"], ["gently disagree with him", "agree with him", "convince him to stay together (charisma roll)"], [], [simRej, simAgree, simConvince ], [], False, 0, '')

start = Choice(["You enter a haunted house with your friends, Alvin, Simon, and Theodore. It was on a dare, and you just needed to last the night. Ghosts don’t exist anyways. But as you walk through the front door, it slamming shut behind you with finality, Theodore is no longer by your side. Before you get the chance to ask Simon and Alvin if they’ve seen him, a shriek resounds throughout the room. Theodore’s voice.\n"], ["talk to Simon", "try to follow the scream"], [], [simResponse, opt3], [], False, 0, '')

runner.build_player()
runner.display_stats()

start.player_stats(runner)
start.runChoice()