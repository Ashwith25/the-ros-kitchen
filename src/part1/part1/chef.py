import rclpy
from rclpy.node import Node
from example_interfaces.msg import String
from kitchen_interfaces.srv import Restock, OrderStatus
import time

class ChefNode(Node):
    def __init__(self):
        super().__init__('chef_node')
        # Create a subscriber to the '/new_orders' topic
        self.subscription = self.create_subscription(
            String,
            'new_orders',
            self.listener_callback,
            10)
        
        '''
            TASK 1

            Note: It is not necessary to exactly implement what I implemented here.
            The data on the topic can be anything of your wish!

        '''
        self.publisher_ = self.create_publisher(String, 'completed_orders', 10) 
        self.client_ = self.create_client(Restock, 'restock_supplies')
        self.service_ = self.create_service(
            OrderStatus, # The type of interface
            'order_status',
            self.order_status_callback)

    def listener_callback(self, msg):
        self.get_logger().info(f'Received Order: "{msg.data}"... Preparing it now!')
        
        time.sleep(2)
        msg1 = String()
        msg1.data = f'{msg.data} is ready!' # Adding data inside the msg block

        self.publisher_.publish(msg1)

        # Restock supplies supplies starting from 5th order and continuing every 10th order
        if '5' in msg.data:
            self.send_restock_request('tomatoes')

    def send_restock_request(self, ingredient):
        # Step 1: Wait for the service to be available
        while not self.client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('Service not available, waiting again...')

        # Step 2: Create the request object
        request = Restock.Request()
        request.ingredient = ingredient

        # Step 3: Call the service asynchronously and add a callback
        future = self.client_.call_async(request)
        future.add_done_callback(self.restock_response_callback)

    def restock_response_callback(self, future):
        # Step 4: Process the response once it's received
        try:
            response = future.result()
            if response.success:
                self.get_logger().info(f"Successfully restocked!")
            else:
                self.get_logger().warn(f"Failed to restock ingredient.")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")

    def order_status_callback(self, request, response):
            # This function is called when a request is received
            self.get_logger().info(f'Order Status request received for: {request.order_number}')
            
            # Do the necessary checks and then return the status
            response.status = 'Yes' # For now, we'll just say yes
            
            return response

def main(args=None):
    rclpy.init(args=args)
    node = ChefNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()