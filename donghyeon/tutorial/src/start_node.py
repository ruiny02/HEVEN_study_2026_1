#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import random
from tutorial.msg import FirstMsg

class StartNode(Node):
    def __init__(self):
        super().__init__('start_node')
        self.publisher_ = self.create_publisher(FirstMsg, 'first_topic', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.count = 1

    def timer_callback(self):
        msg = FirstMsg()
        msg.start_time = self.get_clock().now().to_msg()
        msg.msg_seq = self.count
        msg.original_num = random.randint(1, 100)

        self.get_logger().info("------")
        self.get_logger().info(f"Start Time(sec): {msg.start_time.sec}")
        self.get_logger().info(f"Message Sequence: {msg.msg_seq}")
        self.get_logger().info(f"Original Number: {msg.original_num}")

        self.publisher_.publish(msg)
        self.count += 1

def main(args=None):
    rclpy.init(args=args)
    node = StartNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()