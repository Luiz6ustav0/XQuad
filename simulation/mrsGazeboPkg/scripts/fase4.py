#!/usr/bin/env python

import rospy

from utils.functions.move_uav import go_to
from utils.classes.ReferencePublisher import ReferencePublisher
from utils.classes.BlueFoxImage import *
from utils.functions.fase1_utils import go_home
from utils.functions.Land import land
from utils.functions.align import align
from utils.functions.gazebo_ros_link import link

import time


def main():

    rospy.init_node("fase_4", anonymous=False)
    pub = ReferencePublisher()
    z = 2.2
    bases = [(-0.25, 6, z), (-3.25, 0, z), (-6.25, 0, z), (-5.25, 1, z), (-4.25, 2, z)]  

    imagem = BlueFoxImage()

    for base in bases:
        print("Objetivo: {}".format(base))
        go_to(pub.pub_reference, base)
        go_to(pub.pub_reference, (base[0], base[1], 1))
        go_to(pub.pub_reference, (base[0], base[1], 0.4))
        time.sleep(1)
        existe = imagem.exist_panel_qr()

        if existe:
            # align(pub.pub_reference)
            letter = imagem.get_panel_qr()
            if letter != "Erro de leitura":
                go_to(pub.pub_reference, (base[0], base[1], 0.3))
                print("Linking to: " + letter)
                link(letter)
                go_to(pub.pub_reference, (base[0], base[1], 1.0))
                #go_to(pub.pub_reference, (-3, 3, 2.2))
                go_to(pub.pub_reference, (0, 0, 2.2))
                link(letter, mode=1)
                time.sleep(1)
            else:
                print("Failed to read QR Code")
        else:
            print("No QR code here")

main()
