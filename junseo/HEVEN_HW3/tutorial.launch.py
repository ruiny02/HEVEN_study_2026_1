import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    start_node = Node(
        package='py_pubsub',
        executable='start_node',
        name='start_node',
        output='screen'
    )

    middle_node = Node(
        package='py_pubsub',
        executable='middle_node',
        name='middle_node',
        output='screen'
    )

    end_node = Node(
        package='py_pubsub',
        executable='end_node',
        name='end_node',
        output='screen'
    )

    ld = LaunchDescription()

    ld.add_action(end_node)
    ld.add_action(middle_node)
    ld.add_action(start_node) 


    return ld