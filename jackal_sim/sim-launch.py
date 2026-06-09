import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # 1. Clearpath Simulation Launch
    clearpath_sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('clearpath_gz'), 'launch', 'simulation.launch.py')
        )
    )

    # 2. Static Transform Publisher: j100_0288/odom -> camera_init
    tf_odom_to_camera_init = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='tf_odom_to_camera_init',
        arguments=[
            '--x', '0', '--y', '0', '--z', '0', 
            '--yaw', '0', '--pitch', '0', '--roll', '0', 
            '--frame-id', 'j100_0288/odom', 
            '--child-frame-id', 'camera_init'
        ]
    )

    # 3. Static Transform Publisher: body -> j100_0288/base_link
    tf_body_to_base_link = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='tf_body_to_base_link',
        arguments=[
            '--x', '0', '--y', '0', '--z', '0', 
            '--yaw', '0', '--pitch', '0', '--roll', '0', 
            '--frame-id', 'body', 
            '--child-frame-id', 'j100_0288/base_link'
        ]
    )

    # 4. FAST_LIO Mapping Node
    # Expand the '~' to the absolute path of the user's home directory
    fast_lio_config_path = os.path.expanduser('~/fast_lio2/src/FAST_LIO/config/velodyne.yaml')
    
    fast_lio_node = Node(
        package='fast_lio',
        executable='fastlio_mapping',
        name='fastlio_mapping',
        parameters=[
            {'use_sim_time': True},
            fast_lio_config_path
        ],
        remappings=[
            ('/Odometry', '/j100_0288/odom')
        ]
    )

    # 5. Nav2 Bringup Launch
    nav2_bringup_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('nav2_bringup'), 'launch', 'bringup_launch.py')
        ),
        launch_arguments={'use_sim_time': 'True',
                        'use_localization': 'False'}.items()
    )

    # Combine everything into the LaunchDescription
    return LaunchDescription([
        clearpath_sim_launch,
        tf_odom_to_camera_init,
        tf_body_to_base_link,
        fast_lio_node,
        nav2_bringup_launch
    ])