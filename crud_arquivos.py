import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Caminho da pasta onde os arquivos serão salvos (dentro do projeto)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

# Cria a pasta se não existir
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/upload", methods=["POST"])
def upload():
    # Verifica se veio um arquivo
    if "file" not in request.files:
        return jsonify(erro="Nenhum arquivo enviado"), 400

    arquivo = request.files["file"]

    # Verifica se o nome é válido
    if arquivo.filename == "":
        return jsonify(erro="Nenhum arquivo selecionado"), 400

    # Garante que o nome do arquivo é seguro
    nome_seguro = secure_filename(arquivo.filename)

    # Caminho completo onde o arquivo será salvo
    caminho_completo = os.path.join(app.config["UPLOAD_FOLDER"], nome_seguro)

    # Salva o arquivo fisicamente
    arquivo.save(caminho_completo)

    return jsonify(
        mensagem="Upload realizado com sucesso!",
        arquivo_salvo=nome_seguro,
        caminho=caminho_completo
    )

if __name__ == "__main__":
    app.run(debug=True)
