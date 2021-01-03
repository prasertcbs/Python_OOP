class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def __str__(self):
        # return "fname: {}, lname: {}, age: {}".format(self.fname, self.lname, self.age)

        # a = vars(self)
        # # print(a)
        # s = ["{:10}: {}".format(k, v) for k, v in a.items()]
        # return "\n".join(s)

        attrs = ("fname", "lname", "age")
        s = ["{:10}: {}".format(a, getattr(self, a)) for a in attrs]
        return "\n".join(s)


if __name__ == '__main__':
    p = Person("Peter", "Parker", 26)
    print(p)
