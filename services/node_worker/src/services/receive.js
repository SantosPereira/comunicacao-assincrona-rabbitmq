var amqp = require("amqplib/callback_api");
var mongo_access = require("../mongo_access.js");

function receive() {
	amqp.connect("amqp://localhost", function (error0, connection) {
		if (error0) {
			throw error0;
		}
		connection.createChannel(function (error1, channel) {
			if (error1) {
				throw error1;
			}
			var queue = "meu_topico_queue";

			channel.assertQueue(queue, {
				durable: false,
			});

			console.log(`[*] Esperando por mensagens na fila ${queue}`);
			channel.consume(
				queue,
				function (msg) {
					console.log(
						`\n\n\t[x] Mensagem recebida: ${msg.content.toString()}`
					);
					// mongo_access.teste(msg);
					mongo_access.connect();
					mongo_access.save(JSON.parse(msg.content.toString()));
				},
				{
					noAck: true,
				}
			);
		});
	});
}

module.exports = {
	receive,
};
