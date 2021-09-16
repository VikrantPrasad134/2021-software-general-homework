class robot:
    def __init__(self, position, armPosition, cube, score):
        self.position = position
        self.armPosition = armPosition
        self.cube = cube
        self.score = score
    
    def change_position(self, x):
        self.position += x
    def change_armPosition(self, x):
        if self.armPosition + x >= 0:
            self.armPosition += x
    def pickUpCube(self):
        if self.position >= 3:
            if self.armPosition == 0:
                if self.cube == False:
                    self.cube = True
    def scoreCube(self):
        if self.position == 7:
            if self.armPosition == 10:
                self.score += 1


robo1 = robot(0,0,False,0)

while True:
    print("robot position = " + str(robo1.position) + ", arm position = " + str(robo1.armPosition) + ", cube pickup = " + str(robo1.cube) + ", score = " + str(robo1.score))
    choice = input("What would you like to do? 1 = move robot, 2 = move arm, 3 = pick up a cube, 4 = score, 5 = end")
    if choice == "1":
        robotMovement = input("Would you like to move forward or backward?")
        if robotMovement == "forward":
            robo1.change_position(1)
        elif robotMovement == "backward":
            robo1.change_position(-1)
    elif choice == "2":
        print("How many inches would you like to move your arm? (use negative for backwards)")
        inches = input()
        robo1.change_armPosition(inches)
    elif choice == "3":
        robo1.pickUpCube()
    elif choice == "4":
        robo1.scoreCube()
    elif choice == "5":
        break
    else:
        print("test")
print("test")





     
        
        
