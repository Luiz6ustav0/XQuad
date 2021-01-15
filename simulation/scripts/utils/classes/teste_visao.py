#!/usr/bin/env python

import rospy

from BlueFoxImage import BlueFoxImage
if __name__ == "__main__":
    rospy.init_node("visao", anonymous=False)
    print("teste")
    img = BlueFoxImage()
    print(img.exist_panel_qr())
    #img.get_panel_numbers()
    print(img.get_panel_qr())

