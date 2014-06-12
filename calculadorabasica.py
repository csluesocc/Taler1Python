from Tkinter import*
import tkMessageBox

#Hacemos un metodo para calcular las operaciones aritmeticas
def suma():
  n1= float(caja1.get())
  n2= float(caja2.get())
  suma= n1+n2
  tkMessageBox.showinfo("Su resultado","la suma es: %2.f"%suma)
  caja1.delete(0,20)
  caja2.delete(0,20)

def resta():
  n1= float(caja1.get())
  n2= float(caja2.get())
  res= n1-n2
  tkMessageBox.showinfo("Su resultado","la resta es: %2.f"%res)
  caja1.delete(0,20)
  caja2.delete(0,20)

def multiplicar():
  n1= float(caja1.get())
  n2= float(caja2.get())
  multi= n1*n2
  tkMessageBox.showinfo("Su resultado","la multiplicacion es: %2.f"%multi)
  caja1.delete(0,20)
  caja2.delete(0,20)

def dividir():
  n1= float(caja1.get())
  n2= float(caja2.get())
  di= n1/n2
  tkMessageBox.showinfo("Su resultado","la division es: %2.f"%di)
  caja1.delete(0,20)
  caja2.delete(0,20)

#creamos la interfaz grafica (gui)
ventana=Tk()
#asiganamos un titulo
ventana.title("Calculadora Basica CSHL")
# dimensiones para la ventana(alto,ancho etc)
ventana.geometry("400x250+400+200")

#creamos etiquetas para mostrar texto

var1 = StringVar()
var1.set("Ingresa un numero")
label1 = Label(ventana,textvariable=var1,height = 2)
label1.pack()
#creamos una caja de texto para el primer numero(caja1)
numero1 = StringVar()
caja1 = Entry(ventana,bd= 4,textvariable=numero1)
caja1.pack()
#creamos otra etiqueta para decirle al usuario que ingrese otro numero
var2 = StringVar()
var2.set("Ingresa un numero")
label2 = Label(ventana,textvariable=var2,height = 2)
label2.pack()
#creamos otra caja para el siguiente valor (caja2)
numero2 = StringVar()
caja2 = Entry(ventana,bd= 4,textvariable=numero2)
caja2.pack()

#creamos los botones que llamaran los metodos
botton1 = Button(ventana, text="sumar", command= suma, width=20, bg='blue')
botton1.pack()

botton2 = Button(ventana, text="resta", command= resta, width=20, bg='green')
botton2.pack()

botton3 = Button(ventana, text="dividir", command= dividir, width=20, bg='blue')
botton3.pack()

botton4 = Button(ventana, text="multiplicar", command= multiplicar, width=20, bg='green')
botton4.pack()

#cargar la interfaz

ventana.mainloop()







