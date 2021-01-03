class Student:
    def __init__(self, s_id, fname, lname):
        self.s_id = s_id
        self.fname = fname
        self.lname = lname
        # self.full_name = "{} {}".format(self.fname, self.lname)

    def full_name(self): #getter in Java
        return "{} {}".format(self.fname, self.lname)

    def email(self):
        return "{}.{}{}@cbs.chula.ac.th".format(self.fname, self.lname[:2], self.join_yy)

    @property
    def full_name2(self): #getter in Java
        return "{} {}".format(self.fname, self.lname)

    @property
    def join_yy(self):
        return self.s_id[:2]

    @property
    def degree(self):
        return self.s_id[2]

    @property
    def seq(self):
        return self.s_id[3:7]

    @property
    def check_digit(self):
        return self.s_id[-3]

    @property
    def school(self):
        return self.s_id[-2:]

if __name__ == '__main__':
    s = Student("5841234526", "Fah", "Puinoon")
    print(s.full_name())
    print(s.full_name2)
    print(s.join_yy)
    print(s.s_id[:2])
    print(s.school)
    print(s.email())
    # s.full_name = "Songkarn Fahsai"
    # print(s.full_name())

