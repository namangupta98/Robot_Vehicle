# Robot Vehicle

## Overview
This is a coursework project for ENPM690: Robot Learning to program a simple robot vehicle and add a programmed behavior to the robot from the scratch.

## Dependencies
1. ROS
2. Gazebo
3. Linux

## Instructions
Open new terminal and clone the file in your ROS_workspace/src folder. Type
```
git clone https://github.com/namangupta98/robot_vehicle
```
Build the package by typing
```
$ ~/catkin_ws: catkin_make
``` 
Inside ROS_workspace, run the launch file. Type
```
source devel/setup.bash
roslaunch robot_vehicle spawn.launch telekey:=true
```

Gazebo will open in which my_robot model is there.

<p align="center">
  <img="https://github.com/namangupta98/robot_vehicle/blob/master/extras/gazebo.png">
  <br><b>Fig: Robot in Gazebo</b><br>
</p>

Use i, j, k, l as arrow keys to navigate the world using my_robot. q and z increases and decreases the velocity of the robot respectively.

To get the distance of the robot from the environment as well as their orientation and rotation, type in new terminal
```
rosrun robot_vehicle read_laser.py
``` 

To get the location of the robot, type
```
rostopic echo /tf
rostopic echo /cmd_vel
```

To run the robot to follow walls as well as avoid obstacles, type in a new terminal
```
rosrun robot_vehicle follow_wall.py
```
