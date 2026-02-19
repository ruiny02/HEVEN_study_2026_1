import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import SetEnvironmentVariable

def generate_launch_description():
    # 파이썬 출력 버퍼링을 강제로 해제하는 환경 변수 설정
    set_env_vars = SetEnvironmentVariable('PYTHONUNBUFFERED', '1')

    end_node = Node(
        package='tutorial',
        executable='end_node.py',
        name='end_node',
        output='screen',
        emulate_tty=True
    )

    middle_node = Node(
        package='tutorial',
        executable='middle_node.py',
        name='middle_node',
        output='screen',
        emulate_tty=True
    )

    start_node = Node(
        package='tutorial',
        executable='start_node.py',
        name='start_node',
        output='screen',
        emulate_tty=True
    )

    ld = LaunchDescription()

    # 환경 변수 설정을 최우선으로 액션에 추가합니다.
    ld.add_action(set_env_vars)
    ld.add_action(end_node)
    ld.add_action(middle_node)
    ld.add_action(start_node)

    return ld
