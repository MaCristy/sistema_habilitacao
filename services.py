import model as models
from model import Habilitacao


def listar_habilitacoes():
    return models.listar()


def adicionar_habilitacao(dados):
    campos_obrigatorios = [
        "nome_completo", "primeira_habilitacao", "data_nascimento", "local_nascimento",
        "uf_nascimento", "data_emissao", "validade", "acc", "identidade",
        "org_emissor", "uf_identidade", "cpf", "numero_registro",
        "categoria", "nacionalidade", "filiacao"
    ]

    for campo in campos_obrigatorios:
        if not dados.get(campo):
            raise ValueError(f"O campo '{campo}' é obrigatório.")

    habilitacao = Habilitacao(
        nome_completo=dados["nome_completo"],
        primeira_habilitacao=dados["primeira_habilitacao"],
        data_nascimento=dados["data_nascimento"],
        local_nascimento=dados["local_nascimento"],
        uf_nascimento=dados["uf_nascimento"],
        data_emissao=dados["data_emissao"],
        validade=dados["validade"],
        acc=dados["acc"],
        identidade=dados["identidade"],
        org_emissor=dados["org_emissor"],
        uf_identidade=dados["uf_identidade"],
        cpf=dados["cpf"],
        numero_registro=dados["numero_registro"],
        categoria=dados["categoria"],
        nacionalidade=dados["nacionalidade"],
        filiacao=dados["filiacao"]
    )

    return models.adicionar(habilitacao)


def atualizar_habilitacao(habilitacao_id, dados):
    if not models.buscar_por_id(habilitacao_id):
        raise IndexError("Habilitação não encontrada.")
    return models.atualizar(habilitacao_id, dados)


def deletar_habilitacao(habilitacao_id):
    h = models.deletar(habilitacao_id)
    if not h:
        raise IndexError("Habilitação não encontrada.")
    return h
