import rclpy
from rclpy.node import Node


def main():
    rclpy.init()
    node = Node('python_node')
    node.get_logger().info('Hello, ROS 2 from Python!')
    rclpy.spin(node)
    # node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

