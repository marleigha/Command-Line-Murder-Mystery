from main import Choice

end1 = Choice("You creep slowly and arrive upon the kitchen. The floor is eerily clean, with the smell of chemicals in the air. Something knocks over and you turn to see a cat on a counter. It’s yowls must have been what you heard. You spend the rest of the night petting the cat till dawn breaks and all your friends, including Theodore find you.\n", [], [])

end2 = Choice("your footsteps echo throughout the creaky hall as you quickly arrive at the scene of the screams. Theordore lays bloodied on the floor of the kitchen. All of a sudden a hooded figure stands before you with a knife! Your loud steps made them aware of your arrival. The road ends here\n", [], [])

end3 = Choice("You turn around and the hallway looks normal. Not a single thing out of place, and it’s too quiet. A pin drops and your vision goes black. Your hands go out looking for your assailant, but your hands find no purchase. Next you feel you losing feeling in your hands. Your fingers tingling cold and then completely numb. Slowly all of your limbs become numb and you begin to lose control. You feel your arms lifting, hands placing themselves on the sides of your head. Your mind is racing, you can’t stop the movement, it’s like you’re possessed. Your fingers dig into your skull, and in a moment you feel them twist and snap your neck.\n", [], [])

end4 = Choice("Your hand touches the metal of the doorknob and luckily it turns. You open it as quickly as you can, barely noticing what’s going to be on the other side. The air feels fresh. You’re outside. You must have found a backdoor to get out of the mansion. Soon your friends tumble outside too– even Theodore!\n", [], [])

end5 = Choice("You follow the cat out of the window, and see it sitting gracefully on the roof. You move to sit next to the cat, letting your legs hang off of the sides. The cat moves to sit in your lap and begins purring. You pet the cat comfortably until the sun rises\n", [], [])

simRejMeanderWalk = Choice("You ignore the odd sensation at the back of your neck, keeping your head directly forward. You make it a few paces forward before you hear just the faintest whisper— why do you ignore me?\n", ["turn around", "run for the closest door"], [end3, end4])

simRejMeanderCatWalk = Choice("You ignore both the cat and the odd sensation at the back of your neck, keeping your head directly forward. You make it a few paces forward before you hear just the faintest whisper— why do you ignore me?\n", ["turn around", "run for the closest door"], [end3, end4])

simRejMeanderTurn = Choice("you turn around and see a window that wasn’t open before. A cat’s head pops up by the window, and quickly disappears\n", ["follow the cat", "disregard the cat and keep walking"], [end5, simRejMeanderCatWalk])

simRejMeander = Choice("You start to walk the hallways of the mansion. You feel a chill wind directly hit the back of your neck. The wind starts to have a twinge of warmth, is that someone’s breath or just a draft?\n", ["turn around", "keep walking"], [simRejMeanderTurn, simRejMeanderWalk ])

opt3 = Choice("You follow the scream as best as you can. You think it came from the left wing of the haunted mansion, so you head there. Another scream is heard, this time more garbled.\n", ["run fast toward the sound", "creep slowly towards the sound"], [end2, end1])

simRej = Choice("You: I don’t know. A little bit of mystery is fun isn’t it?\nSimon: Not when our friend might be in danger. I’m going to look for him. Alone.\n", ["leave him alone, and walk towards the scream", "leave him alone, and meander throughout the halls"], [opt3, simRejMeander])

simResponse = Choice("You approach Simon to talk to him.\nSimon: I told you we shouldn’t have come here.\n", ["gently disagree with him"], [simRej])

start = Choice("You enter a haunted house with your friends, Alvin, Simon, and Theodore. It was on a dare, and you just needed to last the night. Ghosts don’t exist anyways. But as you walk through the front door, it slamming shut behind you with finality, Theodore is no longer by your side. Before you get the chance to ask Simon and Alvin if they’ve seen him, a shriek resounds throughout the room. Theodore’s voice.\n", ["talk to Simon", "try to follow the scream"], [simResponse, opt3])

start.runChoice()