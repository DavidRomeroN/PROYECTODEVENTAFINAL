"""from tkinter import *


Ventas = Tk()
Ventas.title("tienda de zapatillas los cariñosos")
Ventas.geometry("1350x700")
Ventas.config(bg="#36B5FF")
titulo = Label(Ventas, text="tienda de zapatillas los cariñosos",
bd=5, relief=FLAT, font=("Arial black", 20), bg="#1E395C", fg="black").pack(fill=X)

datos_cliente = LabelFrame(Ventas, text="Informacion del Cliente",
    font=("Arial black", 12),bg="#1E395C",fg="black",relief=FLAT, bd=10)
datos_cliente.place(x=0, y=80, relwidth=1) 

nombre = Label(datos_cliente, text="Nombre",font=("Arial black", 14),bg="#1E395C",
fg="black").grid(row=0, column=0,padx=8)
nombre_entry = Entry(datos_cliente,borderwidth=4,width=21).grid(row=0,column=1,padx=8)

apellido = Label(datos_cliente, text="Apellido",font=("Arial black", 14),bg="#1E395C",
fg="black").grid(row=0, column=2,padx=8)
apellido_entry = Entry(datos_cliente,borderwidth=4,width=21).grid(row=0,column=3,padx=8)

dni = Label(datos_cliente, text="DNI",font=("Arial black", 14),bg="#1E395C",
fg="black").grid(row=0, column=4,padx=8)
dni_entry = Entry(datos_cliente,borderwidth=4,width=21).grid(row=0,column=5,padx=8)

direccion = Label(datos_cliente, text="Direccion",font=("Arial black", 14),bg="#1E395C",
fg="black").grid(row=0, column=6,padx=8)
direccion_entry = Entry(datos_cliente,borderwidth=4,width=21).grid(row=0,column=7,padx=8)

telefono = Label(datos_cliente, text="Telefono",font=("Arial black", 14),bg="#1E395C",
fg="black").grid(row=0, column=8,padx=8)
telefono_entry = Entry(datos_cliente,borderwidth=4,width=21).grid(row=0,column=9,padx=8)

tabla_productos = Label(Ventas, text=" Productos",
    font=("Arial black", 15),bg="#1E395C",fg="black", relief=FLAT, borderwidth=10)
tabla_productos.place(x=12, y=180, width=1327)   

informatica = LabelFrame(Ventas, text="marca de zapatillas",font=(
    "Arial black", 12),bg="#1E395C", fg="black", relief=FLAT, borderwidth=10)
informatica.place(x=200, y=233, height=380, width=325)
 

frame = Frame(Ventas, bd=10, relief=FLAT, bg="#1E395C")
frame.place(x=800, y=233, width=330, height=380) 

factura = Label(frame, text="Factura",font=("Arial black", 14),
bd=2, relief=FLAT, bg="#1E395C", fg="#000000").pack(fill=X)

scroll = Scrollbar(frame, orient=VERTICAL)
texarea = Text(frame, yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)
scroll.config(command=texarea.yview)
texarea.pack(fill=BOTH, expand=1) 

nike= Label(informatica, text="NIKE", font=("Arial Black", 11), bg="#1E395C", 
fg="#000000").grid(row=1, column=0, pady=11)
nike_entry = Entry(informatica, borderwidth=2, width=20).grid(row=1, column=1, padx=10)

adidas = Label(informatica, text="ADIDAS", font=("Arial Black", 11), bg="#1E395C",
fg="#000000").grid(row=2, column=0, pady=11)
adidas_entry = Entry(informatica, borderwidth=2, width=20).grid(row=2, column=1, padx=10)

puma = Label(informatica, text="PUMA", font=("Arial Black", 11), bg="#1E395C",
fg="#000000").grid(row=3, column=0, pady=11)
puma_entry = Entry(informatica, borderwidth=2, width=20).grid(row=3, column=1, padx=10)

fila = Label(informatica, text="FILA", font=("Arial Black", 11), bg="#1E395C",
fg="#000000").grid(row=4, column=0, pady=11)
fila_entry = Entry(informatica, borderwidth=2, width=20).grid(row=4, column=1, padx=10)

reebok = Label(informatica, text="REEBOK", font=(
            "Arial Black", 11), bg="#1E395C", fg="#000000").grid(row=5, column=0, pady=11)
reebok_entry = Entry(informatica, borderwidth=2, width=20).grid(row=5, column=1, padx=10)

converse_duro = Label(informatica, text="CONVERSE", font=(
            "Arial Black", 11), bg="#1E395C", fg="#000000").grid(row=6, column=0, pady=11)
converse_duro_entry = Entry(informatica, borderwidth=2, width=20).grid(row=6, column=1, padx=10)

resumen = LabelFrame(Ventas, text="Resumen de compra",font=(
    "Arial Black", 11), relief=FLAT, bd=5, bg="#36B5FF",fg="#000000")
resumen.place(x=0, y=570, relwidth=1, height=137)    

infor_label = Label(resumen, text="Informatica", font=(
    "Arial Black", 11),bg="#36B5FF",fg="#000000").grid(row=0,column=0)
infor_entry = Entry(resumen, width=30, borderwidth=2).grid(row=0, column=1, padx=10, pady=15) 

ferre_label = Label(resumen, text="cantidad de productos", font=(
    "Arial Black", 11),bg="#36B5FF",fg="#000000").grid(row=2,column=0)
ferre_entry = Entry(resumen, width=30, borderwidth=2).grid(row=2, column=1, padx=10, pady=15) 

button_frame = Frame(resumen, bd=7, relief=FLAT, bg="#36B5FF") 
button_frame.place(x=550, width=800, height=95)

button_factura = Button(button_frame, text="Factura", width=15, font=("Arial Black", 12), 
pady=10,bg="#1E395C", fg="#000000").grid(row=0, column=0, padx=12, pady=12)

button_imprimir = Button(button_frame, text="Imprimir", width=15, font=("Arial Black", 12), 
pady=10,bg="#1E395C", fg="#000000").grid(row=0, column=1, padx=10, pady=6)

button_limpiar = Button(button_frame, text="Limpiar",  font=("Arial Black", 12), 
pady=10, bg="#1E395C",fg="#000000", width=15).grid(row=0, column=2, padx=10, pady=6)

button_salir = Button(button_frame, text="Salir", font=("Arial Black", 12), 
pady=10, bg="#1E395C",fg="#000000", width=15).grid(row=0, column=3, padx=10, pady=6)

Ventas.mainloop()"""