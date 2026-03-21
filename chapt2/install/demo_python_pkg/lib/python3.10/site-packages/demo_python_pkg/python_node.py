import rclpy
from rclpy.node import Node


def main():
    rclpy.init()
    node = Node('python_node')
    node.get_logger().info('你好python节点！')
    rclpy.spin(node)
    # node.destroy_node()
    rclpy.shutdown()