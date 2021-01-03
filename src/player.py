class Player:
    def __init__(self): # dunder -> double underscores
        self.fname = ""
        self.lname = ""
        self.number = ""


class Player2:
    def __init__(self, fname, lname, number):
        self.fname = fname
        self.lname = lname
        self.number = number

if __name__ == '__main__':

    p1 = Player()
    p1.fname = "Loris"
    p1.lname = "Karius"
    p1.number = 1

    p2 = Player()
    p2.fname = "Alex"
    p2.lname = "Manninger"
    p2.number = 13

    p1a = Player2("Loris", "Karius", 1)
    p2a = Player2("Alex", "Manninger", 13)
    print(p1a.fname)
    print(p2.lname)

    p1t = ("Loris", "Karius", 1)   # tuple
    print(p1t)
    print(p1t[0])

    p1d = {"fname": "Loris", "lname": "Karius", "number": 1}
    print(p1d)
    print(p1d["lname"])




