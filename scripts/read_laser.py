#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def laser_read(msg):
    # 720/5 = 144
    area = [min(msg.ranges[0:143]), min(msg.ranges[144:287]), min(msg.ranges[288:431]), min(msg.ranges[432:575]), min(msg.ranges[576:713]),]
    rospy.loginfo(area)

def main():
    rospy.init_node('read_laser')
    sub= rospy.Subscriber("/laser/scan", LaserScan, laser_read)
    rospy.spin()

if __name__ == '__main__':
    main()
