import rclpy
from rclpy.node import Node
class PersonNode(Node):
    def __init__(self, node_name: str,name: str, age: int) -> None:
        super().__init__(node_name)
        print('PersonNode 的__init__方法被调用了')
        self.name = name
        self.age = age

    def __str__(self):
        return f"PersonNode(name={self.name}, age={self.age})"
    
    def eat(self, food_name: str) :
        self.get_logger().info(f'我叫{self.name}，今年{self.age}岁，我现在正在吃{food_name}。')

def main():
        rclpy.init()
        node = PersonNode('person_node', '小明', 20)
        node.eat('鱼香肉丝')
        rclpy.spin(node)
        rclpy.shutdown()