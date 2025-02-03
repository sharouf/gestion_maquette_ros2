import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random


class VitesseVentPublisher(Node):

    def __init__(self):
        super().__init__('vitesse_vent_publisher')
        self.publisher_ = self.create_publisher(Float32, 'vitesse_vent', 10)
        timer_period = 2.0  
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = Float32()
        msg.data = random.uniform(4.0, 27.0)  
        self.publisher_.publish(msg)
        self.get_logger().info(f'Vitesse du vent : {msg.data:.2f} km/h')


def main(args=None):
    rclpy.init(args=args)
    vitesse_vent_publisher = VitesseVentPublisher()
    rclpy.spin(vitesse_vent_publisher)
    vitesse_vent_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()



