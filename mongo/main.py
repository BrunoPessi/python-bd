from mongo.produto import Produto

produtos = Produto()

produtos.save(
    nome="bola futebol Nike",
    descricao="430 gramas",
    preco="150",
    quantidade=12
)

produtos.save(
    nome="luvas boxe Everlast",
    descricao="14 Oz",
    preco="170",
    quantidade=10
)

print("Produtos: ")
#Lista apenas os produtos com preço acima de 160. Só listará as luvas de boxe
produtos.read({"preco":{"gte": 160}})
