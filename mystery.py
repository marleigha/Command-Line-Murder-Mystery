from main import Choice

end1 = Choice("You creep slowly and arrive upon the kitchen. The floor is eerily clean, with the smell of chemicals in the air. Something knocks over and you turn to see a cat on a counter. It’s yowls must have been what you heard. You spend the rest of the night petting the cat till dawn breaks and all your friends, including Theodore find you.\n", [], [], False)

end2 = Choice("your footsteps echo throughout the creaky hall as you quickly arrive at the scene of the screams. Theordore lays bloodied on the floor of the kitchen. All of a sudden a hooded figure stands before you with a knife! Your loud steps made them aware of your arrival. The road ends here\n", [], [], False)

opt3 = Choice("You follow the scream as best as you can. You think it came from the left wing of the haunted mansion, so you head there. Another scream is heard, this time more garbled.\n", ["run fast toward the sound", "creep slowly towards the sound"], [end2, end1], False)

start = Choice("You enter a haunted house with your friends, Alvin, Simon, and Theodore. It was on a dare, and you just needed to last the night. Ghosts don’t exist anyways. But as you walk through the front door, it slamming shut behind you with finality, Theodore is no longer by your side. Before you get the chance to ask Simon and Alvin if they’ve seen him, a shriek resounds throughout the room. Theodore’s voice.", ["try to follow the scream\n"], [opt3], False)

start.runChoice()