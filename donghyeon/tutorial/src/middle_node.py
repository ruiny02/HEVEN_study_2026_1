#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import math
from tutorial.msg import FirstMsg, SecondMsg

class MiddleNode(Node):
    def __init__(self):
        super().__init__('middle_node')
        self.subscription = self.create_subscription(
            FirstMsg, 
            'first_topic', 
            self.first_topic_callback, 
            10)
        
        self.publisher_ = self.create_publisher(SecondMsg, 'second_topic', 10)

    def first_topic_callback(self, data):
        msg = SecondMsg()
        msg.start_time = data.start_time
        msg.msg_seq = data.msg_seq
        msg.original_num = data.original_num
        
        msg.square_num = float(data.original_num ** 2)
        msg.sqrt_num = math.sqrt(data.original_num)

        self.get_logger().info("------")
        self.get_logger().info(f"Message Sequence: {msg.msg_seq}")
        self.get_logger().info(f"Original Number: {msg.original_num}")
        self.get_logger().info(f"Square Number: {msg.square_num}")
        self.get_logger().info(f"Square Root Number: {msg.sqrt_num:.2f}")

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MiddleNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()