import sqlite3

class comidas:
    def __init__(self, banco_comidas):
        self.banco = sqlite3.connect(banco_comidas)
        self.criar_tabela_comidas()

    def criar_tabela_comidas(self):
        cursor = self.banco.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS banco_de_dados_comida (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_comida TEXT NOT NULL,
                preço_comida INTEGER
            )
        ''')
        self.banco.commit()

    def adicionar_comidas(self, nome_comida, preço_comida):
        cursor = self.banco.cursor()
        cursor.execute("INSERT INTO banco_de_dados_comida (nome_comida, preço_comida) VALUES(?, ?)", (nome_comida, preço_comida))
        self.banco.commit()

    def remover_comidas(self, id):
        cursor = self.banco.cursor()
        cursor.execute("DELETE FROM banco_de_dados_comida WHERE id=?", (id,))
        self.banco.commit()

    def consultar_comidas(self):
        cursor = self.banco.cursor()
        cursor.execute("SELECT * FROM banco_de_dados_comida")
        resultado = cursor.fetchall()
        for res in resultado:
            print(f"Id: {res[0]}\nName: {res[1]}\nPrice: {res[2]}")
            print("=-="*20)

    def procurar_produto(self, id):
        cursor = self.banco.cursor()
        try:
            cursor.execute("SELECT * FROM banco_de_dados_comida WHERE id=?", (id,))
            resultado = cursor.fetchone()
            print(f"ID: {resultado[0]}\nName: {resultado[1]}\nPrice: {resultado[2]}")
        except (Exception, sqlite3.Error) as error:
            print("ERRO")


sistema = comidas("banco_de_dados_comida.db")

while True:
    add_chose = str(input("Deseja adicionar algum produto?[S/N]: ")).upper()
    if "S" in add_chose:
        adicionar_comid = str(input("Adicione uma comida: "))
        preço_comid = int(input("Digite o preço da comida: "))
        sistema.adicionar_comidas((adicionar_comid), (preço_comid))
    else:
        break
while True:
    remove_chose = str(input("Deseja remover alguma comida?[S/N]: ")).upper()
    if "S" in remove_chose:
        remove_id = int(input("Digite o ID: "))
        sistema.procurar_produto(remove_id)
        remove_chose_2 = str(input("Tem certeza que deseja deletar este produto?[S/N]: ")).upper()
        if "S" in remove_chose_2:
            sistema.remover_comidas(remove_id)
            print("Item removido com sucesso!!")
    else:
        break

sistema.consultar_comidas()
