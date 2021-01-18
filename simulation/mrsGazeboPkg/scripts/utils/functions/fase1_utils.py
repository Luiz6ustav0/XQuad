import math
import time

from utils.classes.BlueFoxImage import *
from utils.classes.Position_Command import Position_Info
from utils.functions.move_uav import *
from utils.functions.Land import land
from utils.functions.takeoff import takeoff
from utils.functions.align import align

def bases_suspensas():
    base_s_1 = [-0.15, 6, 2.5]
    base_s_2 = [-3, 0, 2.5]
    bases = [base_s_1, base_s_2]
    return bases


def taking_photo():
    imagem = BlueFoxImage()
    c = imagem.get_distances_platforms()
    print(c)
    return c


def land_takeoff_routine():
    time.sleep(2)
    land()
    time.sleep(2)
    takeoff()
    time.sleep(2)


def compare_bases(all_bases, base):
    existe = 0
    for known_base in all_bases:
        # print("Base: x:{}, y:{}".format(base[0], base[1]))
        # print("Known_base: x:{}, y:{}".format(known_base[0], known_base[1]))
        if (
            (abs(base[1] - known_base[1]) < 0.5)
            and (abs(base[0] - known_base[0]) < 0.5)
            or (base[0] == 0.0 and base[1] == 0.0)
        ):
            existe = 1
            print("existe ja a base")
            break
    return existe


def go_to_base_and_align(publisher, base):
    reducao_altura_na_base = (base[0], base[1], 1.0)

    go_to(publisher.pub_reference, base)
    time.sleep(2)

    go_to(publisher.pub_reference, reducao_altura_na_base)
    time.sleep(2)

    align(publisher.pub_reference)
    time.sleep(2)


def go_home(publisher):
    home = (-0.25, 0.25, 2.5)
    go_to(publisher.pub_reference, home)
    time.sleep(1)
    align(publisher.pub_reference)
    time.sleep(1)
