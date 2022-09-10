from funçoes.conexao import SqlManager


class Execucao(SqlManager):
    cs = None

    def __init__(self):
        super().__init__()
        self.db_results = None

    def ExecuteF(self, produto):
        self.R_conexao_sql()
        query = f'SELECT * FROM Contas.dbo.estoque where id = {produto}'
        self.cursor.execute(query)
        self.db_results = self.cursor.fetchall()
        self.DConnection()

        return self.db_results

    def ExecuteS(self):
        self.R_conexao_sql()
        query = 'SELECT * FROM Contas.dbo.estoque'
        self.cursor.execute(query)
        self.db_results = self.cursor.fetchall()
        self.DConnection()

        return self.db_results


    def UpdateS(self, qtd, onde):
        self.R_conexao_sql()
        query = f"declare @valor int, @valor1 int; set @valor = (select quantidade from dbo.estoque where id = {onde}); set @valor1 = (@valor + {qtd}); update dbo.estoque set quantidade = @valor1, updateDate = getdate() where id = {onde}"
        self.cursor.execute(query)
        self.cnxn.commit()
        self.DConnection()

    def UpdateSub(self, qtd, onde):
        self.R_conexao_sql()
        query = f"declare @valor int, @valor1 int; set @valor = (select quantidade from dbo.estoque where id = {onde}); set @valor1 = (@valor - {qtd}); update dbo.estoque set quantidade = @valor1, updateDate = getdate() where id = {onde}"
        self.cursor.execute(query)
        self.cnxn.commit()
        self.DConnection()

    def InsertS(self, nome='', qtd=0):
        self.R_conexao_sql()
        query = f"insert into Contas.dbo.estoque (name, quantidade, createDate, updateDate) values ('{nome}', {qtd}, getdate(), getdate())"
        self.cursor.execute(query)
        self.cnxn.commit()
        self.DConnection()

    def DeleteS(self, onde):
        self.R_conexao_sql()
        query = f"delete from Contas.dbo.estoque where id = {onde}"
        self.cursor.execute(query)
        self.cnxn.commit()
        self.DConnection()

    @staticmethod
    def MenuS():
        print('-' * 20)
        menu = 'Menu'
        print(f'{menu:^20}')
        print('-' * 20)
        print('1 - Mostra Menu novamente')
        print('2 - Lista de estoque')
        print('3 - Atualizar produto')
        print('4 - Adicionar produto')
        print('5 - Remover produto')
        print('0 - Sair')


