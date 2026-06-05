<<<<<<< HEAD
#! /usr/bin/env python3
# Copyright (c) 2019 Samsung Research America
=======
#!/usr/bin/env python3

# Copyright (c) 2025 Open Navigation LLC
>>>>>>> jazzy
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from pathlib import Path
import sys

from ament_index_python.packages import get_package_share_directory
<<<<<<< HEAD
from launch import LaunchDescription, LaunchService
from launch.actions import (AppendEnvironmentVariable, DeclareLaunchArgument, ExecuteProcess,
                            IncludeLaunchDescription, SetEnvironmentVariable)
=======
<<<<<<<< HEAD:nav2_system_tests/src/route/test_route_launch.py
from launch import LaunchDescription, LaunchService
from launch.actions import (AppendEnvironmentVariable, ExecuteProcess, IncludeLaunchDescription,
                            SetEnvironmentVariable)
from launch.launch_context import LaunchContext
========

from launch import LaunchDescription
from launch import LaunchService
from launch.actions import (
    AppendEnvironmentVariable,
    DeclareLaunchArgument,
    ExecuteProcess,
    IncludeLaunchDescription,
    SetEnvironmentVariable)
>>>>>>>> jazzy:nav2_system_tests/src/behaviors/spin/test_spin_behavior.launch.py
>>>>>>> jazzy
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch_testing.legacy import LaunchTestService
from nav2_common.launch import RewrittenYaml


<<<<<<< HEAD
def generate_launch_description() -> LaunchDescription:
    bringup_dir = get_package_share_directory('nav2_bringup')
    sim_dir = get_package_share_directory('nav2_minimal_tb3_sim')
    params_file = LaunchConfiguration('params_file')
=======
<<<<<<<< HEAD:nav2_system_tests/src/route/test_route_launch.py
def generate_launch_description() -> LaunchDescription:
    sim_dir = get_package_share_directory('nav2_minimal_tb3_sim')
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')

========
def generate_launch_description():
    bringup_dir = get_package_share_directory('nav2_bringup')
    sim_dir = get_package_share_directory('nav2_minimal_tb3_sim')
    params_file = LaunchConfiguration('params_file')
>>>>>>>> jazzy:nav2_system_tests/src/behaviors/spin/test_spin_behavior.launch.py
>>>>>>> jazzy
    world_sdf_xacro = os.path.join(sim_dir, 'worlds', 'tb3_sandbox.sdf.xacro')
    robot_sdf = os.path.join(sim_dir, 'urdf', 'gz_waffle.sdf.xacro')
    urdf = os.path.join(sim_dir, 'urdf', 'turtlebot3_waffle.urdf')
    with open(urdf, 'r') as infp:
        robot_description = infp.read()

<<<<<<< HEAD
    # Create our own temporary YAML files that include substitutions
    param_substitutions = {'use_sim_time': 'True'}
=======
<<<<<<<< HEAD:nav2_system_tests/src/route/test_route_launch.py
    map_yaml_file = os.path.join(nav2_bringup_dir, 'maps', 'tb3_sandbox.yaml')

    bt_navigator_xml = os.path.join(
        get_package_share_directory('nav2_bt_navigator'),
        'behavior_trees',
        os.getenv('BT_NAVIGATOR_XML', ''),
    )

    params_file = os.path.join(nav2_bringup_dir, 'params', 'nav2_params.yaml')
    graph_filepath = os.path.join(nav2_bringup_dir, 'graphs', 'turtlebot3_graph.geojson')

    # Replace the default parameter values for testing special features
    # without having multiple params_files inside the nav2 stack
    context = LaunchContext()
    param_substitutions = {}

    if os.getenv('ASTAR') == 'True':
        param_substitutions.update({'use_astar': 'True'})

    param_substitutions.update(
        {'planner_server.ros__parameters.GridBased.plugin': os.getenv('PLANNER', '')}
    )
    param_substitutions.update(
        {'controller_server.ros__parameters.FollowPath.plugin': os.getenv('CONTROLLER', '')}
    )
    param_substitutions.update(
        {'route_server.ros__parameters.max_planning_time': '0.0001'}
    )

========
    # Create our own temporary YAML files that include substitutions
    param_substitutions = {'use_sim_time': 'True'}
>>>>>>>> jazzy:nav2_system_tests/src/behaviors/spin/test_spin_behavior.launch.py
>>>>>>> jazzy
    configured_params = RewrittenYaml(
        source_file=params_file,
        root_key='',
        param_rewrites=param_substitutions,
<<<<<<< HEAD
=======
<<<<<<<< HEAD:nav2_system_tests/src/route/test_route_launch.py
>>>>>>> jazzy
        value_rewrites={
            'KEEPOUT_ZONE_ENABLED': 'False',
            'SPEED_ZONE_ENABLED': 'False',
        },
<<<<<<< HEAD
        convert_types=True,
    )

=======
========
>>>>>>>> jazzy:nav2_system_tests/src/behaviors/spin/test_spin_behavior.launch.py
        convert_types=True,
    )

    new_yaml = configured_params.perform(context)

>>>>>>> jazzy
    return LaunchDescription(
        [
            SetEnvironmentVariable('RCUTILS_LOGGING_BUFFERED_STREAM', '1'),
            SetEnvironmentVariable('RCUTILS_LOGGING_USE_STDOUT', '1'),
<<<<<<< HEAD
=======
<<<<<<<< HEAD:nav2_system_tests/src/route/test_route_launch.py
========
>>>>>>> jazzy
            DeclareLaunchArgument(
                'params_file',
                default_value=os.path.join(bringup_dir, 'params', 'nav2_params.yaml'),
                description='Full path to the ROS2 parameters file to use',
            ),
            # Simulation for odometry
<<<<<<< HEAD
=======
>>>>>>>> jazzy:nav2_system_tests/src/behaviors/spin/test_spin_behavior.launch.py
>>>>>>> jazzy
            AppendEnvironmentVariable(
                'GZ_SIM_RESOURCE_PATH', os.path.join(sim_dir, 'models')
            ),
            AppendEnvironmentVariable(
                'GZ_SIM_RESOURCE_PATH',
                str(Path(os.path.join(sim_dir)).parent.resolve())
            ),
            ExecuteProcess(
                cmd=['gz', 'sim', '-r', '-s', world_sdf_xacro],
                output='screen',
            ),
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(sim_dir, 'launch', 'spawn_tb3.launch.py')
                ),
                launch_arguments={
                    'use_sim_time': 'True',
                    'robot_sdf': robot_sdf,
                    'x_pose': '-2.0',
                    'y_pose': '-0.5',
                    'z_pose': '0.01',
                    'roll': '0.0',
                    'pitch': '0.0',
                    'yaw': '0.0',
                }.items(),
            ),
            # No need for localization
            Node(
                package='tf2_ros',
                executable='static_transform_publisher',
                output='screen',
                arguments=[
                    '--x', '0',
                    '--y', '0',
                    '--z', '0',
                    '--roll', '0',
                    '--pitch', '0',
                    '--yaw', '0',
                    '--frame-id', 'map',
                    '--child-frame-id', 'odom'
                ],
                parameters=[{'use_sim_time': True}],
            ),
            # Need transforms
            Node(
                package='robot_state_publisher',
                executable='robot_state_publisher',
                name='robot_state_publisher',
                output='screen',
                parameters=[
                    {'use_sim_time': True, 'robot_description': robot_description}
                ],
            ),
<<<<<<< HEAD
=======
<<<<<<<< HEAD:nav2_system_tests/src/route/test_route_launch.py
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(
                    os.path.join(nav2_bringup_dir, 'launch', 'bringup_launch.py')
                ),
                launch_arguments={
                    'namespace': '',
                    'use_namespace': 'False',
                    'map': map_yaml_file,
                    'graph': graph_filepath,
                    'use_sim_time': 'True',
                    'params_file': new_yaml,
                    'bt_xml_file': bt_navigator_xml,
                    'use_composition': 'False',
                    'autostart': 'True',
                }.items(),
========
>>>>>>> jazzy
            # Server under test
            Node(
                package='nav2_behaviors',
                executable='behavior_server',
                name='behavior_server',
                output='screen',
                parameters=[configured_params],
            ),
            Node(
                package='nav2_lifecycle_manager',
                executable='lifecycle_manager',
                name='lifecycle_manager_navigation',
                output='screen',
                parameters=[
                    {'use_sim_time': True},
                    {'autostart': True},
                    {'node_names': ['behavior_server']},
                ],
<<<<<<< HEAD
=======
>>>>>>>> jazzy:nav2_system_tests/src/behaviors/spin/test_spin_behavior.launch.py
>>>>>>> jazzy
            ),
        ]
    )


def main(argv: list[str] = sys.argv[1:]):  # type: ignore[no-untyped-def]
    ld = generate_launch_description()

    test1_action = ExecuteProcess(
<<<<<<< HEAD
        cmd=[os.path.join(
            os.getenv('TEST_DIR', ''),
            'spin_tester.py'), '--ros-args', '-p', 'use_sim_time:=True'],
=======
<<<<<<<< HEAD:nav2_system_tests/src/route/test_route_launch.py
        cmd=[
            os.path.join(os.getenv('TEST_DIR', ''), os.getenv('TESTER', '')),
            '-r',
            '-2.0',
            '-0.5',
            '2.0',
            '0.0',
            '-e',
            'True',
        ],
========
        cmd=[os.path.join(
            os.getenv('TEST_DIR'), 'spin_tester.py'), '--ros-args', '-p', 'use_sim_time:=True'],
>>>>>>>> jazzy:nav2_system_tests/src/behaviors/spin/test_spin_behavior.launch.py
>>>>>>> jazzy
        name='tester_node',
        output='screen',
    )

    lts = LaunchTestService()  # type: ignore[no-untyped-call]
    lts.add_test_action(ld, test1_action)  # type: ignore[no-untyped-call]
    ls = LaunchService(argv=argv)
    ls.include_launch_description(ld)
<<<<<<< HEAD
    return_code = lts.run(ls)  # type: ignore[no-untyped-call]
=======
<<<<<<<< HEAD:nav2_system_tests/src/route/test_route_launch.py
    return_code = lts.run(ls)  # type: ignore[no-untyped-call]
========
    return_code = lts.run(ls)
>>>>>>>> jazzy:nav2_system_tests/src/behaviors/spin/test_spin_behavior.launch.py
>>>>>>> jazzy
    return return_code


if __name__ == '__main__':
    sys.exit(main())
