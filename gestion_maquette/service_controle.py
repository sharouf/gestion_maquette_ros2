import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool 
from std_msgs.msg import Bool  

class ServiceControleVentilateur(Node):

    def __init__(self):
        super().__init__('service_controle_ventilateur')


        self.srv = self.create_service(SetBool, 'controle_ventilateur', self.controle_ventilateur_callback)
        self.get_logger().info('service ROS2 "controle_ventilateur" ')

        self.publisher_ = self.create_publisher(Bool, 'commande_ventilateur', 10)

        self.ventilateur_etat = False

    def controle_ventilateur_callback(self, request, response):
        """ request obtenu """
        self.ventilateur_etat = request.data  

        ventilateur_msg = Bool()
        ventilateur_msg.data = self.ventilateur_etat
        self.publisher_.publish(ventilateur_msg)

        response.success = True
        response.message = "Ventilateur ON" if self.ventilateur_etat else "Ventilateur OFF"

        self.get_logger().info(f'Commande reçue : {response.message}')
        return response


def main(args=None):
    rclpy.init(args=args)
    node = ServiceControleVentilateur()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

