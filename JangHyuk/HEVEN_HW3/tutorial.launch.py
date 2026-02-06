import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # 첫 번째 노드: 
    start_node = Node(
        package='tutorial',
        executable='start_node.py',
        name='start_node', 
        output='screen'
    )
    # 두 번째 노드: 
    middle_node = Node(
        package='tutorial',
        executable='middle_node.py',
        name='middle_node', 
        output='screen'
    )
    # 세 번째 노드: 
    end_node = Node(
        package='tutorial', 
        executable='end_node.py', 
        name='end_node',
        output='screen'
    )
    ld = LaunchDescription()

    ld.add_action(end_node)
    ld.add_action(middle_node)
    ld.add_action(start_node)
    return ld
