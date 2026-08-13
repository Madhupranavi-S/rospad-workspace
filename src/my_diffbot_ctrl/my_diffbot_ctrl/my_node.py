import rclpy                                          # ROS 2 Python library
from rclpy.node import Node                           # base class for every node
from geometry_msgs.msg import Twist                  # velocity command: linear + angular


class DriveForward(Node):
    def __init__(self):
        super().__init__('drive_forward')              # register node name
        self.pub   = self.create_publisher(Twist, '/cmd_vel', 10)  # publish to /cmd_vel
        self.timer = self.create_timer(0.1, self.drive)             # call drive() at 10 Hz
        self.get_logger().info('Driving forward at 0.3 m/s')      # log startup

    def drive(self):                                   # called every 0.1 s
        msg = Twist()                                   # create a blank velocity command
        msg.linear.x  = 0.3   # forward speed in m/s
        msg.angular.z = 0.0   # no rotation
        self.pub.publish(msg)                           # send to the robot


def main(args=None):
    rclpy.init(args=args)                               # start the ROS 2 runtime
    rclpy.spin(DriveForward())                          # create node and loop until Ctrl-C
    rclpy.shutdown()                                    # clean up