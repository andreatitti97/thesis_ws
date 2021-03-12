## *********************************************************
##
## File autogenerated for the franka_ros_controllers package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 245, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [{'upper': 'CONTROLLER_GAINS', 'lower': 'controller_gains', 'srcline': 124, 'name': 'Controller_Gains', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT::CONTROLLER_GAINS', 'field': 'DEFAULT::controller_gains', 'state': True, 'parentclass': 'DEFAULT', 'groups': [], 'parameters': [{'srcline': 20, 'description': 'Stiffness parameter of joint 1', 'max': 1500.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/andrea/thesis_ws/src/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'name': 'j1_k', 'edit_method': '', 'default': 1200.0, 'level': 0, 'min': 200.0, 'type': 'double'}, {'srcline': 21, 'description': 'Stiffness parameter of joint 2', 'max': 1500.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/andrea/thesis_ws/src/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'name': 'j2_k', 'edit_method': '', 'default': 1000.0, 'level': 0, 'min': 200.0, 'type': 'double'}, {'srcline': 22, 'description': 'Stiffness parameter of joint 3', 'max': 1500.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/andrea/thesis_ws/src/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'name': 'j3_k', 'edit_method': '', 'default': 1000.0, 'level': 0, 'min': 200.0, 'type': 'double'}, {'srcline': 23, 'description': 'Stiffness parameter of joint 4', 'max': 1500.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/andrea/thesis_ws/src/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'name': 'j4_k', 'edit_method': '', 'default': 800.0, 'level': 0, 'min': 200.0, 'type': 'double'}, {'srcline': 24, 'description': 'Stiffness parameter of joint 5', 'max': 1000.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/andrea/thesis_ws/src/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'name': 'j5_k', 'edit_method': '', 'default': 300.0, 'level': 0, 'min': 100.0, 'type': 'double'}, {'srcline': 25, 'description': 'Stiffness parameter of joint 6', 'max': 500.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/andrea/thesis_ws/src/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'name': 'j6_k', 'edit_method': '', 'default': 200.0, 'level': 0, 'min': 75.0, 'type': 'double'}, {'srcline': 26, 'description': 'Stiffness parameter of joint 7', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/andrea/thesis_ws/src/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'name': 'j7_k', 'edit_method': '', 'default': 50.0, 'level': 0, 'min': 20.0, 'type': 'double'}, {'srcline': 28, 'description': 'Damping parameter of joint 1', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/andrea/thesis_ws/src/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'name': 'j1_d', 'edit_method': '', 'default': 50.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 29, 'description': 'Damping parameter of joint 2', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/andrea/thesis_ws/src/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'name': 'j2_d', 'edit_method': '', 'default': 50.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 30, 'description': 'Damping parameter of joint 3', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/andrea/thesis_ws/src/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'name': 'j3_d', 'edit_method': '', 'default': 50.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 31, 'description': 'Damping parameter of joint 4', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/andrea/thesis_ws/src/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'name': 'j4_d', 'edit_method': '', 'default': 20.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 32, 'description': 'Damping parameter of joint 5', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/andrea/thesis_ws/src/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'name': 'j5_d', 'edit_method': '', 'default': 20.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 33, 'description': 'Damping parameter of joint 6', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/andrea/thesis_ws/src/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'name': 'j6_d', 'edit_method': '', 'default': 20.0, 'level': 0, 'min': 0.0, 'type': 'double'}, {'srcline': 34, 'description': 'Damping parameter of joint 7', 'max': 200.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/home/andrea/thesis_ws/src/franka_ros_interface/franka_ros_controllers/cfg/joint_controller_params.cfg', 'name': 'j7_d', 'edit_method': '', 'default': 10.0, 'level': 0, 'min': 0.0, 'type': 'double'}], 'type': '', 'id': 1}], 'parameters': [{'srcline': 290, 'description': 'Filter parameter that dictates how smoothly subsequent joint position commands are smoothed. Also responsible for speed of joint position execution.', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'position_joint_delta_filter', 'edit_method': '', 'default': 0.3, 'level': 0, 'min': 0.1, 'type': 'double'}, {'srcline': 290, 'description': 'Filter parameter that dictates how smoothly subsequent joint velocity commands are smoothed. Also responsible for acceleration of joints.', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'name': 'velocity_joint_delta_filter', 'edit_method': '', 'default': 0.3, 'level': 0, 'min': 0.1, 'type': 'double'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

