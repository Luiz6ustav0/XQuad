import rospy
import time

from mrs_msgs.msg import *
from geometry_msgs.msg import *
from std_msgs.msg import *
from std_srvs.srv import *
from mavros_msgs.srv import *
from mrs_msgs.srv import *
from mrs_msgs.msg import *
from mavros_msgs.msg import *

from utils.classes.Tracker import Tracker


def land():
    services = [
        "/uav1/uav_manager/land",
        "/uav1/control_manager/motors 0",
        "/uav1/mavros/cmd/arming 0",
    ]

    state_tracker = Tracker()

    message_types = [SetBool, CommandBool, SetMode, Trigger]
    arguments = [1, 1, [0, "offboard"], None]

    first_call = 0

    # Land
    while (
        state_tracker.tracker != "LandoffTracker"
        and state_tracker.tracker is not "NullTracker"
    ) or first_call == 0:
        first_call = 1
        serviceName = services[0].split(" ")[0]
        print("Waiting for {}\n".format(serviceName))
        rospy.wait_for_service(serviceName)
        try:
            run_service = rospy.ServiceProxy(serviceName, Trigger)
            print("Running {}\n\n".format(serviceName))
            resp1 = run_service()
        except rospy.ServiceException as e:
            print("Error: %s" % e)
        time.sleep(1)

    # Desligando Motors
    while state_tracker.tracker != "NullTracker":
        time.sleep(2)

    while state_tracker.motors:
        serviceName = services[1].split(" ")[0]
        print("Waiting for {}\n".format(serviceName))
        rospy.wait_for_service(serviceName)
        try:
            run_service = rospy.ServiceProxy(serviceName, SetBool)
            print("Running {}\n\n".format(serviceName))
            resp1 = run_service(0)
        except rospy.ServiceException as e:
            print("Error: %s" % e)
        time.sleep(1)

    # Arming
    serviceName = services[2].split(" ")[0]
    print("Waiting for {}\n".format(serviceName))
    rospy.wait_for_service(serviceName)
    try:
        run_service = rospy.ServiceProxy(serviceName, CommandBool)
        print("Running {}\n\n".format(serviceName))
        resp1 = run_service(0)
    except rospy.ServiceException as e:
        print("Error: %s" % e)
