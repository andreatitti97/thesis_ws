#!/usr/bin/env python

import rospy
from franka_core_msgs.msg import RobotState 
from listener_msg import robot_state_jacobian

def talker():
    pub = rospy.Publisher("/panda_simulator/custom_franka_state_controller/robot_state", RobotState, queue_size=None)
    rospy.init_node('robot_jacobian_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        pub.publish(robot_state_jacobian)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
