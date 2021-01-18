import rospy
from gazebo_ros_link_attacher.srv import Attach

import time


def link(model_name, mode=0):
    """
        attach or detach UAV to a model through a link

        params:
            model_name:
                name of the gazebo model the drone must be attached to
            mode:
                default = 0
                If mode is 0 then this function tries to attach the drone to
                model_name, if mode is 1 then this function tries to detach 
                the drone from model_name
    """
    
    modes = ['attach', 'detach']
    
    drone_model = "uav1"
    drone_link = "uav1::base_link" # "uav1::uav1/imu_link"

    model_link = 'equipment' + model_name + '::link_' + model_name

    serviceName = "/link_attacher_node/" + modes[mode]
    rospy.wait_for_service(serviceName)
    try:
        attach_func = rospy.ServiceProxy(serviceName, Attach)
        resp1 = attach_func(drone_model, drone_link, 'equipment' + model_name, model_link)
    except rospy.ServiceException as e:
        print("Error: %s" % e)

    return resp1
