import structures as ps

class Setup:
    def __init__(self):
        self.velocity = ps.Profile()
        self.velocity.set_zero(-30, 0, 30)
        self.velocity.set_small(0, 30, 90, 120)

        self.angle = ps.Profile()
        self.angle.set_small(0, 30, 90, 120)
        self.angle.set_zero(-30, 0, 30)

        self.current = ps.Profile()
        self.current.set_zero(-10, 0, 10)
        self.current.set_small(0, 10, 15, 25)
        self.current.set_medium(15, 25, 40, 55)
