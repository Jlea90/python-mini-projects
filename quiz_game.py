print("Welcome to my silly quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play.")
score = 0

answer = input("What do you call a bear with no teeth? ")
if answer.lower() == "gummy bear":
    print("You got it!")
    score += 1
else:
    print("It is called a gummy bear!") 

answer = input("Why did the student eat his homework? ")
if answer.lower() == "teacher said it was a piece of cake":
    print("you got it!")
    score += 1
else: 
    print("Because the teacher told him it was a piece of cake!")

answer = input("Why don't eggs tell jokes? " )
if answer.lower() == "they crack up":
    print("you got it!")
    score += 1
else: 
    print("Because they crack up!")

answer = input("How do you organize a space party? ")
if answer.lower() == "you planet":
    print("you got it!")
    score += 1
else: 
    print("You planet!")

answer = input("What do you call a dinosaur that is sleeping? " )
if answer.lower() == "dino-snore":
    print("you got it!")
    score += 1
else: 
    print("A dino-snore!")

print("You got " + str(score) + " jokes right!")

if score >= 4:
    print("\nCongrats! You've unlocked the Super Silly Story Challenge!")
    print("In this challenge, you'll help complete a hilarious story by providing some words.\n")

    # Ask for user input to fill in the blanks of the story
    noun1 = input("Enter a noun (plural): ")
    adjective1 = input("Enter an adjective: ")
    verb_past_tense = input("Enter a verb (past tense): ")
    noun2 = input("Enter a noun: ")
    sound_effect = input("Enter a sound effect (like 'Boom' or 'Splash'): ")

    # The story with blanks filled by the user's input
    story = f"""
    Once upon a time, in a land filled with {noun1},
    there was a {adjective1} kingdom where everyone {verb_past_tense} all day long.
    One day, a giant {noun2} appeared, making a loud '{sound_effect}!' noise,
    which scared all the {noun1}. But fear not, for our brave quiz taker saved the day!
    """

    print(story)

    print("What a hilaroius story! Well, this is the end of the Silly Quiz, Bye!")
else:
    print("\nYou did great, but the Super Silly Story Challenge remains locked. Try again to unlock it!")

    print("This is the end of the Silly Quiz! Bye!")