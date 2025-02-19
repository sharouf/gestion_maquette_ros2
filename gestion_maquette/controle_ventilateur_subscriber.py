import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, Bool
from example_interfaces.srv import SetBool 

class ControleVentilateur(Node):

    def __init__(self):
        super().__init__('controle_ventilateur_subscriber')


        self.subscription = self.create_subscription(
            Float32,
            'temperature',
            self.listener_callback,
            10)

        self.publisher_ = self.create_publisher(Bool, 'commande_ventilateur', 10)

        # Service pour contrôle manuel du ventilateur
        self.srv = self.create_service(SetBool, 'controle_ventilateur', self.service_callback)

        self.ventilateur_par_temperature = False
        self.ventilateur_par_service = None  

        self.get_logger().info('Contrôle du ventilateur initialisé.')

    def listener_callback(self, msg):
        self.ventilateur_par_temperature = msg.data > 30.0
        self.update_ventilateur_state()

    def service_callback(self, request, response):
        """ Contrôle via service """
        self.ventilateur_par_service = request.data  
        self.update_ventilateur_state()

        response.success = True
        response.message = "Ventilateur ON" if self.ventilateur_par_service else "Ventilateur OFF"
        self.get_logger().info(f'Commande service : {response.message}')
        return response

    def update_ventilateur_state(self):
        """ état du ventilateur """
        if self.ventilateur_par_service is not None:
            ventilateur_active = self.ventilateur_par_service
        else:
            ventilateur_active = self.ventilateur_par_temperature

        fan_msg = Bool()
        fan_msg.data = ventilateur_active
        self.publisher_.publish(fan_msg)

        # Affichage de l’état actuel
        if ventilateur_active:
            self.get_logger().info('Ventilateur ON')
        else:
            self.get_logger().info('Ventilateur OFF')


def main(args=None):
    rclpy.init(args=args)
    node = ControleVentilateur()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

