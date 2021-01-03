class Eyeglasses:
    def __init__(self, eye, bridge, temple):
        self.eye = eye
        self.bridge = bridge
        self.temple = temple

    @classmethod  # function decorator
    def of(cls, frame_string, sep="-"):
        s = frame_string.split(sep)
        return cls(int(s[0]), int(s[1]), int(s[2]))

    @classmethod
    def of2(cls, frame_with_weight):
        pass

    @staticmethod
    def gram_oz(g):
        return g * 0.035274

    def __str__(self):
        return "{}-{}-{}".format(self.eye, self.bridge, self.temple)


if __name__ == '__main__':
    f1 = Eyeglasses(55, 16, 140)
    print(f1)
    f2 = Eyeglasses.of("55,16,140", ",")
    print(f2)
    print(f2.eye, f2.bridge, f2.temple)
    print(Eyeglasses.gram_oz(20))
