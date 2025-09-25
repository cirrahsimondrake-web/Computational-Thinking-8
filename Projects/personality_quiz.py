extrovert_points = 0
introvert_points = 0
ambivert_points= 0

answer = input("When your at lunch do you A) want to yap to your friends,B) observe and not talk, or C)will talk but not as much?:")
if answer == "A" or answer== "C":
    extrovert_points += 5
elif answer == "B":
    introvert_points += 7
elif answer == "C":
    ambivert_points += 6


answer = input("Would you rather have an A) dog, B) cat, or C) both:")
if answer == "A":
    extrovert_points += 5
elif answer == "B":
    introvert_points +=7
elif answer == "C":
    ambivert_points += 6

answer = input ("When your by yourself do you A) beg your parents to go to a friends house, B) read/dance by yourself, or C)talk to one of your friends while laying down on your bed?")
if answer == "B" and introvert_points > 9:
    introvert_points += 9
elif answer == "A" or answer== "C": 
    extrovert_points += 5
elif answer == "C":
    ambivert_points += 6

answer = input ("If your preforming in front of people would you A) want to be in the spot light, B) be in the back, or C) in the middle")
if answer == "A":
    extrovert_points += 5
elif answer == "B":
    introvert_points += 7
elif answer == "C":
    ambivert_points += 6

answer = input ("during class projects would you A) talk only with your friends, B) only talk when you have to, or C) talk to anybody")
if answer == "A":
    extrovert_points += 5
elif answer == "B":
    introvert_points += 7
elif answer == "C":
    ambivert_points += 6

if extrovert_points > introvert_points and extrovert_points > ambivert_points:
    print ("you are an extrovert!")
elif introvert_points > extrovert_points and introvert_points > ambivert_points:
    print ("you are an Introvert!")
elif ambivert_points > introvert_points and ambivert_points > extrovert_points:
    print ("you are an Ambivert!")
    
