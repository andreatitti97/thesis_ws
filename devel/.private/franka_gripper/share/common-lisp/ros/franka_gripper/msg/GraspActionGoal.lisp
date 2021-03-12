; Auto-generated. Do not edit!


(cl:in-package franka_gripper-msg)


;//! \htmlinclude GraspActionGoal.msg.html

(cl:defclass <GraspActionGoal> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (goal_id
    :reader goal_id
    :initarg :goal_id
    :type actionlib_msgs-msg:GoalID
    :initform (cl:make-instance 'actionlib_msgs-msg:GoalID))
   (goal
    :reader goal
    :initarg :goal
    :type franka_gripper-msg:GraspGoal
    :initform (cl:make-instance 'franka_gripper-msg:GraspGoal)))
)

(cl:defclass GraspActionGoal (<GraspActionGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GraspActionGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GraspActionGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name franka_gripper-msg:<GraspActionGoal> is deprecated: use franka_gripper-msg:GraspActionGoal instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <GraspActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader franka_gripper-msg:header-val is deprecated.  Use franka_gripper-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'goal_id-val :lambda-list '(m))
(cl:defmethod goal_id-val ((m <GraspActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader franka_gripper-msg:goal_id-val is deprecated.  Use franka_gripper-msg:goal_id instead.")
  (goal_id m))

(cl:ensure-generic-function 'goal-val :lambda-list '(m))
(cl:defmethod goal-val ((m <GraspActionGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader franka_gripper-msg:goal-val is deprecated.  Use franka_gripper-msg:goal instead.")
  (goal m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GraspActionGoal>) ostream)
  "Serializes a message object of type '<GraspActionGoal>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal_id) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'goal) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GraspActionGoal>) istream)
  "Deserializes a message object of type '<GraspActionGoal>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal_id) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'goal) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GraspActionGoal>)))
  "Returns string type for a message object of type '<GraspActionGoal>"
  "franka_gripper/GraspActionGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspActionGoal)))
  "Returns string type for a message object of type 'GraspActionGoal"
  "franka_gripper/GraspActionGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GraspActionGoal>)))
  "Returns md5sum for a message object of type '<GraspActionGoal>"
  "7bd1a6e7f94ef15bb6dd05cb170e7909")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GraspActionGoal)))
  "Returns md5sum for a message object of type 'GraspActionGoal"
  "7bd1a6e7f94ef15bb6dd05cb170e7909")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GraspActionGoal>)))
  "Returns full string definition for message of type '<GraspActionGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%GraspGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: franka_gripper/GraspGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%float64 width # [m]~%GraspEpsilon epsilon~%float64 speed # [m/s]~%float64 force # [N]~%~%================================================================================~%MSG: franka_gripper/GraspEpsilon~%float64 inner # [m]~%float64 outer # [m]~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GraspActionGoal)))
  "Returns full string definition for message of type 'GraspActionGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%GraspGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: franka_gripper/GraspGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%float64 width # [m]~%GraspEpsilon epsilon~%float64 speed # [m/s]~%float64 force # [N]~%~%================================================================================~%MSG: franka_gripper/GraspEpsilon~%float64 inner # [m]~%float64 outer # [m]~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GraspActionGoal>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal_id))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'goal))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GraspActionGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'GraspActionGoal
    (cl:cons ':header (header msg))
    (cl:cons ':goal_id (goal_id msg))
    (cl:cons ':goal (goal msg))
))
