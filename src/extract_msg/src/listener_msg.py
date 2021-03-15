#!/usr/bin/env python
import rospy
from franka_core_msgs.msg import RobotState # Python message class for Odometry

robot_state_jacobian = None 
def timer_callback(event): # Type rospy.TimerEvent
    print('timer_cb (' + str(event.current_real) + '): jacobian is')
    print(str(None) if robot_state_jacobian is None else str(robot_state_jacobian))
def sub_callback(data):
    global robot_state_jacobian
    #rospy.loginfo(data.O_Jac_EE)
    robot_state_jacobian = data.O_Jac_EE
    print robot_state_jacobian
def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/panda_simulator/custom_franka_state_controller/robot_state", RobotState, sub_callback)
    rospy.Timer(rospy.Duration(2), timer_callback)
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()