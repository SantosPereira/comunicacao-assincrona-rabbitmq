# publisher.py
import pika


class Publisher:
    def __init__(self, config = {'host': 'localhost', 'port': 5672, 'exchange': 'my_exchange'}):
        self.config = config

    def publish(self, routing_key, message):
        # Create a new channel with the next available channel number
        # or pass in a channel number to use 
        connection = self.create_connection()
        # Creates an exchange if it does not already exist, and if
        # the exchange exists,
        # verifies that it is of the correct and expected class.
        channel = connection.channel()
        channel.exchange_declare(exchange=self.config['exchange'],
        exchange_type='topic')  # Publishes message to the exchange with the given routing key
        channel.basic_publish(exchange=self.config['exchange'],
        routing_key=routing_key, body=message)
        print(f'\n\n\n[*] Mensagem {message} enviada para {routing_key}\n\n')  # Create new connection
    
    def create_connection(self):
        param = pika.ConnectionParameters(host=self.config['host'], port=self.config['port']) 
        return pika.BlockingConnection(param)

