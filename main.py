
print("You hear abou a zombie apocalypse on the news.")
c1=input("Would you like to: \n\na) ignore the warnings \nb) drive out to your private island on a private jet \nc) seek safety in a bomb shelter\n\nAnswer: ")
if c1 == "a" or c1 == "A":
  print(" Despite the warnings on the news, you head to work on your usual schedule. On the bus, somebody starts coughing blood and his veins are turning purple. He struggles for a moment then his eyes turn cold. Nobody leaves the bus alive, including you.\n\nYou have died.")
  exit()
if c1 == "b" or c1 == "B":
  print("\nYou leave the house in a hurry, and take an uber to the airport. You board your private jet and give the pilot directions.\n\n")
  c2 = input("Oh no! During your trip, your private jet suddenly starts rocking. \na) go to sleep; you trust the pilot to be able to navigate through these winds\nb) jump off the plane. You have heard how amazing parachuting can be with the right wind\nc) something is fishy here. go to the pilot to see what the problem is.\n\nAnswer: ")
  if c2 == "a" or c2 == "A":
    print("\nYou fall asleep quickly but wake up when the jet starts to fall. You rush to the window and see that you are dropping fast. You run towards the pilot but his veins are purple and his cold hands reach desperately for you. \n\nyou have died.")
    exit()
  if c2 == "b" or c2 == "B":
    print("\nYou prepare yourself for the jump but fall off when the jet wobbles. You are speeding down and think that now would be a great time to pull out the parachute. You then realise you forgot to bring one.\n\nyou have died.")
    exit()
  if c2 == "c" or c2 == "C":
    print("\nYou head to the pilots room and discover that he is infected! You do not have much time to decide what to do, as he is running towards you. ")
    c3 = input("Would you like to do: \na) try taking him down with a random pen you have in your pocket\nb) jump off the jet\nc) try pushing him off the jet\n\nAnswer: ")
    if c3 == "a" or c3 == "A":
      print("You ready yourself as the zombie comes at you, trying to remember the combat training you have had in the past. \n You abandon the pen and you kick him repeatedly until he falls apart. \nSuddenly the jet turns upside down and the side door opens and everything falls out, but you hold onto a handle. You climb up through the space to the pilot seat, even though you do not know how to pilot a jet ")
      c4 = input("\nWould you like to:\na) press the green button on the left\nb) press the red button on the right\nc) turn the knob above the control wheel\n\nAnswer: ")
      if c4 == "a" or c4 == "A":
        print("You press the green button on the left. It des nothing. Sadly, you plummet to your death.\n\nyou have died.")
        exit()
      if c4 == "b" or c4 == "B":
        print("You press the red button on the right. A speaker starts to speak:\n\n    'Self-detruction has been activated'\n      '10...9...8...'")
        c5 = input("Quick! You have barely anytime before the jet self-destructs. \n\nWoud you like to:\na) try and figure out how to stop it\nb) accept your inevitable death\nc) jump out of the plane\n\nAnswer: ")
        if c5 == "a" or c5 == "A":
          print("you search the control panel for a back button, whoch is how your final seconds are spent. The jet explodes\n\nyou have died.")
          exit()
        if c5 == "b" or c5 == "B":
          print("you decide to spend the final seconds of your life happily. You pull out your phone and start watching Brooklyn 99. Thejet explodes.\n\nyou have died.")
          exit()
        if c5 == "c" or c5 == "C":
          print("You decide that you have no option but to jump out of the plane. You wait until you are close to the water, and jump. You now have to somehow get to your island...")
          c6 = input("\nWould you like to:\na) go back to the sinking plane and see if there is anything useful\nb) try to swim to your island\nc) try to find a dolphin that will help you get to your island\n\nAnswer: ")
          if c6 == "a" or c6 == "A":
            print("You swim to the jet and find the door has broken off. You sit on it and start paddling your way to your island with another piece of plane. \nOh no! There is something circling underneath you!")
            c7 = input("Would you like to:\na) toss down a piece of muesli bar into the water\nb)paddle away as fast as you can\nc) try to scare it by cannon-balling into the water\n\nAnswer: ")
            if c7 == "b" or c7 =="B":
              print("You try paddling away from the sea-creature, but unfortunately it wants to eat you. The last thing you see is the pale bue sky.\n\nyou have died.")
              exit()
            if c7 == "c" or c7 == "C":
              print("You cannon-ball into the water, trying to scare the sea-creature, but unfortunately it decides to eat you.\n\nyou have died.")
              exit()
          if c6 == "b" or c6 == "B" or c6 == "c" or c6 == "C" or c7 == "a" or c7 == "A":
            print("The dolphin has deemed you worthy of it's friendship! It's name is Finn and it agrees to help you get to your island. \n You ride on the waves for 10 minutes unil you finally get there. You say bye to Finn and turn around face-to-face with a growling black panther.")
            c8 = input("Would you like to:\n a) jump back into the water\n b) say hello\n c) freeze until it walks away\n\Answer: ")
            if c8 == "a" or c8 == "A":
              print("You jump back into the water, but the panther doesn't care. Frustated that you tried to run away, it bites you and leaves you bleeding in th water.\n\nyou have died.")
              exit()
            if c8 == "c" or c8 == "C":
              print("You try freezing until it walks away, but the panther is offended that you think it is that dumb. It bites you and leaves you bleeding on the ground.\n\nyou have died.")
              exit()
            if c8 == "b" or c8 =="B":
              print("You attempt saying hello. However, the panther does not understand you, as he is beyond communicating through words. He ends up biting you, and leaves you bleeding on the ground before you can explain that this is your island.\n\nyou have died.")
              exit()
      if c4 == "c" or c4 == "C":
        print("You turn the knob above the control wheel. The speakers start to speak:\n\n        'Auto-pilot activted.'\n\nYou sigh in relief as the jet steadies itself.")
    if c3 == "b" or "B":
      print("You back off and jump off the jet, landing flat on the ocean.\n\nyou have died.")
      exit()
    if c3 == "c" or c3 == "C":
      print("You grb his arm, but you end up fainting because of his terrible smell, and he eats you.\n\nyou have died.")
      exit()



if c1 == "c" or c1 == "C":