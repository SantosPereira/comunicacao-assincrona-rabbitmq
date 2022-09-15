const mongoose = require("mongoose");
const Usuario = require("./models/model.js");

function teste(msg) {
	console.log(`\t${msg.content.toString()}`);
}

function connect() {
	mongoose.connect("mongodb://localhost:27017/microsservico", {
		useNewUrlParser: true,
		useUnifiedTopology: true,
	});
	const db = mongoose.connection;
	db.on("error", console.error.bind(console, "connection error: "));
	db.once("open", function () {
		console.log("Conexão com o banco de dados realizada com sucesso");
	});
}

function save(msg) {
	console.log(msg);
    const usuario = new Usuario({
        nome: msg.nome,
        idade: msg.idade,
    });
    usuario.save().then(() => console.log("Usuario salvo com sucesso"));
}

module.exports = {
	teste,
	connect,
    save,
};
