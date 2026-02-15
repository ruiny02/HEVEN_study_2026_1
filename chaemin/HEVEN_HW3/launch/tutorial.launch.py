from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    # 1. end_node (먼저 실행)
    end_node = Node(
        package='tutorial',
        executable='end_node.py',
        name='end_node',
        output='screen'
    )

    # 2. middle_node
    middle_node = Node(
        package='tutorial',
        executable='middle_node.py',
        name='middle_node',
        output='screen'
    )

    # 3. start_node (마지막 실행)
    start_node = Node(
        package='tutorial',
        executable='start_node.py',
        name='start_node',
        output='screen'
    )

    # 실행 순서: end → middle → start
    return LaunchDescription([
        end_node,
        middle_node,
        start_node
    ])
