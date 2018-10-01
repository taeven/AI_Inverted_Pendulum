class Trapaz:
    def __init__(self, t1, t2, t3, t4):
        self.t1 = t1
        self.t2 = t2
        self.t4 = t4
        self.t3 = t3


class Profile:
    def set_zero(self, t1, t2, t4):
        t3 = t2
        self.zero = Trapaz(t1, t2, t3, t4)

    def set_small(self, t1, t2, t3, t4):
        self.pos_small = Trapaz(t1, t2, t3, t4)
        self.neg_small = Trapaz(-t4, -t3, -t2, -t1)

    def set_medium(self, t1, t2, t3, t4):
        self.medium = Trapaz(t1, t2, t3, t4)
