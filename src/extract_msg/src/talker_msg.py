#!/usr/bin/env python

import rospy
import genpy
import struct
from franka_core_msgs.msg import RobotState 
from listener_msg import robot_state_jacobian

import franka_msgs.msg
import std_msgs.msg

def talker():
    pub = rospy.Publisher("/panda_simulator/custom_franka_state_controller/robot_state",float, queue_size=50)
    rospy.init_node('robot_jacobian_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    #self = robot_state_jacobian
    robot_state = robot_state_jacobian
    while not rospy.is_shutdown():
        #getattr(RobotState)
        #RobotState._get_types(self)
        rospy.loginfo(robot_state.attr)
        #pub.publish(robot_state.O_Jac_EE)
        rate.sleep()

#class RobotState.O_Jac_EE 

if __name__ == '__main__':
    robot_state = RobotState()
    #print('Jacobian',getattr(robot_state,"O_Jac_EE"))
    attr = getattr(robot_state,"O_Jac_EE")

    try:
        talker()
    except rospy.ROSInterruptException:
        pass
