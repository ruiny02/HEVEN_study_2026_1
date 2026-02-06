from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hw4',
            executable='end_node',
            name='end_node',
            output='screen'
        ),
        Node(
            package='hw4',
            executable='middle_node',
            name='middle_node',
            output='screen'
        ),
        Node(
            package='hw4',
            executable='start_node',
            name='start_node',
            output='screen'
        ),
    ])