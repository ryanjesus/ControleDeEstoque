from funçoes.conexao import SqlManager


class Execucao(SqlManager):

    cs = None

    def __init__(self):
        super().__init__()
        self.db_results = None

    def ExecuteS(self):
        cs.R_conexao_sql()
        query = 'SELECT * FROM Contas.dbo.estoque'
        self.cursor.execute(query)
        self.db_results = self.cursor.fetchall()
        # print(self.db_results)
        for row in self.db_results:
            print(
                f"id: {row[0]:<3} Produto: {row[1]:24} Quantidade: {row[2]} CreateDate: {row[3]} UpdateDate: {row[4]}")
        cs.DConnection()

    def UpdateS(self, qtd, onde):
        query = f"update dbo.estoque set quantidade = {qtd}, updateDate = getdate() where id = {onde}"
        self.cursor.execute(query)
        self.cnxn.commit()

    def InsertS(self, nome, qtd=0):
        query = f"insert into Contas.dbo.estoque (produto, quantidade, createDate, updateDate) values ('{nome}', {qtd}, getdate(), getdate()) "
        self.cursor.execute(query)
        self.cnxn.commit()

    def DeleteS(self, onde):
        query = f"delete from Contas.dbo.estoque where id = {onde}"
        self.cursor.execute(query)
        self.cnxn.commit()

    @staticmethod
    def MenuS():
        print('-' * 20)
        menu = 'Menu'
        print(f'{menu:^20}')
        print('-' * 20)
        print('1 - Lista de estoque')
        print('2 - Atualizar produto')
        print('3 - Adicionar produto')
        print('4 - Remover produto')
        print('0 - Sair')


cs = Execucao()

