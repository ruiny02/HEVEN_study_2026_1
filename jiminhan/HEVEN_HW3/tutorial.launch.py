from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # 첫 번째 노드: 
        Node(
            package='tutorial',
            executable='start_node.py',
            name='start_node', 
            output='screen'
        ),
        # 두 번째 노드: 
        Node(
            package='tutorial',
            executable='middle_node.py',
            name='middle_node', 
            output='screen'
        ),
        # 세 번째 노드: 
        Node(
            package='tutorial',
            executable='end_node.py',
            name='end_node', 
            output='screen'
        ),
    ])
