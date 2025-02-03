import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random  


class TemperaturePublisher(Node):

    def __init__(self):
        super().__init__('temperature_publisher')
        self.publisher_ = self.create_publisher(Float32, 'temperature', 10)
        timer_period = 2.0 
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        msg.data = random.uniform(-5.0, 35.0)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Température : {msg.data:.2f} °C')


def main(args=None):
    rclpy.init(args=args)
    temperature_publisher = TemperaturePublisher()
    rclpy.spin(temperature_publisher)
    temperature_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

