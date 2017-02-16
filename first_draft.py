print """
    Welcome to my quiz!\n
    """

name = raw_input("What is your name? ")
print "\n\nHello, %s!" % (name) + "\n"

print "Today we are going to determine your personality type and the best type of exercise for you.\n"
print "You will be asked questions surrounding the following personality traits:\n"
print "\t ACHIEVEMENT, STRESS MANAGEMENT, SELF ESTEEM, SEARCH FOR MEANING, MOOD AND TENSION, and PLAYFULNESS\n"
print "Answer each question by typing YES, NO, or IN BETWEEN after the question.\n"
print "Once you have answered all the questions, we will show you which personality traits have the highest scores.\n"
print "The area with your highest score is your personality match and motivator for exercise.\n\n\n"

begin_prompt = raw_input("ARE YOU READY TO BEGIN? ")
if (begin_prompt == "yes"):
    print "\nOk %s! Lets get started.\n\n\n" % (name)
elif (begin_prompt == "no"):
    print "Too bad %s! You have gone too far to turn around!" % (name)
else:
    print "I did not understand your answer. I asked if you were ready to begin the quiz."


#starting first section here#
print """
    ***Part One: ACHIEVEMENT***
    """
print "The following statements should be answered by typing YES, NO or IN BETWEEN\n" #i want this to count regardless of cap or lowercase

total_ach = 0
statements = ["1) I like setting challenging goals and trying to achieve them. ", "2) I challenge myself to do better in all areas of my life. ", "3) I work best when I set tough yet realistic expectations for myself. ", "4) I believe I need to set clear goals to have a successful life. ", "5) I don't believe in the concept of failure. "]

for statement in statements:
    s1 = raw_input(statement)
    if (s1 == "yes"):
        total_ach += 2
    elif (s1 == "in between"):
        total_ach += 1
    else:
        total_ach +=0 

# print total_ach # may not want to include this here
print "\n\n\nThat concludes the first section. Five more to go. Let's continue.\n\n\n"


#starting second section here#
print """
    ***Part Two: STRESS MANAGEMENT***
    """
print "The following statements should be answered by typing YES, NO or IN BETWEEN\n" #i want this to count regardless of cap or lowercase

total_stress = 0
statements = ["1) My work is very stressful. ", "2) There have been a lot of challenges in my life in the past 12 months. ", "3) My life rarely feels even and relaxed. ", "4) I have to cope with a lof of pressure on a daily basis. ", "5) In the past year I have felt 'burned out' by stress. "]

for statement in statements:
    s1 = raw_input(statement)
    if (s1 == "yes"):
        total_stress += 2
    elif (s1 == "in between"):
        total_stress += 1
    else:
        total_stress +=0         

# print total_stress # may not want to include this here
print "\n\n\nThat concludes the second section. Four more to go. Let's continue.\n\n\n"


#starting third section here#
print """
    ***Part Three: SELF ESTEEM***
    """
print "The following statements should be answered by typing YES, NO or IN BETWEEN\n" #i want this to count regardless of cap or lowercase

total_esteem = 0
statements = ["1) When I compare myself to others, I get the feeling they are somehow better than I am. ", "2) I get upset with myself when I make mistakes. ", "3) I have a hard time accepting myself as I am. ", "4) If I could be anyone in the world, I would choose to be someone other than myself. ", "5) I don't seem to say or do very much that is worthwhile. "]

for statement in statements:
    s1 = raw_input(statement)
    if (s1 == "yes"):
        total_esteem += 2
    elif (s1 == "in between"):
        total_esteem += 1
    else:
        total_esteem +=0         

# print total_esteem # may not want to include this here
print "\n\n\nThat concludes the third section. Three more to go. Let's continue.\n\n\n"


#starting fourth section here#
print """
    ***Part Four: SEARCH FOR MEANING***
    """
print "The following statements should be answered by typing YES, NO or IN BETWEEN\n" #i want this to count regardless of cap or lowercase

total_search = 0
statements = ["1) I feel something important is missing in my life. ", "2) I often wonder what my life is all about. ", "3) When I take time to reflect, I feel troubled by the shallowness of my lifestyle. ", "4) There seems to be a deeper purpose to life that I have difficulty connecting to. ", "5) I sometimes fear that as my life is ending I will realize I have completely missed the point. "]

for statement in statements:
    s1 = raw_input(statement)
    if (s1 == "yes"):
        total_search += 2
    elif (s1 == "in between"):
        total_search += 1
    else:
        total_search +=0         

# print total_search # may not want to include this here
print "\n\n\nThat concludes the fourth section. Two more to go. Let's continue.\n\n\n"


#starting fifth section here#
print """
    ***Part Five: MOOD AND TENSION***
    """
print "The following statements should be answered by typing YES, NO or IN BETWEEN\n" #i want this to count regardless of cap or lowercase

total_mood = 0
statements = ["1) I am an anxious person. ", "2) I suffer from feeling blue or depressed. ", "3) My body feels tense a lot of the time. ", "4) People who know me think I am a moody person. ", "5) I worry a lot. "]

for statement in statements:
    s1 = raw_input(statement)
    if (s1 == "yes"):
        total_mood += 2
    elif (s1 == "in between"):
        total_mood += 1
    else:
        total_mood +=0         

# print total_mood # may not want to include this here
print "\n\n\nThat concludes the fifth section. One more to go. Let's continue.\n\n\n"

#starting sixth section here#
print """
    ***Part Six: PLAYFULNESS***
    """
print "The following statements should be answered by typing YES, NO or IN BETWEEN\n" #i want this to count regardless of cap or lowercase

total_play = 0
statements = ["1) I consider myself to be a playful person. ", "2) People tell me I am fun to be around. ", "3) I like to play games and sports just for the fun of it. ", "4) My sense of humor is one of my most valued assets. ", "5) I have an easy time getting into a playful spirit. "]

for statement in statements:
    s1 = raw_input(statement)
    if (s1 == "yes"):
        total_play += 2
    elif (s1 == "in between"):
        total_play += 1
    else:
        total_play +=0         

# print total_play # may not want to include this here
print "\n\n\nThat concludes the last section!\n\n\n"

#onto results section
print "Time for the results!\n\n\n"

#this is where I get stuck--i want to not only evaluate the highest value among the list, but to display the variable name associated with it.
#for example, if "total_play" has the highest number value, I want a certain thing to happen
#this "thing" will be for python to print out the results associated with that variable
print max(total_ach, total_stress, total_esteem, total_search, total_mood, total_play)