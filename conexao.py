import pyodbc

class SqlManager:
    

    def __init__(self):
        self.server = "DESKTOP-E267L7P\SQLEXPRESS"
        self.database = "Contas"
        # self.cursor = None

    def r_conexao_sql(self):
        self.cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+self.server+';DATABASE='+self.database+';Trusted_Connection=yes;')

        return self.cnxn.cursor() 


    cursor = r_conexao_sql()

    cursor.execute("select * from Users")
    row = cursor.fetchone()
    while row: 
        print(row)
        row = cursor.fetchone()