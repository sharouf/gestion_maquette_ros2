import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Bool


class ControleLED(Node):

    def __init__(self):
        super().__init__('controle_led_subscriber')
        self.subscription = self.create_subscription(
            Float32,
            'vitesse_vent',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(Bool, 'commande_led', 10)

    def listener_callback(self, msg):
        led_allumee = msg.data > 20.0 
        led_msg = Bool()
        led_msg.data = led_allumee
        self.publisher_.publish(led_msg)
        if led_allumee:
            self.get_logger().info(f'Vitesse élevée ({msg.data} km/h) : LED ON')
        else:
            self.get_logger().info(f'Vitesse normale ({msg.data} km/h) : LED OFF')


def main(args=None):
    rclpy.init(args=args)
    controle_led_subscriber = ControleLED()
    rclpy.spin(controle_led_subscriber)
    controle_led_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

