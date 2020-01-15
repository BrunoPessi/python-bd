import pymongo


class MongoConnection():
    def __init__(self):
        try:
            self.client = pymongo.MongoClient("localhost", 27017)
            self.estoque = self.client["estoque"]
            self.produto = self.estoque["produto"]
            # Login padrao do MongoDB, database 'estoque' e collection 'produto'
        except Exception as e:
            print(f"Erro ao estabelecer conexão: {e}")

    def db_save(self, json):
        try:
            produto_id = self.produto.insert_one(json).insert_id
            print(produto_id)
        except Exception as e:
            print(f"Erro ao salvar registro: {e} \n {json}")

    def db_read(self, query=None, projection=None):
        for prd in self.produto.find(query, projection):
            print(prd)

    def db_update(self, query, field):
        self.produto.update(query, field)

    def db_remove(self, query):
        self.produto.remove(query)
