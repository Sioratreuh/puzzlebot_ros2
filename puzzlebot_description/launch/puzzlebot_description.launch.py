
from launch import LaunchDescription
from launch_ros.actions import Node 

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='puzzlebot_description',
            executable='puzzlebot_description_node',
            name='puzzlebot_description_node',
            output='screen'
        )
    ])

