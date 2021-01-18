#!/usr/bin/env python

import rospy
import time
from mrs_msgs.srv import *
from mrs_msgs.msg import *
from geometry_msgs.msg import *
from sensor_msgs.msg import *
from std_msgs.msg import *
from std_srvs.srv import *
from mavros_msgs.srv import *
from mavros_msgs.msg import *

from utils.classes.Tracker import Tracker
from utils.classes.Motor import Motor
from utils.classes.MavrosState import MavrosState
from utils.functions.Land import land

# Talvez usar ros::time e uma boa....
# Por que o modo offboard?
# Para motores pode ser tbm o /uav1/control_manager/motors ?


def takeoff():

    mavros_state = MavrosState()
    motors = Motor()
    state_trackers = Tracker()

    services = [
        "/uav1/control_manager/motors 1",
        "/uav1/mavros/cmd/arming 1",
        "/uav1/mavros/set_mode 0 offboard",
        "/uav1/uav_manager/takeoff",
    ]

    # Motors
    while not motors.motors:
        serviceName = services[0].split(" ")[0]
        print("Waiting for {}\n".format(serviceName))
        rospy.wait_for_service(serviceName)
        try:
            run_service = rospy.ServiceProxy(serviceName, SetBool)
            print("Running {}\n\n".format(serviceName))
            resp1 = run_service(1)
        except rospy.ServiceException as e:
            print("Error: %s" % e)
        time.sleep(1)

    # Arming UAV
    while not mavros_state.armed:
        serviceName = services[1].split(" ")[0]
        print("Waiting for {}\n".format(serviceName))
        rospy.wait_for_service(serviceName)
        try:
            run_service = rospy.ServiceProxy(serviceName, CommandBool)
            print("Running {}\n\n".format(serviceName))
            resp1 = run_service(1)
        except rospy.ServiceException as e:
            print("Error: %s" % e)
        time.sleep(1)

    # Set Mode
    while mavros_state.mode != "OFFBOARD":
        serviceName = services[2].split(" ")[0]
        print("Waiting for {}\n".format(serviceName))
        rospy.wait_for_service(serviceName)
        try:
            run_service = rospy.ServiceProxy(serviceName, SetMode)
            print("Running {}\n\n".format(serviceName))
            resp1 = run_service(0, "offboard")
        except rospy.ServiceException as e:
            print("Error: %s" % e)
        time.sleep(1)

    # Takeoff
    serviceName = services[3].split(" ")[0]
    print("Waiting for {}\n".format(serviceName))
    rospy.wait_for_service(serviceName)
    try:
        run_service = rospy.ServiceProxy(serviceName, Trigger)
        print("Running {}\n\n".format(serviceName))
        resp1 = run_service()
    except rospy.ServiceException as e:
        print("Error: %s" % e)

    cnt = 0
    while state_trackers.tracker != "MpcTracker":
        if cnt < 8:
            print("taking off...")
            cnt += 1
            time.sleep(2)
        else:
            land()
            takeoff()
