from tkinter import *
from window import *
#Alumno: Diego Axel Valenzuela Rios | Matricula:200904
#CRUD

def main():
    root = Tk()
    root.wm_title("CRUD Python MySQL")

    print('Que desea hacer?\n1.clientes\n2.productos')
    opcion = int(input('Que desea actualizar?\n'))
    if(opcion == 1):
        app = window_costumer(root)
        app.mainloop()
    elif (opcion == 2):
        app = window_product(root)
        app.mainloop()
 
if __name__ == "__main__":
    main()
