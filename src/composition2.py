class Printer:
    def print_page(self, data):
        print("printing {}".format(data))


class Scanner:
    def scan_page(self):
        print("scanning...")


class Fax:
    def fax_page(self, number):
        print("faxing to {}".format(number))


class Aio:  # all in one printer
    def __init__(self, p, s, f):
        self.p = p
        self.s = s
        self.f = f


if __name__ == '__main__':
    a = Aio(Printer(), Scanner(), Fax())
    a.p.print_page("hello")
    a.s.scan_page()
    a.f.fax_page("022185765")
