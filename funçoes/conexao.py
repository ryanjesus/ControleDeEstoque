import pyodbc

class SqlManager:
    

    def __init__(self):
        self.server = "DESKTOP-E267L7P\SQLEXPRESS"
        self.database = "Contas"
        self.cnxn = None

    def R_conexao_sql(self):
        self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';Trusted_Connection=yes;')
        # self.cnxn._open_connection()

        self.cursor = self.cnxn.cursor()
        print('Conexão Bem Sucedida')

    def DConnection(self):
        self.cursor.close()
    
    # def ExecuteS(self):
    #     query = 'SELECT * FROM Contas.dbo.estoque'
    #     self.cursor.execute(query)
    #     self.db_results = self.cursor.fetchall()
    #     print(self.db_results)


#  cs = SqlManager()
#  cs.R_conexao_sql()
#  db_results = cs.ExecuteS()
#  print(db_results)

 # cs.DConnection()

    