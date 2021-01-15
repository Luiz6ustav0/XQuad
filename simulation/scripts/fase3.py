#!/usr/bin/env python

import rospy
from mrs_msgs.srv import *
from mrs_msgs.msg import *
from geometry_msgs.msg import *
from sensor_msgs.msg import *
from std_msgs.msg import *

from utils.functions.move_uav import go_to
from utils.classes.ReferencePublisher import ReferencePublisher
from utils.classes.BlueFoxImage import *
from utils.functions.fase1_utils import go_home
from utils.functions.Land import land
from utils.classes.Painel import Painel
from utils.functions.align import align

import math
import time
import numpy as np

# VALORES DAS PLATAFORMAS
# 7 4 -> -1.25 2
# 6 7 -> -2.25 5
# 2 2 -> -6.25 0
# -0.15, 6, 2.5
# -3, 0, 2.5
# tirar do loop do blue fox


def photo_analyse():
    imagem = BlueFoxImage()
    if imagem.exist_panel():
        print("\nPainel localizado")
        numeros_encontrados = imagem.get_numbers()
        painel = Painel(numeros_encontrados[0], numeros_encontrados[1])
        print(painel)
    else:
        print("\nNao ha painel nesta base\n")


def main():
    rospy.init_node("paineis", anonymous=False)
    pub = ReferencePublisher()
    z = 2.2
    bases = [(-0.15, 6, z), (-3.25, 0, z), (-1.25, 2, z), (-2.25, 5, z), (-6.25, 0, z)]

    for base in bases:
        print("Objetivo: {}".format(base))
        go_to(pub.pub_reference, base)
        time.sleep(5)
        go_to(pub.pub_reference, (base[0], base[1], 1))
        time.sleep(3)
        align(pub.pub_reference)
        go_to(pub.pub_reference, (base[0], base[1], 0.3))
        time.sleep(5)

        photo_analyse()
        time.sleep(1)

        go_to(pub.pub_reference, (base[0], base[1], 2.2))
        time.sleep(1)

    centro_safe = (-3, 3, 1.2)
    go_to(pub.pub_reference, centro_safe)
    time.sleep(2)
    go_home(pub)
    time.sleep(15)
    land()


main()
