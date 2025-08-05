import rclpy
from rclpy.node import Node
import random
from example_interfaces.msg import String # The NEW import
from kitchen_interfaces.srv import OrderStatus

class WaiterNode(Node):
    def __init__(self):
        super().__init__('waiter_node')
        # Create a publisher at '/new_orders' topic
        self.publisher_ = self.create_publisher(String, 'new_orders', 10) 
        timer_period = 1.0
        self._order_number = 1
        self.menu = ['Pizza', 'Pasta', 'Burger'] # Menu list to choose from
        self.timer = self.create_timer(timer_period, self.timer_callback) # timer instance to publishe after a given interval
        
        '''
        TASK 1
        '''

        self.subscription = self.create_subscription(
            String,
            'completed_orders',
            self.listener_callback,
            10)
        self.client_ = self.create_client(OrderStatus, 'order_status')

        # Every 5 seconds we'd just ask the chef if an order is ready or not!
        self.client_timer = self.create_timer(5.0, self.client_timer_callback)

    def listener_callback(self, msg):
        self.get_logger().info(f'Picking Order: "{msg.data}"!')

        
    def timer_callback(self):
        msg = String()
        msg.data = f'Order #{self._order_number}: {random.choice(self.menu)}' # Adding data inside the msg block
        self.publisher_.publish(msg) # Trigger publish to the topic
        self._order_number += 1
        self.get_logger().info(f'Publishing: "{msg.data}"')

    '''
    TASK 2
    '''

    def send_order_status_request(self, order_number):
        while not self.client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('Service not available, waiting again...')

        request = OrderStatus.Request()
        request.order_number = order_number

        future = self.client_.call_async(request)
        future.add_done_callback(self.order_status_response_callback)

    def order_status_response_callback(self, future):
        try:
            response = future.result()
            if response.status:
                self.get_logger().info(f"Order is ready!")
            else:
                self.get_logger().warn(f"Order is under preparation")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")

    def client_timer_callback(self):
        self.send_order_status_request(self._order_number - 3) # Just some previously placed order

def main(args=None):
    rclpy.init(args=args)
    node = WaiterNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
