import mysql.connector

class Clientes:

    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", passwd="ghost47", database="greengrocer")

    def __str__(self):
        datos = self.query_clientes()
        aux=""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def query_clientes(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM costumers")
        datos = cur.fetchall()
        cur.close()
        return datos

    def srch_cliente(self, Id):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM costumers WHERE CostumerID = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos

    def insert_cliente(self, Nombre, Telefono, Direccion):
        cur = self.cnn.cursor()
        sql = '''insert into costumers(CostumerName, PhoneNumber, Address) values('{}','{}','{}')'''.format(Nombre, Telefono, Direccion)
        #sql = "INSERT INTO clientes (Nombre, Apellido, Direccion) VALUES("{}","{}","{}")".format(Nombre, Apellido, Direccion)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def delete_cliente(self, Id):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM costumers WHERE CostumerID = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modify_cliente(self, Id, Nombre, Telefono, Direccion):
        cur = self.cnn.cursor()
        sql = '''UPDATE costumers SET CostumerName='{}', PhoneNumber='{}', Address='{}' WHERE CostumerID={}'''.format(Nombre, Telefono, Direccion, Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

class Products:
    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", passwd="ghost47", database="greengrocer")

    def __str__(self):
        datos = self.query_clientes()
        aux=""
        for row in datos:
            aux = aux + str(row) + "\n"
        return aux

    def query_productos(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM products")
        datos = cur.fetchall()
        cur.close()
        return datos

    def srch_producto(self, Id):
        cur = self.cnn.cursor()
        sql = "SELECT * FROM products WHERE ProductID = {}".format(Id)
        cur.execute(sql)
        datos = cur.fetchone()
        cur.close()
        return datos

    def insert_producto(self, Nombre, Precio, Unidad, Existencias, Proveedor):
        cur = self.cnn.cursor()
        sql = '''insert into products(ProductName, UnitPrice, Unit, Stock, SupplierID) values('{}','{}','{}','{}','{}')'''.format(Nombre, Precio, Unidad, Existencias, Proveedor)
        cur.execute(sql)
        n = cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    

    def delete_producto(self, Id):
        cur = self.cnn.cursor()
        sql = '''DELETE FROM products WHERE ProductID = {}'''.format(Id)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   

    def modify_producto(self, Nombre, Precio, Unidad, Existencias, Proveedor):
        cur = self.cnn.cursor()
        sql = '''UPDATE products SET ProductName='{}', UnitPrice='{}', Unit='{}', Stock='{}', SupplierID='{}' WHERE CostumerID={}'''.format(Nombre, Precio, Unidad, Existencias, Proveedor)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n   