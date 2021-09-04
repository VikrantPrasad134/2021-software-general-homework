# Create a program in which the user creates 
# a specific FRC team and store the following variables:
	# Team Number (named team_number)
	# Team Name (named team_name)
	# Location (named location)
	# Rookie Year (named rookie_year)
	# Is Active (named is_active)
# Be sure to store each variable as the correct type!

team_number = 1956
team_name = "Robo Ticks"
location = "Davis, California"
rookie_year = 2014
is_active = False

print("The team number is " + str(team_number))
print("The team name is " + team_name)
print("The team location is " + location)
print("The teams rookie year was " + str(rookie_year))
if is_active == True:
	print("The team is active.")
else:
	print("The team is inactive.")

if is_active == True:
	print(team_name + ", an FRC team in " + location + ", has been an active team since " + str(rookie_year) + ".")
else:
	print(team_name + ", an FRC team in " + location + ", had its rookie year in " + str(rookie_year) + ", but currently the team is inactive.")

mydict = {"hello": "bye"}
print(mydict["hello"])
