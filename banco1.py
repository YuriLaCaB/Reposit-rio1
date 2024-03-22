import sqlite3


class Gestao:
    def __init__(self, banco):
        self.conn = sqlite3.connect(banco)
        self.criar_tabela_estoque()

    def criar_tabela_estoque(self):
        cursor = self.conn.cursor()
        cursor.execute(''' 
            CREATE TABLE IF NOT EXISTS estoque (
                id INTEGER PRIMARY KEY,
                produto TEXT,
                quantidade INTEGER
                )
            ''')
        self.conn.commit()

    def adicionar_produto(self, produto, quantidade):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO estoque (produto, quantidade) VALUES (?, ?)", (produto, quantidade))
        self.conn.commit()

    def remover_produto(self, produto, quantidade):
        cursor = self.conn.cursor()
        cursor.execute("SELECT quantidade FROM estoque WHERE produto=?", (produto,))
        resultado = cursor.fetchone()
        if resultado:
            estoque_atual = resultado[0]
            if estoque_atual >= quantidade:
               cursor.execute("UPDATE estoque SET quantidade=? WHERE produto=?",
                              (estoque_atual - quantidade, produto))
               self.conn.commit()
               #se tiver a quantidade de camisa em estoque for maior do que a quantidade a ser deletada vai fazer isso
            else:
                print(f"Quantidade insuficiente de {produto} em estoque")
                #se tiver 5 camisas vermelhas e quiserem apagar 10
        else:
            print(f"{produto} não encontado em estoque")
            #o produto não existe

    def consultar_estoque(self, produto):
        cursor = self.conn.cursor()
        cursor.execute("SELECT quantidade FROM estoque WHERE produto=?", (produto,))
        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]
        else:
            return 0

    def listar_produtos(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT produto FROM estoque")
        produtos = cursor.fetchall()
        return [produtos[0] for produto in produtos]

sistema = Gestao("estoque.db")

sistema.adicionar_produto("Chapeu verde", 33)
sistema.adicionar_produto("Calça jeans azul", 100)
sistema.adicionar_produto("Maquiagem", 10)

estoque_calça = sistema.consultar_estoque("Calça jeans azul")
print(f"Quantidade de Calça jeans em estoque {estoque_calça}")

sistema.remover_produto("Chapeu verde", 15)

produtos_em_estoque = sistema.listar_produtos()
print(f"Produtos em estoque: {produtos_em_estoque}")