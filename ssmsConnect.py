import pyodbc
con_string ="driver=ODBC Driver 17 for SQL Server;server=DESKTOP-H017GK7S\SQLEXPRESS;database=disney;trusted_connection=yes;"

def create_table():
    sql =""" create table Person(
        id int identity(1,1) primary key,
        gender char(1),
        weight real,
        height real
    )"""
    with pyodbc.connect(con_string) as con:
        con.execute(sql)

if __name__=='__main__':
    create_table