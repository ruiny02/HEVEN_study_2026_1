from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    pkg_share = get_package_share_directory('tutorial')
    pkg_root = os.path.dirname(pkg_share)  # .../install/tutorial/share
    pkg_prefix = os.path.dirname(pkg_root) # .../install/tutorial

    start_py  = os.path.join(pkg_prefix, 'lib', 'tutorial', 'start_node.py')
    middle_py = os.path.join(pkg_prefix, 'lib', 'tutorial', 'middle_node.py')
    end_py    = os.path.join(pkg_prefix, 'lib', 'tutorial', 'end_node.py')

    return LaunchDescription([
        Node(
            package='tutorial',
            executable=start_py,
            name='start_node',
            output='screen'
        ),
        Node(
            package='tutorial',
            executable=middle_py,
            name='middle_node',
            output='screen'
        ),
        Node(
            package='tutorial',
            executable=end_py,
            name='end_node',
            output='screen'
        ),
    ])
