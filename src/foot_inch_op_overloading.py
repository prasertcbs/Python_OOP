class FootInch:
    def __init__(self, foot, inch):
        self.foot = foot
        self.inch = inch
        self.inches = self.foot * 12 + self.inch

    def __str__(self):
        return "{}'{}\"".format(self.foot, self.inch)

    def __add__(self, other):  # overload + operator
        x = self.inches + other.inches
        f = x // 12
        i = x % 12
        return FootInch(f, i)

    def __sub__(self, other):  # overload - operator
        x = self.inches - other.inches
        f = x // 12
        i = x % 12
        return FootInch(f, i)

    # def __mul__(self, other):
    #     x = self.inches * other.inches
    #     f = x // 12
    #     i = x % 12
    #     return FootInch(f, i)


    # def __divmod__(self, other):
    # https://docs.python.org/3/library/functions.html#divmod
    #     x = self.inches * other.inches
    #     f = x // 12
    #     i = x % 12
    #     return FootInch(f, i)


if __name__ == '__main__':
    m1 = FootInch(2, 0)
    m2 = FootInch(3, 0)
    m = m1 + m2
    ma = m1.__add__(m2)
    m5 = m1 - m2
    # m6 = m1 * m2
    print(m)
    print(ma)
    print(m5)
    # print(m6)