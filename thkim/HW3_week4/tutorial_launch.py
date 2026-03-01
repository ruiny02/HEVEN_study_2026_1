import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 1. end_node 실행
        Node(
            package='tutorial',
            executable='end_node.py',
            name='end_node',
            output='screen'
        ),
        # 2. middle_node 실행
        Node(
            package='tutorial',
            executable='middle_node.py',
            name='middle_node',
            output='screen'
        ),
        # 3. start_node 실행
        Node(
            package='tutorial',
            executable='start_node.py',
            name='start_node',
            output='screen'
        )
    ])