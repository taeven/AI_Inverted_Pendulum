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


def fuzzy(t, profile):
    if t >= profile.t1 and t < profile.t2:
        return (1/(profile.t2 - profile.t1))*(t-profile.t1)
    if t >= profile.t2 and t <= profile.t3:
        return 1
    if t > profile.t3 and t <= profile.t4:
        return (1/(profile.t3-profile.t4))*(t-profile.t4)
    return 0


def area_trapaz(h, trapaz):
    x = h*(trapaz.t2 - trapaz.t1)+trapaz.t1
    area = (trapaz.t4-trapaz.t1 - x)*h
    return area


def get_i_profile(prof_angle, prof_velocity, angle, velocity):
    combin = []
    # row1
    combin.append((2, min(fuzzy(angle, prof_angle.neg_small),
                          fuzzy(velocity, prof_velocity.neg_small))))
    combin.append((1, min(fuzzy(angle, prof_angle.zero),
                          fuzzy(velocity, prof_velocity.neg_small))))
    combin.append((0, min(fuzzy(angle, prof_angle.pos_small),
                          fuzzy(velocity, prof_velocity.neg_small))))
    # row2
    combin.append((1, min(fuzzy(angle, prof_angle.neg_small),
                          fuzzy(velocity, prof_velocity.zero))))
    combin.append((0, min(fuzzy(angle, prof_angle.zero),
                          fuzzy(velocity, prof_velocity.zero))))
    combin.append((-1, min(fuzzy(angle, prof_angle.pos_small),
                           fuzzy(velocity, prof_velocity.zero))))
    # row3
    combin.append((0, min(fuzzy(angle, prof_angle.neg_small),
                          fuzzy(velocity, prof_velocity.pos_small))))
    combin.append((-1, min(fuzzy(angle, prof_angle.zero),
                           fuzzy(velocity, prof_velocity.pos_small))))
    combin.append((0, min(fuzzy(angle, prof_angle.pos_small),
                          fuzzy(velocity, prof_velocity.pos_small))))

    return combin


def defuzzy(prof_i, prof_angle, prof_velocity, angle, velocity):
    combin = get_i_profile(prof_angle, prof_velocity, angle, velocity)
    total_area = 0
    multiply = 0
    for (a, b) in combin:
        print(a, " ", b, "-", angle, velocity)
        area = 0
        centroid_x = 0
        if abs(a) == 0:
            area = area_trapaz(b, prof_i.zero)
            centroid_x = (prof_i.zero.t4 + prof_i.zero.t1)/2
        if abs(a) == 1:
            area = area_trapaz(b, prof_i.pos_small)
            centroid_x = (prof_i.pos_small.t4 + prof_i.pos_small.t1)/2
        if abs(a) == 2:
            area = area_trapaz(b, prof_i.medium)
            centroid_x = (prof_i.medium.t4 + prof_i.medium.t1)/2

        # sign of centroid
        if a != 0:
            centroid_x = centroid_x*(a/abs(a))
        total_area = total_area + area
        multiply = multiply + area*centroid_x
    print(multiply, " ", total_area)
    if multiply == 0:
        return 0
    ans = multiply/total_area
    return ans


# i = 0
# while i <= 1:
#     print(i, " ", area_trapaz(i, angle.pos_small))
#     i = i+0.1
