from collections import OrderedDict
import json
import os


DB_FILE = "cnhs.db"


class Habilitacao:
    _id_counter = 1  #contador estático para gerar IDs automáticos

    def __init__(self, nome_completo,primeira_habilitacao, data_nascimento,
    local_nascimento, uf_nascimento, data_emissao, validade, acc, identidade, org_emissor, uf_identidade, cpf, numero_registro, categoria, nacionalidade, filiacao):
        self.id = Habilitacao._id_counter
        self.nome_completo = nome_completo
        self.primeira_habilitacao = primeira_habilitacao
        self.data_nascimento = data_nascimento
        self.local_nascimento = local_nascimento
        self.uf_nascimento = uf_nascimento
        self.data_emissao = data_emissao
        self.validade = validade
        self.acc = acc
        self.identidade = identidade
        self.org_emissor = org_emissor
        self.uf_identidade = uf_identidade
        self.cpf = cpf
        self.numero_registro = numero_registro
        self.categoria = categoria
        self.nacionalidade = nacionalidade
        self.filiacao = filiacao
        Habilitacao._id_counter += 1

    #
    def to_dict(self): 
        return OrderedDict([
            ("id", self.id),
            ("nome_completo", self.nome_completo),
            ("primeira_habilitacao", self.primeira_habilitacao),
            ("data_nascimento", self.data_nascimento),
            ("local_nascimento", self.local_nascimento),
            ("uf_nascimento", self.uf_nascimento),
            ("data_emissao", self.data_emissao),
            ("validade", self.validade),
            ("acc", self.acc),
            ("identidade", self.identidade),
            ("org_emissor", self.org_emissor),
            ("uf_identidade", self.uf_identidade),
            ("cpf", self.cpf),
            ("numero_registro", self.numero_registro),
            ("categoria", self.categoria),
            ("nacionalidade", self.nacionalidade),
            ("filiacao", self.filiacao)
        ])


#Banco de dados em memória
habilitacoes = []


# Funções auxiliares para persistência
def _get_db_path():
    base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, DB_FILE)


def _salvar_db():
    """Salva habilitações em JSON no arquivo cnhs.db"""
    try:
        dados = [h.to_dict() for h in habilitacoes]
        with open(_get_db_path(), 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar DB: {e}")


def _carregar_db():
    """Carrega habilitações do arquivo cnhs.db"""
    global habilitacoes
    path = _get_db_path()
    if os.path.exists(path):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                habilitacoes = []
                max_id = 0
                for item in dados:
                    h = Habilitacao(
                        nome_completo=item.get("nome_completo"),
                        primeira_habilitacao=item.get("primeira_habilitacao"),
                        data_nascimento=item.get("data_nascimento"),
                        local_nascimento=item.get("local_nascimento"),
                        uf_nascimento=item.get("uf_nascimento"),
                        data_emissao=item.get("data_emissao"),
                        validade=item.get("validade"),
                        acc=item.get("acc"),
                        identidade=item.get("identidade"),
                        org_emissor=item.get("org_emissor"),
                        uf_identidade=item.get("uf_identidade"),
                        cpf=item.get("cpf"),
                        numero_registro=item.get("numero_registro"),
                        categoria=item.get("categoria"),
                        nacionalidade=item.get("nacionalidade"),
                        filiacao=item.get("filiacao")
                    )
                    h.id = item.get("id", 0)
                    habilitacoes.append(h)
                    if h.id > max_id:
                        max_id = h.id
                Habilitacao._id_counter = max_id + 1
        except Exception as e:
            print(f"Erro ao carregar DB: {e}")
            habilitacoes = []


#Banco de dados em memória
habilitacoes = []


#CRUD
#Funções de acesso aos dados
def listar():
    return [h.to_dict() for h in habilitacoes]


def adicionar(habilitacao: Habilitacao):
    habilitacoes.append(habilitacao)
    _salvar_db()
    return habilitacao.to_dict()


def buscar_por_id(habilitacao_id):
    for h in habilitacoes:
        if h.id == habilitacao_id:
            return h
    return None


def atualizar(habilitacao_id, dados):
    h = buscar_por_id(habilitacao_id)
    if h:
        for campo, valor in dados.items():
            if hasattr(h, campo):
                setattr(h, campo, valor)
        _salvar_db()
        return h.to_dict()
    return None


def deletar(habilitacao_id):
    h = buscar_por_id(habilitacao_id)
    if h:
        habilitacoes.remove(h)
        _salvar_db()
        return h.to_dict()
    return None


# Carrega dados ao iniciar o módulo
_carregar_db()
