from std_msgs.msg import *
from mrs_msgs.msg import *
from geometry_msgs.msg import *

from utils.classes.Position_Command import *


def go_to(publisher, pos):
    header = Header()
    reference = Reference()
    msg = ReferenceStamped()
    pos_atual = Position_Info()

    header.frame_id = "uav1/hector_origin"

    x, y, z = pos[0], pos[1], pos[2]
    reference.position = Point(x, y, z)

    msg.header = header
    msg.reference = reference
    publisher.publish(msg)
    while not in_position(reference, pos_atual):
        publisher.publish(msg)


def in_position(goal, p_atual):
    pos = Position_Info()
    delta = 0.001
    x_aux = p_atual.pos.position.x
    y_aux = p_atual.pos.position.y
    z_aux = p_atual.pos.position.z
    if (
        (abs(x_aux - goal.position.x) >= delta)
        or (abs(y_aux - goal.position.y) >= delta)
        or (abs(z_aux - goal.position.z) >= delta)
    ):
        time.sleep(2)
        return False
    return True
