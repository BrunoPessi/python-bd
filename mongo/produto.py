from mongo.conexao import MongoConnection


class Produto():
    def __init__(self):
        self.conexao = MongoConnection()

    def save(self, nome, descricao, preco, quantidade):
        self.conexao.db_save({
            "nome": nome,
            "descricao": descricao,
            "preco": preco,
            "quantidade": quantidade
        })

    def update(self, query, field):
        self.conexao.db_update(query, field)

    def remove(self, query):
        self.conexao.db_remove(query)

    def read(self, query=None, projection=None):
        self.conexao.db_read(query, projection)
