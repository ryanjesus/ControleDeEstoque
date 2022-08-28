from conexao import SqlManager

class Execucao(SqlManager):

    def ExecuteS(self): 
        
        query = 'SELECT * FROM Contas.dbo.estoque'
        self.cursor.execute(query)
        self.db_results = self.cursor.fetchall()
        # print(self.db_results)
        for row in self.db_results:
            print(f"id: {row[0]} Produto: {row[1]} Quantidade: {row[2]} CreateDate: {row[3]} UpdateDate: {row[4]}" )
    
    def UpdateS(self):

        query = "update dbo.estoque set quatidade = {} where produto = '{}'"
        self.cursor.execute(query)
        self.cnxn.commit()
        
        

cs = Execucao()
#cs.R_conexao_sql()
cs.ExecuteS()
#cs.DConnection()

