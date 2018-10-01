import profiles as ps


class Setup:
    def __init__(self):
        self.velocity = ps.Profile()
        self.velocity.set_zero(-5, 0, 5)
        self.velocity.set_small(0, 5, 10, 15)

        self.angle = ps.Profile()
        self.angle.set_small(0, 5, 10, 15)
        self.angle.set_zero(-5, 0, 5)

        self.current = ps.Profile()
        self.current.set_zero(-5, 0, 5)
        self.current.set_small(0, 5, 10, 15)
        self.current.set_medium(10, 15, 20, 25)
