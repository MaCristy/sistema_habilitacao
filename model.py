from collections import OrderedDict


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


#CRUD
#Funções de acesso aos dados
def listar():
    return [h.to_dict() for h in habilitacoes]


def adicionar(habilitacao: Habilitacao):
    habilitacoes.append(habilitacao)
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
        return h.to_dict()
    return None


def deletar(habilitacao_id):
    h = buscar_por_id(habilitacao_id)
    if h:
        habilitacoes.remove(h)
        return h.to_dict()
    return None
