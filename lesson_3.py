# Set the variable in_list to whatever value you want. Let's use 
# [ 5, 2, 3, 1, 4, 6, 8, 7 ] as an example.

# Use for loops, while loops, and whatever else we've learned to 
# set the variable x to the length of in_list - but you may NOT use len! 
# Try to mimic the behavior of len.

in_list = [ 5, 2, 3, 1, 4, 6, 8, 7 ]
x = 0
for i in in_list:
    x += 1
print(str(x))
################################################
# Create a program to accept words from a user, and add them to a dictionary. 
# At the end, use print(mydict) to print out the user's work to them


mydict = {}
while True:
    print("Please enter a word. If you would like to stop hit enter")
    word = input()
    if word == "":
        break
    print("Please enter the corresponding value.")
    value = input()
    if len(word.split()) > 1:
        print("The key cannot contain a space.")
    elif word in mydict:
        print("This key is already in the dictionary.")
    else:
        mydict[word] = value

print(mydict)

print("Please enter a sentence: ")
sentence = input()
sentenceSplit = sentence.split()
timesRan = 0
for item in sentenceSplit:
    if item in mydict:
        sentenceSplit[timesRan] = mydict[item]
    timesRan += 1

print(" ".join(sentenceSplit))

################################################
# Extend your dictionary program from assignment #2 to have some added capabilities:

# Make sure the user cannot enter more than one translation for the same word, 
# in either direction. For example, if ‘dog’: ‘Hund’ is already an entry in the 
# dictionary, then adding a new translation for ‘dog’ OR another word that translates 
# to ‘Hund’ should fail.

# Make sure the user cannot input a key that contains a space, but a value that 
# contains a space is acceptable. So adding ‘the dog’ : ‘Hund’ should fail, but 
# ‘dog’ : ‘der Hund’ is fine.



################################################
# Instead of printing out the dictionary when the program is done, ask the user 
# for a sentence and “translate” it, word-by-word, as output. 

# If a word has no translation, use the word unchanged.
