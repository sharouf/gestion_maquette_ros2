from flask import Flask, render_template, request
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from example_interfaces.srv import SetBool

app = Flask(__name__)


rclpy.init()
node = rclpy.create_node('flask_interface')
client_ventilateur = node.create_client(SetBool, 'controle_ventilateur')

def send_request(command):

    while not client_ventilateur.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('"controle_ventilateur"')

    req = SetBool.Request()
    req.data = command  # True = ON, False = OFF
    future = client_ventilateur.call_async(req)
    rclpy.spin_until_future_complete(node, future)
    return future.result().message

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():

    action = request.form.get('action')

    if action == "on":
        message = send_request(True)  
    elif action == "off":
        message = send_request(False)  
    else:
        message = "Commande invalide"

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
