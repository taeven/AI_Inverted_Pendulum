import structures
from parameters import Setup


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

    fuz_angle = []
    fuz_angle.append(fuzzy(angle, prof_angle.neg_small))
    fuz_angle.append(fuzzy(angle, prof_angle.zero))
    fuz_angle.append(fuzzy(angle, prof_angle.pos_small))

    fuz_velocity = []
    fuz_velocity.append(fuzzy(velocity, prof_velocity.neg_small))
    fuz_velocity.append(fuzzy(velocity, prof_velocity.zero))
    fuz_velocity.append(fuzzy(velocity, prof_velocity.pos_small))

    print(angle, velocity)
    print(fuz_angle)
    print(fuz_velocity)
    

    for i in range(3):  # velocity
        for j in range(3):  # angle
            k = 0
            if i == 0 and j == 0:
                k = 2

            if (i == 0 and j == 1) or (i == 1 and j == 0):
                k = 1

            if (i == 0 and j == 2) or (i == 1 and j == 1) or (i == 2 and j == 0):
                k = 0

            if (i == 1 and j == 2) or (i == 2 and j == 1):
                k = -1

            if i == 2 and j == 2:
                k = -2

            # if fuz_angle[j] == 0 or fuz_velocity[i] == 0:
            #     combin.append((k, fuz_velocity[i]+fuz_angle[j]))
            # else:
            combin.append((k, min(fuz_velocity[i], fuz_angle[j])))
    # for i in range(3):
    print(combin)
    print("----------------------")
    #     for j in range(3):
    #         print(fuz_angle[i])

    #             # row1

    # combin.append((2, min(fuzzy(angle, prof_angle.neg_small),
    #                       fuzzy(velocity, prof_velocity.neg_small))))
    # combin.append((1, min(fuzzy(angle, prof_angle.zero),
    #                       fuzzy(velocity, prof_velocity.neg_small))))
    # combin.append((0, min(fuzzy(angle, prof_angle.pos_small),
    #                       fuzzy(velocity, prof_velocity.neg_small))))
    # # row2
    # combin.append((1, min(fuzzy(angle, prof_angle.neg_small),
    #                       fuzzy(velocity, prof_velocity.zero))))
    # combin.append((0, min(fuzzy(angle, prof_angle.zero),
    #                       fuzzy(velocity, prof_velocity.zero))))
    # combin.append((-1, min(fuzzy(angle, prof_angle.pos_small),
    #                        fuzzy(velocity, prof_velocity.zero))))
    # # row3
    # combin.append((0, min(fuzzy(angle, prof_angle.neg_small),
    #                       fuzzy(velocity, prof_velocity.pos_small))))
    # combin.append((-1, min(fuzzy(angle, prof_angle.zero),
    #                        fuzzy(velocity, prof_velocity.pos_small))))
    # combin.append((0, min(fuzzy(angle, prof_angle.pos_small),
    #                       fuzzy(velocity, prof_velocity.pos_small))))

    return combin


def defuzzy(prof_i, prof_angle, prof_velocity, angle, velocity):
    combin = get_i_profile(prof_angle, prof_velocity, angle, velocity)
    total_area = 0
    multiply = 0
    # print(combin)
    for (a, b) in combin:
        # print(a, " ", b, "-", angle, velocity)
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
    # print(multiply, " ", total_area)
    if multiply == 0:
        return 0
    ans = multiply/total_area
    return ans


# setup = Setup()
# defuzzy(setup.current, setup.angle, setup.velocity, 15, 0)


# i = 0
# while i <= 1:
#     print(i, " ", area_trapaz(i, angle.pos_small))
#     i = i+0.1
