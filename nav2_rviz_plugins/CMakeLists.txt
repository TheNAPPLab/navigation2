cmake_minimum_required(VERSION 3.8)
project(nav2_rviz_plugins)

find_package(ament_cmake REQUIRED)
find_package(backward_ros REQUIRED)
find_package(geometry_msgs REQUIRED)
<<<<<<< HEAD
find_package(nav2_common REQUIRED)
=======
find_package(nav2_route REQUIRED)
find_package(nav2_util REQUIRED)
>>>>>>> jazzy
find_package(nav2_lifecycle_manager REQUIRED)
find_package(nav2_msgs REQUIRED)
find_package(nav2_util REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(nav2_route REQUIRED)
find_package(pluginlib REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(rviz_common REQUIRED)
find_package(rviz_default_plugins REQUIRED)
find_package(rviz_ogre_vendor REQUIRED)
find_package(rviz_rendering REQUIRED)
find_package(std_msgs REQUIRED)
find_package(tf2_geometry_msgs REQUIRED)
find_package(visualization_msgs REQUIRED)
find_package(nav2_ros_common REQUIRED)
find_package(yaml_cpp_vendor REQUIRED)
find_package(yaml-cpp REQUIRED)

# In Kilted and older distros, rviz with Qt6 is not supported
if(TARGET Qt5::Core)
  set(QT_VERSION_MAJOR 5)
  set(QT_VERSION ${Qt5Core_VERSION})
  # In Qt5, state machine is part of core
  find_package(Qt5 REQUIRED COMPONENTS Core Gui Widgets Test Concurrent)
elseif(TARGET Qt6::Core)
  set(QT_VERSION_MAJOR 6)
  set(QT_VERSION ${Qt6Core_VERSION})
  find_package(Qt6 REQUIRED COMPONENTS Core Gui Widgets StateMachine Test Concurrent)
endif()
if(${QT_VERSION} VERSION_LESS 5.15.0)
  function(qt_wrap_cpp out)
    qt5_wrap_cpp(_sources ${ARGN})
    set("${out}" ${_sources} PARENT_SCOPE)
  endfunction()
  function(qt_wrap_ui out)
      qt5_wrap_ui(_uis_hdrs ${ARGN})
      set("${out}" ${_uis_hdrs} PARENT_SCOPE)
  endfunction()
endif()

set(QT_LIBRARIES
  Qt${QT_VERSION_MAJOR}::Core
  Qt${QT_VERSION_MAJOR}::Gui
  Qt${QT_VERSION_MAJOR}::Widgets
)
if(QT_VERSION_MAJOR EQUAL 6)
  list(APPEND QT_LIBRARIES Qt6::StateMachine)
endif()

nav2_package()

# We specifically don't turn on CMAKE_AUTOMOC, since it generates one huge
# mocs_compilation.cpp file that takes a lot of memory to compile.  Instead
# we create individual moc files that can be compiled separately.
set(nav2_rviz_plugins_headers_to_moc
  include/nav2_rviz_plugins/costmap_cost_tool.hpp
  include/nav2_rviz_plugins/docking_panel.hpp
  include/nav2_rviz_plugins/goal_pose_updater.hpp
  include/nav2_rviz_plugins/goal_tool.hpp
  include/nav2_rviz_plugins/nav2_panel.hpp
  include/nav2_rviz_plugins/route_tool.hpp
  include/nav2_rviz_plugins/selector.hpp
<<<<<<< HEAD
  include/nav2_rviz_plugins/particle_cloud_display/particle_cloud_display.hpp
)

foreach(header "${nav2_rviz_plugins_headers_to_moc}")
  qt_wrap_cpp(nav2_rviz_plugins_moc_files "${header}")
endforeach()

qt_wrap_ui(route_tool_UIS_H resource/route_tool.ui)

# Qt5 boilerplate options from http://doc.qt.io/qt-5/cmake-manual.html
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)
=======
  include/nav2_rviz_plugins/utils.hpp
  include/nav2_rviz_plugins/particle_cloud_display/flat_weighted_arrows_array.hpp
  include/nav2_rviz_plugins/particle_cloud_display/particle_cloud_display.hpp
)

qt_wrap_ui(route_tool_UIS_H resource/route_tool.ui)

include_directories(
  include
)
>>>>>>> jazzy

set(library_name ${PROJECT_NAME})

add_library(${library_name} SHARED
  src/costmap_cost_tool.cpp
  src/docking_panel.cpp
  src/goal_tool.cpp
  src/nav2_panel.cpp
  src/route_tool.cpp
  src/selector.cpp
  src/utils.cpp
  src/particle_cloud_display/flat_weighted_arrows_array.cpp
  src/particle_cloud_display/particle_cloud_display.cpp
<<<<<<< HEAD
  ${nav2_rviz_plugins_moc_files}
  ${route_tool_UIS_H}
)
=======
  ${nav2_rviz_plugins_headers_to_moc}
  ${route_tool_UIS_H}
)

set(dependencies
  geometry_msgs
  nav2_route
  nav2_util
  nav2_lifecycle_manager
  nav2_msgs
  nav_msgs
  pluginlib
  Qt5
  rclcpp
  rclcpp_lifecycle
  rviz_common
  rviz_default_plugins
  rviz_ogre_vendor
  rviz_rendering
  std_msgs
  tf2_geometry_msgs
  yaml_cpp_vendor
)

ament_target_dependencies(${library_name}
  ${dependencies}
)

>>>>>>> jazzy
target_include_directories(${library_name} PUBLIC
  ${OGRE_INCLUDE_DIRS}
<<<<<<< HEAD
  "$<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>"
  "$<INSTALL_INTERFACE:include/${PROJECT_NAME}>"
=======
  ${nav2_route_INCLUDE_DIRS}
>>>>>>> jazzy
)
target_link_libraries(${library_name} PUBLIC
  ${geometry_msgs_TARGETS}
  nav2_lifecycle_manager::nav2_lifecycle_manager_core
  ${nav2_msgs_TARGETS}
  nav2_util::nav2_util_core
  nav2_ros_common::nav2_ros_common
  nav2_route::route_server_core
  rclcpp::rclcpp
  rclcpp_action::rclcpp_action
  rviz_common::rviz_common
<<<<<<< HEAD
  rviz_default_plugins::rviz_default_plugins
  rviz_rendering::rviz_rendering
  ${std_msgs_TARGETS}
  tf2_geometry_msgs::tf2_geometry_msgs
  ${visualization_msgs_TARGETS}
  ${QT_LIBRARIES}
)
target_link_libraries(${library_name} PRIVATE
  pluginlib::pluginlib
  yaml-cpp::yaml-cpp
=======
  nav2_route::route_server_core
>>>>>>> jazzy
)

pluginlib_export_plugin_description_file(rviz_common plugins_description.xml)

install(
  TARGETS ${library_name}
  EXPORT ${library_name}
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)

install(
  DIRECTORY include/
  DESTINATION include/${PROJECT_NAME}
)

install(
  DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/icons"
<<<<<<< HEAD
  DESTINATION "share/${PROJECT_NAME}"
)

install(DIRECTORY rviz launch DESTINATION share/${PROJECT_NAME})
=======
            "${CMAKE_CURRENT_SOURCE_DIR}/resource"
            "${CMAKE_CURRENT_SOURCE_DIR}/rviz"
            "${CMAKE_CURRENT_SOURCE_DIR}/launch"
  DESTINATION "share/${PROJECT_NAME}"
)

>>>>>>> jazzy

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_export_include_directories(include/${PROJECT_NAME})
ament_export_targets(${library_name} HAS_LIBRARY_TARGET)
ament_export_dependencies(
  geometry_msgs
  nav2_lifecycle_manager
  nav2_msgs
  nav2_route
  nav2_util
  Qt${QT_VERSION_MAJOR}
  rclcpp
<<<<<<< HEAD
  rclcpp_action
  rviz_common
  rviz_default_plugins
  rviz_rendering
  std_msgs
  tf2_geometry_msgs
  nav2_ros_common
  visualization_msgs
=======
  nav2_route
>>>>>>> jazzy
)

ament_package()
