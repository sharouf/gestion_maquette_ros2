import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Bool

class ControleDeshumidificateur(Node):

    def __init__(self):
        super().__init__('controle_deshumidificateur')
        self.subscription = self.create_subscription(
            Float32,
            'humidite',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(Bool, 'commande_deshumidificateur', 10)

    def listener_callback(self, msg):
        deshumidificateur_active = msg.data > 80.0 
        deshumidificateur_msg = Bool()
        deshumidificateur_msg.data = deshumidificateur_active
        self.publisher_.publish(deshumidificateur_msg)

        if deshumidificateur_active:
            self.get_logger().info(f'Humidité haute ({msg.data:.2f}%) : Déshumidificateur ON')
        else:
            self.get_logger().info(f'Humidité normale ({msg.data:.2f}%) : Déshumidificateur OFF')

def main(args=None):
    rclpy.init(args=args)
    node = ControleDeshumidificateur()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

