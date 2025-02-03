import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Bool


class ControleVentilateur(Node):

    def __init__(self):
        super().__init__('controle_ventilateur_subscriber')
        self.subscription = self.create_subscription(
            Float32,
            'temperature',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(Bool, 'commande_ventilateur', 10)

    def listener_callback(self, msg):
        ventilateur_active = msg.data > 30.0
        fan_msg = Bool()
        fan_msg.data = ventilateur_active
        self.publisher_.publish(fan_msg)
        if ventilateur_active:
            self.get_logger().info(f'Température élevée ({msg.data} °C) : Ventilateur ON')
        else:
            self.get_logger().info(f'Température normale ({msg.data} °C) : Ventilateur OFF')


def main(args=None):
    rclpy.init(args=args)
    controle_ventilateur_subscriber = ControleVentilateur()
    rclpy.spin(controle_ventilateur_subscriber)
    controle_ventilateur_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

