class Athlete:
    def __init__(self, name, sport, medal):
        self.name = name
        self.sport = sport
        self.medal = medal

    def __str__(self):
        return "{:10} {:12} {}".format(self.name, self.sport, self.medal)

    def __lt__(self, other):
        d = {"gold": 1, "silver": 2, "bronze": 3}
        if d[self.medal] == d[other.medal]:
            return self.name < other.name
        else:
            return d[self.medal] < d[other.medal]
            # return d[self.medal] < d[other.medal]
            # return self.medal > other.medal


if __name__ == '__main__':
    data = [
        Athlete("Peter", "Judo", "silver"),
        Athlete("Taylor", "Tennis", "gold"),
        Athlete("John", "Tennis", "silver"),
        Athlete("Sarah", "Badminton", "bronze"),
        Athlete("Tony", "Boxing", "gold"),
        Athlete("Bruce", "Judo", "gold"),
    ]
    s = sorted(data)
    [print(e) for e in s]
