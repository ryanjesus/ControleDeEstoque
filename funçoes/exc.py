from conexao import SqlManager

class Execucao(SqlManager):

    def ExecuteS(self):
        query = 'SELECT nome, email FROM Contas.dbo.Users'
        self.cursor.execute(query)
        self.db_results = self.cursor.fetchall()
        print(self.db_results)

cs = Execucao()
cs.R_conexao_sql()
cs.ExecuteS()
cs.DConnection()

