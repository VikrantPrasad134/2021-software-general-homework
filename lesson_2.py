# A student has taken 3 tests in a class, and wants to know their current grade 
# (which is only calculated by these tests). 

# Ask the user to input all three of the test scores for the student, one by one. 

# The program should then calculate the average test score (average is adding all three 
# test scores together then dividing by 3), and then print the student's letter grade 
# (as well as the average score as a number).

print("Please enter test 1: ")
test1 = input()
print("Please enter test 2: ")
test2 = input()
print("Please enter test 3: ")
test3 = input()
test1 = int(test1)
test2 = int(test2)
test3 = int(test3)
average = (test1 + test2 + test3) / 3
print("The average score of the student's 3 tests is " + str(average))
if average >= 90:
    print("This students scores average out to an A.")
elif average >= 80:
    print("This students scores average out to an B.")
elif average >= 70:
    print("This students scores average out to an C.")
elif average >= 60:
    print("This students scores average out to an D.")
else:
    print("This students scores average out to an F.")

#########################################################

# Gregory wants to know how many toys they can buy at Toys'N'Us

# They prioritize buying the most expensive toys first (For ejm. If Gregory had $50 
# they'd end up buying 2 Jumbo Baby Yoda Plushies, 1 Beyblade, and 5 Sticky Hands with 
# a remainder of $0.30 left)

# Have the user input how much money Gregory has then print how many of each 
# toy they can afford, as well as how much money they'd have remaining

print("Please enter how much money Gregory has.")
money = input()
money = int(money)
originalMoney = money
plushies = 0
beyblades = 0
stickyHands = 0
while money >= 20:
    money -= 20
    plushies += 1
while money >= 7.2:
    money -= 7.2
    beyblades += 1
while money >= 0.5:
    money -= 0.5
    stickyHands += 1
print("Gregory can buy " + str(plushies) + " baby yoda plushies, " + str(beyblades) + " beyblades and " + str(stickyHands) + " sticky hands.")
print("Gregory has $" + str(money) + " remaining.")

#Jumbo BabyYoda Plush - $20
#Beyblades - $7.20
#Sticky hands - $0.50