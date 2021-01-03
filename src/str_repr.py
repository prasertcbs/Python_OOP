class Medal:
    def __init__(self, country, gold, silver, bronze):
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def total(self):  # instance method
        return self.gold + self.silver + self.bronze

    # def __str__(self): # toString()
    #     return "{:15} g: {:3} s: {:3} b: {:3} t: {:3}".format(self.country, self.gold, self.silver, self.bronze, self.total())

    def __repr__(self):  # string representation
        return "({!r},{},{},{},{})".format(self.country, self.gold, self.silver,
                                           self.bronze, self.total())
        # return "{}{}".format(self.__class__.__name__, repr((self.country, self.gold, self.silver, self.bronze)))


if __name__ == '__main__':
    # th = Medal("Thailand", 5, 6, 10)
    # print(th) -> print(str(th)) -> print(th.__str__()) -> print(th.__repr__())
    # print(th.country, "g", th.gold, "s", th.silver, "b", th.bronze, "t", th.total())
    m = [
        Medal("Thailand", 5, 6, 10),
        Medal("Japan", 15, 20, 10),
        Medal("China", 55, 40, 105)
    ]
    for c in m:
        print(c)
