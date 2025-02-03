import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random  

class HumiditePublisher(Node):

    def __init__(self):
        super().__init__('humidite_publisher')
        self.publisher_ = self.create_publisher(Float32, 'humidite', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)  

    def timer_callback(self):
        msg = Float32()
        msg.data = random.uniform(40.0, 90.0) 
        self.publisher_.publish(msg)
        self.get_logger().info(f'Humidité : {msg.data:.2f} %')

def main(args=None):
    rclpy.init(args=args)
    node = HumiditePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

