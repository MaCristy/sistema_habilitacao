from flask import Flask, request, jsonify
import services
import json
import os

app = Flask(__name__)

# Pasta de upload das imagens
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "Bem vindos à API de Cadastro de Habilitações"


#CREATE
@app.route("/habilitacoes", methods=["POST"])
def criar_habilitacao():
    try:
        dados = request.get_json()
        habilitacao = services.adicionar_habilitacao(dados)
        return app.response_class(
            # Adicionando a habilitação criada ao corpo da resposta
            response=json.dumps(habilitacao, indent=4, ensure_ascii=False, sort_keys=False),
            status=201,
            mimetype="application/json"
        )# Retornando a habilitação criada como JSON
    except ValueError as e:
        return jsonify({"erro": str(e)}), 400

#READ
@app.route("/habilitacoes", methods=["GET"])
def listar_habilitacoes():
    habilitacoes = services.listar_habilitacoes() # Retornando a lista de habilitações como JSON
    return app.response_class( 
        response=json.dumps({
            "quantidade_total": len(habilitacoes),
            "habilitacoes": habilitacoes
        }, indent=4, ensure_ascii=False, sort_keys=False),
        status=200,
        mimetype="application/json"
    ) #Retornando a lista de habilitações como JSON


#UPDATE
@app.route("/habilitacoes/<int:habilitacao_id>", methods=["PUT"])
def atualizar_habilitacao(habilitacao_id):
    try:
        dados = request.get_json()
        habilitacao = services.atualizar_habilitacao(habilitacao_id, dados)
        return jsonify(habilitacao)
    except IndexError as e:
        return jsonify({"erro": str(e)}), 404


#DELETE
@app.route("/habilitacoes/<int:habilitacao_id>", methods=["DELETE"])
def deletar_habilitacao(habilitacao_id):
    try:
        habilitacao = services.deletar_habilitacao(habilitacao_id)
        return jsonify({
            "mensagem": "Habilitação removida com sucesso!",
            "habilitacao": habilitacao
        })
    except IndexError as e:
        return jsonify({"erro": str(e)}), 404

# UPLOAD DE FOTO
@app.route("/habilitacoes/<int:habilitacao_id>/foto", methods=["POST"])
def upload_foto(habilitacao_id):
    if "foto" not in request.files:
        return jsonify({"erro": "Nenhuma imagem enviada. Use o campo 'foto'."}), 400

    foto = request.files["foto"]

    if foto.filename == "":
        return jsonify({"erro": "Arquivo inválido."}), 400

    caminho = os.path.join(UPLOAD_FOLDER, foto.filename)
    foto.save(caminho)

    habilitacao = services.adicionar_foto(habilitacao_id, caminho)

    return jsonify({
        "mensagem": "Foto enviada com sucesso!",
        "habilitacao": habilitacao
    })

from flask import send_from_directory

@app.route('/uploads/<path:filename>')
def get_uploaded_file(filename):
    return send_from_directory('uploads', filename)

    

if __name__ == "__main__":
    app.run(debug=True, port=5000)