def immutable_demo():
    # n = 5
    # print("id(n) = {}, n = {}".format(id(n), n))
    # n = n + 4
    # print("id(n) = {}, n = {}".format(id(n), n))
    s = "rain"
    print("id(s) = {}, s = {}".format(id(s), s))
    s = s + "bow"
    print("id(s) = {}, s = {}".format(id(s), s))

def mutable_demo():
    p = ["rain"]
    print("id(p) = {}, p = {}".format(id(p), p))
    p[0] = p[0] + "bow"
    print("id(p) = {}, p = {}".format(id(p), p))
    q = p
    print("id(p) = {}, p = {}\nid(q) = {}, q = {}".format(id(p), p, id(q), q))
    q.append("sunshine")
    print("id(p) = {}, p = {}\nid(q) = {}, q = {}".format(id(p), p, id(q), q))

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return "id(self) = {}, name = {}, phone = {}".format(id(self), self.name, self.phone)

if __name__ == '__main__':
    # immutable_demo()
    # mutable_demo()
    a = Contact("Fah", "0812223333")
    print(a)
    a.phone = "0992223333"
    print(a)
    b = a
    print(b)
    b.phone = "0773334444"
    print("a = ", a)
    print("b = ", b)