const mongoose = require("mongoose");

const UsuarioSchema = new mongoose.Schema({
  nome: {
    type: String,
    required: true,
  },
  idade: {
    type: Number,
    default: 0,
  },
});

const Usuario = mongoose.model("Usuario", UsuarioSchema);

module.exports = Usuario;