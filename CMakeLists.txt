cmake_minimum_required(VERSION 2.8.3)
project(robot_vehicle)

# Compile as C++11, supported in ROS Kinetic
# add_compile_options(-std=c++1)

# Find catkin and any catkin packages
find_package(
  catkin REQUIRED COMPONENTS 
  roscpp
  urdf
  sensor_msgs
  geometry_msgs
)

# Declare a catkin package
catkin_package(
	INCLUDE_DIRS
	CATKIN_DEPENDS roscpp geometry_msgs
	DEPENDS
)

# Build target library
include_directories( 
  include
  ${catkin_INCLUDE_DIRS})

install(PROGRAMS
  scripts/keyboard_teleop
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

# Build algo and main
# add_executable(robot_vehicle scripts/keyboard.cpp)
# target_link_libraries(robot_vehicle ${catkin_LIBRARIES})
