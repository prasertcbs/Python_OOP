class Student:
    def __init__(self, fname, lname, blood):
        self.fname = fname
        self.lname = lname
        self.blood = blood  # A, B, AB, O

    def __str__(self):
        return "{} {}, blood group: {}".format(self.fname, self.lname, self.blood)


class Person:
    def __init__(self, fname, lname, blood):
        self.fname = fname
        self.lname = lname
        # self.blood = blood # A, B, AB, O
        self.setBlood(blood)

    def getBlood(self):
        return self.__blood

    def setBlood(self, blood):
        if blood.upper() in ["A", "B", "AB", "O"]:
            self.__blood = blood.upper()
        else:
            raise ValueError("invalid blood group.")

    def __str__(self):
        return "{} {}, blood group: {}".format(self.fname, self.lname, self.__blood)


if __name__ == '__main__':
    # s1 = Student("Peter", "Parker", "A")
    # s1.blood = "Y"
    # print(s1)

    p1 = Person("Peter", "Parker", "A")
    print(p1)
    p2 = Person("Bruce", "Wayne", "Ab")
    print(p2)
    p2.setBlood("O")
    print(p2)
    p2.__blood = "B"
    print(p2)
    print(p2.__dict__)
    p2._Person__blood = "A"
    print(p2)
    print(p2.getBlood())
