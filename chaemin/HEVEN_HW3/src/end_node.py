#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from tutorial.msg import SecondMsg

class EndNode(Node):
    def __init__(self):
        super().__init__('end_node')
        self.subscription = self.create_subscription(
            SecondMsg, 
            'second_topic', 
            self.second_topic_callback, 
            10)

    def second_topic_callback(self, data):
        now = self.get_clock().now()
        
        start_time = rclpy.time.Time.from_msg(data.start_time)
        
        diff_ns = now.nanoseconds - start_time.nanoseconds

        self.get_logger().info("------")
        self.get_logger().info(f"Processing Time(nsec): {diff_ns}")
        self.get_logger().info(f"Message Sequence: {data.msg_seq}")

        self.get_logger().info(
            f"Original | Square | Square Root: {data.original_num} | {int(data.square_num)} | {data.sqrt_num:.2f}"
        )

def main(args=None):
    rclpy.init(args=args)
    node = EndNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()