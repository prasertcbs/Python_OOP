class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return "{} {}".format(self.fname, self.lname)

class Student(Person):
    def __init__(self, s_id, fname, lname):
        super().__init__(fname, lname)
        self.s_id = s_id

        # self.s_id = s_id
        # self.fname = fname
        # self.lname = lname

    def __str__(self):
        return "{} {}".format(self.s_id, super().__str__())

class ExchangeStudent(Student):
    def __init__(self, s_id, fname, lname, partner_univ):
        super().__init__(s_id, fname, lname)
        self.partner_univ = partner_univ



if __name__ == '__main__':
    s1 = Student("1234", "Fon", "Sairoong")
    print(s1)
    s2 = ExchangeStudent("7890", "Peter", "Parker", "ABC Univ.")
    print(s2)