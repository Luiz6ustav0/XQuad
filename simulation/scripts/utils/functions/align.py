#!/usr/bin/env python
import math
import time

from utils.classes.BlueFoxImage import *
from utils.classes.Position_Command import Position_Info
from utils.functions.move_uav import *


def align(pub):
    img = BlueFoxImage()
    print("Alinhamento do drone sendo realizado")
    ang_x = img.angle_scan(img.get_centroid())[1][0][0]
    ang_y = img.angle_scan(img.get_centroid())[1][0][1]
    ang_total = math.sqrt(ang_x ** 2 + ang_y ** 2)
    primeira = 1
    cnt = 0
    while (ang_total > 0.08 or primeira) and cnt < 2:
        # print("ANGULO TOTAL: {}".format(ang_total))
        align_y(pub)
        align_x(pub)
        primeira = 0
        ang_x = img.angle_scan(img.get_centroid())[1][0][0]
        ang_y = img.angle_scan(img.get_centroid())[1][0][1]
        ang_total = math.sqrt(ang_x ** 2 + ang_y ** 2)
        cnt += 1


def align_y(pub):
    img = BlueFoxImage()
    centro = img.angle_scan(img.get_centroid())[1][0]
    flag = img.angle_scan(img.get_centroid())[0]
    # print("FLAG: {}, ANGULOS: {}, {}".format(flag, centro[0], centro[1]))
    # time.sleep(5)
    if abs(centro[0]) > 0.01:
        if centro[0] > 0:
            while centro[0] > 0:
                move_positive_dy(pub)
                centro = img.angle_scan(img.get_centroid())[1][0]
        elif centro[0] < 0:
            while centro[0] < 0:
                move_negative_dy(pub)
                centro = img.angle_scan(img.get_centroid())[1][0]


def align_x(pub):
    img = BlueFoxImage()
    centro = img.angle_scan(img.get_centroid())[1][0]
    flag = img.angle_scan(img.get_centroid())[0]
    # print("FLAG: {}, ANGULOS: {}, {}\n".format(flag, centro[0], centro[1]))
    # time.sleep(5)
    if abs(centro[1]) > 0.01:
        if centro[1] > 0:
            while centro[1] > 0:
                move_positive_dx(pub)
                centro = img.angle_scan(img.get_centroid())[1][0]
        elif centro[1] < 0:
            while centro[1] < 0:
                move_negative_dx(pub)
                centro = img.angle_scan(img.get_centroid())[1][0]


def move_positive_dx(pub):
    current_pos = Position_Info()
    while current_pos.pos.position.x == 0.00:
        pass
    next_pos = (
        current_pos.pos.position.x + 0.1,
        current_pos.pos.position.y,
        current_pos.pos.position.z,
    )
    go_to(pub, next_pos)


def move_negative_dx(pub):
    current_pos = Position_Info()
    while current_pos.pos.position.x == 0.00:
        pass
    next_pos = (
        current_pos.pos.position.x - 0.1,
        current_pos.pos.position.y,
        current_pos.pos.position.z,
    )
    go_to(pub, next_pos)


def move_positive_dy(pub):
    current_pos = Position_Info()
    while current_pos.pos.position.x == 0.00:
        pass
    next_pos = (
        current_pos.pos.position.x,
        current_pos.pos.position.y + 0.1,
        current_pos.pos.position.z,
    )
    go_to(pub, next_pos)


def move_negative_dy(pub):
    current_pos = Position_Info()
    while current_pos.pos.position.x == 0.00:
        pass
    next_pos = (
        current_pos.pos.position.x,
        current_pos.pos.position.y - 0.1,
        current_pos.pos.position.z,
    )
    go_to(pub, next_pos)
