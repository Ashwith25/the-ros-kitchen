import rclpy
from rclpy.node import Node
# Import our custom Service interface
import time 
from kitchen_interfaces.srv import Restock

class ManagerNode(Node):
    def __init__(self):
        super().__init__('manager_node')
        # Create the service server at 'restock_supplies'
        self.service_ = self.create_service(
            Restock, # The type of interface
            'restock_supplies',
            self.restock_callback)
        self.get_logger().info("The manager is ready to handle restock requests.")

    def restock_callback(self, request, response):
        # This function is called when a request is received
        self.get_logger().info(f'Restock request received for: {request.ingredient}')
        
        time.sleep(3) # Simulating the time the server might take to execute the action
        
        # We process the request and set the response
        response.success = True # In a real robot, we'd do more here
        
        return response

def main(args=None):
    rclpy.init(args=args)
    node = ManagerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()