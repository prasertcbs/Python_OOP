def demo_tuple():
    p12 = "Joe", "Gomez", 12
    print(p12)
    print(p12[1])

def demo_dict():
    p12 = {"fname": "Joe", "lname": "Gomez", "number": 12}
    print(p12)
    print(p12["lname"])

class Player:
    pass

class Player2:
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.number = 0

class Player3:
    def __init__(self, fname, lname, number):
        self.fname = fname
        self.lname = lname
        self.number = number

def demo_simple_player_class():
    p12 = Player()  # p12 -> instance
    p12.fname = "Joe"  # attribute/property
    p12.lname = "Gomez"
    p12.number = 12
    print(p12.lname)

def demo_simple_player2_class():
    p12 = Player2()
    p12.fname = "Joe"
    p12.lname = "Gomez"
    p12.number = 12
    print(p12.lname)

def demo_simple_player3_class():
    p12 = Player3("Joe", "Gomez", 12)
    print(p12.lname)

if __name__ == '__main__':
    # demo_tuple()
    # demo_dict()
    # demo_simple_player_class()
    demo_simple_player3_class()