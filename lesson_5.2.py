'''
class Animal:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    def increaseAge(self):
        self.age += 1
class Dog(Animal):
    def __init__(self, age, name, breed):
        super().__init__(age, name)
    def __repr__(self):
        return "dog" + self.name
pet = Dog(5, "Coco","poodle")
print(str(pet.age))
pet.increaseAge()
print(str(pet.age))
print(pet)
'''
class Base():
    def __init__(self, x, y, name, color):
        self.x = x
        self.y = y
        self.name = name
        self.color = color
    def returnLocation(self):
        return(self.x + str(self.y))
class Pawn(Base):
    def __init__(self, x, y, name, color):
        super().__init__(x, y, name, color)
class Bishop(Base):
    def __init__(self, x, y, name, color):
        super().__init__(x, y, name, color)
class Knight(Base):
    def __init__(self, x, y, name, color):
        super().__init__(x, y, name, color)
class Rook(Base):
    def __init__(self, x, y, name, color):
        super().__init__(x, y, name, color)
class Queen(Base):
    def __init__(self, x, y, name, color):
        super().__init__(x, y, name, color)
class King(Base):
    def __init__(self, x, y, name, color):
        super().__init__(x, y, name, color)

def createPawn(x, y, color, class_name):
    class_name = Pawn(x, y, "pawn", color)
    print(class_name.returnLocation())
def createBishop(x, y, color, class_name):
    class_name = Bishop(x, y, "bishop", color)
    print(class_name.returnLocation())
def createKnight(x, y, color, class_name):
    class_name = Knight(x, y, "knight", color)
    print(class_name.returnLocation())
def createRook(x, y, color, class_name):
    class_name = Rook(x, y, "rook", color)
    print(class_name.returnLocation())
def createQueen(x, y, color, class_name):
    class_name = Queen(x, y, "queen", color)
    print(class_name.returnLocation())
def createKing(x, y, color, class_name):
    class_name = King(x, y, "king", color)
    print(class_name.returnLocation())


createPawn("A", 2, "white", "WhitePawn1")
createPawn("B", 2, "white", "WhitePawn2")
createPawn("C", 2, "white", "WhitePawn3")
createPawn("D", 2, "white", "WhitePawn4")
createPawn("E", 2, "white", "WhitePawn5")
createPawn("F", 2, "white", "WhitePawn6")
createPawn("G", 2, "white", "WhitePawn7")
createPawn("H", 2, "white", "WhitePawn8")

createBishop("C", 1, "White", "WhiteBishop1")
createBishop("F", 2, "White", "WhiteBishop2")
