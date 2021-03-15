#! /usr/bin/env python

import rospy
from franka_core_msgs.msg import RobotState # Python message class RobotState
#from listener_msg import robot_state_jacobian
global robot_state_jacobian
rospy.init_node("robot_state_pub")
msg = rospy.wait_for_message("/panda_simulator/custom_franka_state_controller/robot_state", RobotState)

#print msg.header
print msg.O_Jac_EE
robot_state_jacobian = msg.O_Jac_EE
#robot_state_jacobian = msg.0_Jac_EE #Jacobian saved in sleep position 
