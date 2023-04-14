#from io import BufferedIOBase
from tkinter import *
from tkinter import ttk
from connection import *
from tkinter import messagebox

class window_costumer(Frame):

    Clients = Clientes();

    def __init__(self, master=None):
        super().__init__(master,width=900, height=300)
        self.master = master
        self.pack()
        self.create_widgets()
        self.loadData()
        self.enableTB("disabled")
        self.enableBtnOp("normal")
        self.enableBtn("disabled")
        self.id = -1

    def loadData(self):
        datos = self.Clients.query_clientes()
        for row in datos:
            self.grid.insert("",END,text=row[0],values=(row[1],row[2],row[3]))

        if len(self.grid.get_children())>0:
            self.grid.selection_set(self.grid.get_children()[0])

    def enableTB(self,estado):
        self.txtNombre.configure(state=estado)
        self.txtApellido.configure(state=estado)
        self.txtDireccion.configure(state=estado)

    def enableBtnOp(self,estado):
        self.btnNew.configure(state=estado)
        self.btnUpdate.configure(state=estado)
        self.btnDelete.configure(state=estado)
        
    def enableBtn(self,estado):
        self.btnGuardar.configure(state=estado)
        self.btnCancelar.configure(state=estado)

    def clearTB(self):
        self.txtNombre.delete(0,END)
        self.txtApellido.delete(0,END)
        self.txtDireccion.delete(0,END)

    def clearGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
    
    def fNew(self):
        self.enableTB("normal")
        self.enableBtnOp("disabled")
        self.enableBtn("normal")
        self.clearTB()
        self.txtNombre.focus()
    
    def fUpdate(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, 'text')

        if clave == '':
            messagebox.showwarning("Modificar", "Debes seleccionar un elemento.")
        else:
            self.id = clave
            self.enableTB("normal")
            valores = self.grid.item(selected,'values')
            self.clearTB();

            self.txtNombre.insert(0,valores[0])
            self.txtApellido.insert(0,valores[1])
            self.txtDireccion.insert(0,valores[2])

            self.enableBtnOp("disabled")
            self.enableBtn("normal")
            self.txtNombre.focus()    

    def fDelete(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, 'text')

        if clave == '':
            messagebox.showwarning("Eliminar", "Debes seleccionar un elemento.")
        else:
            valores = self.grid.item(selected,'values')
            data = str(clave)+","+valores[0]+","+valores[1]+","+valores[2]
            r = messagebox.askquestion("Eliminar", "Deseas elminar el registro?\n"+data)
            if r == messagebox.YES:
                n = self.Clients.delete_cliente(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", "Elemento eliminado correctamente.")
                    self.clearGrid()
                    self.loadData()
                else:
                    messagebox.showinfo("Eliminar", "No se pudo eliminar el elemento.")

    def fGuardar(self):
        if self.id == -1:
            self.Clients.insert_cliente(self.txtNombre.get(), self.txtApellido.get(), self.txtDireccion.get())
            messagebox.showinfo("Insertar","Elemento insertado correctamente.")
        else:
            self.Clients.modify_cliente(self.id, self.txtNombre.get(), self.txtApellido.get(), self.txtDireccion.get())
            messagebox.showinfo("Modificar","Elemento modificado correctamente.")
            self.id = -1
        self.clearGrid()
        self.loadData()
        self.clearTB()
        self.enableBtn("disabled")
        self.enableBtnOp("normal")
        self.enableTB("disabled")

    def fCancelar(self):
        r = messagebox.askquestion("Cancelar","Estas seguro que quieres cancelar la operacion?")
        if r == messagebox.YES:
            self.clearTB()
            self.enableBtn("disabled")
            self.enableBtnOp("normal")
            self.enableTB("disabled")

    def create_widgets(self):
        frame1 = Frame(self, bg="#8B8B8B")
        frame1.place(x=0,y=0,width=100, height=300)

        self.btnNew=Button(frame1,text="Nuevo", command=self.fNew, bg="black", fg="#FF009B")
        self.btnNew.place(x=8,y=50,width=80, height=30 )

        self.btnUpdate=Button(frame1,text="Modificar", command=self.fUpdate, bg="black", fg="#FF009B")
        self.btnUpdate.place(x=8,y=100,width=80, height=30 )

        self.btnDelete=Button(frame1,text="Eliminar", command=self.fDelete, bg="black", fg="#FF009B")
        self.btnDelete.place(x=8,y=150,width=80, height=30 )

        frame2 = Frame(self,bg="#2A2A2A" )
        frame2.place(x=105,y=0,width=150, height=300)   

        #lbl1 = Label(frame2,text="ID Clientes: ")
        #lbl1.place(x=5,y=10)
        #self.txtID_Cliente=Entry(frame2)
        #self.txtID_Cliente.place(x=5,y=35,width=50, height=20) 

        lbl2 = Label(frame2,text="Nombre: ")
        lbl2.place(x=5,y=65)
        self.txtNombre=Entry(frame2)
        self.txtNombre.place(x=5,y=90,width=75, height=20)

        lbl3 = Label(frame2,text="Telefono: ")
        lbl3.place(x=5,y=120)
        self.txtApellido=Entry(frame2)
        self.txtApellido.place(x=5,y=145,width=100, height=20)

        lbl4 = Label(frame2,text="Direccion: ")
        lbl4.place(x=5,y=175)
        self.txtDireccion=Entry(frame2)
        self.txtDireccion.place(x=5,y=200,width=120, height=20)   

        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardar, bg="#6B00EB", fg="white")
        self.btnGuardar.place(x=10,y=240,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="#EB0067", fg="white")
        self.btnCancelar.place(x=80,y=240,width=60, height=30)     

        frame3 = Frame(self, bg="#E5025F")
        frame3.place(x=260, y=0, width=540, height=290)

        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3"))
        self.grid.column("#0",width=65)
        self.grid.column("col1",width=159, anchor=CENTER)
        self.grid.column("col2",width=100, anchor=CENTER)
        self.grid.column("col3",width=200, anchor=CENTER)
        self.grid.heading("#0", text="ID Cliente", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Telefono", anchor=CENTER)
        self.grid.heading("col3", text="Direccion", anchor=CENTER)
        #self.grid.place(x=260,y=0,width=435, height=290)

        self.grid.pack(side=LEFT, fill=Y)
        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode']='browse'

class window_product(Frame):

    Productos = Products();

    def __init__(self, master=None):
        super().__init__(master,width=1300, height=600)
        self.master = master
        self.pack()
        self.create_widgets()
        self.loadData()
        self.enableTB("disabled")
        self.enableBtnOp("normal")
        self.enableBtn("disabled")
        self.id = -1

    def loadData(self):
        datos = self.Productos.query_productos()
        for row in datos:
            self.grid.insert("",END,text=row[0],values=(row[1],row[2],row[3],row[4],row[5]))

        if len(self.grid.get_children())>0:
            self.grid.selection_set(self.grid.get_children()[0])

    def enableTB(self,estado):
        self.txtNombre.configure(state=estado)
        self.txtPrecio.configure(state=estado)
        self.txtUnidad.configure(state=estado)
        self.txtExistencias.configure(state=estado)
        self.txtProveedor.configure(state=estado)

    def enableBtnOp(self,estado):
        self.btnNew.configure(state=estado)
        self.btnUpdate.configure(state=estado)
        self.btnDelete.configure(state=estado)
        
    def enableBtn(self,estado):
        self.btnGuardar.configure(state=estado)
        self.btnCancelar.configure(state=estado)

    def clearTB(self):
        self.txtNombre.delete(0,END)
        self.txtPrecio.configure(0,END)
        self.txtUnidad.configure(0,END)
        self.txtExistencias.configure(0,END)
        self.txtProveedor.configure(0,END)

    def clearGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
    
    def fNew(self):
        self.enableTB("normal")
        self.enableBtnOp("disabled")
        self.enableBtn("normal")
        self.clearTB()
        self.txtNombre.focus()
    
    def fUpdate(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, 'text')

        if clave == '':
            messagebox.showwarning("Modificar", "Debes seleccionar un elemento.")
        else:
            self.id = clave
            self.enableTB("normal")
            valores = self.grid.item(selected,'values')
            self.clearTB();

            self.txtNombre.insert(0,valores[0])
            self.txtPrecio.insert(0,valores[1])
            self.txtUnidad.insert(0,valores[2])
            self.txtExistencias.insert(0,valores[3])
            self.txtProveedor.insert(0,valores[4])

            self.enableBtnOp("disabled")
            self.enableBtn("normal")
            self.txtNombre.focus()    

    def fDelete(self):
        selected = self.grid.focus()
        clave = self.grid.item(selected, 'text')

        if clave == '':
            messagebox.showwarning("Eliminar", "Debes seleccionar un elemento.")
        else:
            valores = self.grid.item(selected,'values')
            data = str(clave)+","+valores[0]+","+valores[1]+","+valores[2]
            r = messagebox.askquestion("Eliminar", "Deseas elminar el registro?\n"+data)
            if r == messagebox.YES:
                n = self.Clients.delete_cliente(clave)
                if n == 1:
                    messagebox.showinfo("Eliminar", "Elemento eliminado correctamente.")
                    self.clearGrid()
                    self.loadData()
                else:
                    messagebox.showinfo("Eliminar", "No se pudo eliminar el elemento.")

    def fGuardar(self):
        if self.id == -1:
            self.Productos.insert_producto(self.txtNombre.get(), self.txtPrecio.get(), self.txtUnidad.get(), self.txtExistencias.get(), self.txtProveedor.get())
            messagebox.showinfo("Insertar","Elemento insertado correctamente.")
        else:
            self.Productos.modify_producto(self.txtNombre.get(), self.txtPrecio.get(), self.txtUnidad.get(), self.txtExistencias.get(), self.txtProveedor.get())
            messagebox.showinfo("Modificar","Elemento modificado correctamente.")
            self.id = -1
        self.clearGrid()
        self.loadData()
        self.clearTB()
        self.enableBtn("disabled")
        self.enableBtnOp("normal")
        self.enableTB("disabled")

    def fCancelar(self):
        r = messagebox.askquestion("Cancelar","Estas seguro que quieres cancelar la operacion?")
        if r == messagebox.YES:
            self.clearTB()
            self.enableBtn("disabled")
            self.enableBtnOp("normal")
            self.enableTB("disabled")

    def create_widgets(self):
        frame1 = Frame(self, bg="#8B8B8B")
        frame1.place(x=0,y=0,width=100, height=600)

        self.btnNew=Button(frame1,text="Nuevo", command=self.fNew, bg="black", fg="#FF009B")
        self.btnNew.place(x=8,y=50,width=80, height=30 )

        self.btnUpdate=Button(frame1,text="Modificar", command=self.fUpdate, bg="black", fg="#FF009B")
        self.btnUpdate.place(x=8,y=100,width=80, height=30 )

        self.btnDelete=Button(frame1,text="Eliminar", command=self.fDelete, bg="black", fg="#FF009B")
        self.btnDelete.place(x=8,y=150,width=80, height=30 )

        frame2 = Frame(self,bg="#2A2A2A" )
        frame2.place(x=105,y=0,width=150, height=600)   

        #lbl1 = Label(frame2,text="ID Clientes: ")
        #lbl1.place(x=5,y=10)
        #self.txtID_Cliente=Entry(frame2)
        #self.txtID_Cliente.place(x=5,y=35,width=50, height=20) 

        lbl2 = Label(frame2,text="Nombre: ")
        lbl2.place(x=5,y=65)
        self.txtNombre=Entry(frame2)
        self.txtNombre.place(x=5,y=90,width=75, height=20)

        lbl3 = Label(frame2,text="Precio: ")
        lbl3.place(x=5,y=120)
        self.txtPrecio=Entry(frame2)
        self.txtPrecio.place(x=5,y=145,width=100, height=20)

        lbl4 = Label(frame2,text="Unidad: ")
        lbl4.place(x=5,y=175)
        self.txtUnidad=Entry(frame2)
        self.txtUnidad.place(x=5,y=200,width=120, height=20)   

        lbl5 = Label(frame2,text="Existencias: ")
        lbl5.place(x=5,y=230)
        self.txtExistencias=Entry(frame2)
        self.txtExistencias.place(x=5,y=255,width=120, height=20)   

        lbl6 = Label(frame2,text="Proveedor: ")
        lbl6.place(x=5,y=285)
        self.txtProveedor=Entry(frame2)
        self.txtProveedor.place(x=5,y=310,width=120, height=20)   


        self.btnGuardar=Button(frame2,text="Guardar", command=self.fGuardar, bg="#6B00EB", fg="white")
        self.btnGuardar.place(x=10,y=340,width=60, height=30)
        self.btnCancelar=Button(frame2,text="Cancelar", command=self.fCancelar, bg="#EB0067", fg="white")
        self.btnCancelar.place(x=80,y=340,width=60, height=30)     

        frame3 = Frame(self, bg="#E5025F")
        frame3.place(x=260, y=0, width=970, height=500)

        self.grid = ttk.Treeview(frame3, columns=("col1","col2","col3","col4","col5"))
        self.grid.column("#0",width=100, anchor=CENTER)
        self.grid.column("col1",width=159, anchor=CENTER)
        self.grid.column("col2",width=100, anchor=CENTER)
        self.grid.column("col3",width=200, anchor=CENTER)
        self.grid.column("col4",width=200, anchor=CENTER)
        self.grid.column("col5",width=200, anchor=CENTER)
        self.grid.heading("#0", text="ID Producto", anchor=CENTER)
        self.grid.heading("col1", text="Nombre", anchor=CENTER)
        self.grid.heading("col2", text="Precio", anchor=CENTER)
        self.grid.heading("col3", text="Unidad", anchor=CENTER)
        self.grid.heading("col4", text="Existencias", anchor=CENTER)
        self.grid.heading("col5", text="Proveedor", anchor=CENTER)
        #self.grid.place(x=260,y=0,width=435, height=290)

        self.grid.pack(side=LEFT, fill=Y)
        sb = Scrollbar(frame3, orient=VERTICAL)
        sb.pack(side=RIGHT, fill=Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode']='browse'

