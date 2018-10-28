import structures as ps

class Setup:
    def __init__(self):


        #velocity profile
        self.velocity = ps.Profile()
        self.velocity.set_zero(-30, 0, 30)
        self.velocity.set_small(0, 30, 90, 120)


        #angle profile
        self.angle = ps.Profile()
        self.angle.set_small(0, 30, 90, 120)
        self.angle.set_zero(-30, 0, 30)


        #current profile
        self.current = ps.Profile()
        self.current.set_zero(-10, 0, 10)
        self.current.set_small(0, 10, 15, 25)
        self.current.set_medium(15, 25, 40, 55)

        #Gravitation acc
        self.g_value = 10
        #MOment of Intertia
        self.I = 0.8
        #constant int the eq. (i = k*I*alpha)
        self.k = 1
        #start angle
        self.start_angle = -40
        #start omega
        self.start_velocity = 0
        #start acceleration
        self.start_alpha = 0
        #differential time
        self.dt = 1
