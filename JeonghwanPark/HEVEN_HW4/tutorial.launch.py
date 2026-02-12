from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    start_node = Node(
        package='tutorial',
        executable='start_node.py',
        name='start_node'
    )

    middle_node = Node(
        package='tutorial',
        executable='middle_node.py',
        name='middle_node'
    )

    end_node = Node(
        package='tutorial',
        executable='end_node.py',
        name='end_node'
    )

    return LaunchDescription([
        start_node,
        middle_node,
        end_node
    ])
