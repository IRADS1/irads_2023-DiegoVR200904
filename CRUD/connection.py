import mysql.connector

class Clientes:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", passwd="ghost47", database="test")

    def __str__(self):
        datos = self.query_clientes()
        aux=""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def query_clientes(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM clientes")
        datos = cur.fetchall()
        cur.close()
        return datos

    def srch_cliente(self, Id):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM clientes WHERE idClientes = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos

    def insert_cliente(self, Nombre, Apellido, Direccion):
        cur = self.cnn.cursor()
        sql = '''INSERT INTO clientes (Nombre, Apellido, Direccion) VALUES('{}','{}','{}')'''.format(Nombre, Apellido, Direccion)
        #sql = "INSERT INTO clientes (Nombre, Apellido, Direccion) VALUES("{}","{}","{}")".format(Nombre, Apellido, Direccion)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def delete_cliente(self, Id):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM clientes WHERE idClientes = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modify_cliente(self, Id, Nombre, Apellido, Direccion):
        cur = self.cnn.cursor()
        sql = '''UPDATE clientes SET Nombre='{}', Apellido='{}', Direccion='{}' WHERE idClientes={}'''.format(Nombre, Apellido, Direccion, Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    