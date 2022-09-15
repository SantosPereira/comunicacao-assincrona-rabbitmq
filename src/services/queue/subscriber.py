# subscriber.py
import pika
import sys

config = {'host': 'localhost', 'port': 5672, 'exchange': 'my_exchange'}

class Subscriber:
    def __init__(self, queueName, bindingKey, config):
        self.queueName = queueName
        self.bindingKey = bindingKey
        self.config = config
        self.connection = self._create_connection()


    def __del__(self):
        self.connection.close()


    def _create_connection(self):
        parameters = pika.ConnectionParameters(host=self.config['host'],
                                               port=self.config['port'])
        return pika.BlockingConnection(parameters)


    def on_message_callback(self, channel, method, properties, body):
        binding_key = method.routing_key
        print('\n\nNova mensagem recebida de ~~> ' + binding_key)
        print(str(body, encoding='utf-8'))


    def setup(self):
        channel = self.connection.channel()
        channel.exchange_declare(exchange=self.config['exchange'], exchange_type='topic')      # This method creates or checks a queue
        channel.queue_declare(queue=self.queueName)
        # Binds the queue to the specified exchang
        channel.queue_bind(queue=self.queueName, exchange=self.config['exchange'], routing_key=self.bindingKey)
        channel.basic_consume(queue=self.queueName,on_message_callback=self.on_message_callback, auto_ack=True)
        print(f'\n\n\n[*] Esperando dados de {self.queueName}. Pressione CTRL+C para sair\n\n')
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()


# if len(sys.argv) < 2:
#     print('Usage: ' + __file__ + ' <QueueName > <BindingKey >')
#     sys.exit()
# else:
#     # queueName = sys.argv[1]
#     queueName = 'meu_topico'+'_queue'
#     # key in the form exchange.*
#     # key = sys.argv[2]
#     key = 'meu_topico' + '.*'
#     subscriber = Subscriber(queueName, key, config)
#     subscriber.setup()

queueName = 'meu_topico'+'_queue'
# key in the form exchange.*
# key = sys.argv[2]
key = 'meu_topico' + '.*'
subscriber = Subscriber(queueName, key, config)
subscriber.setup()
