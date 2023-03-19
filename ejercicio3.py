
from tkinter import *
from tkinter import ttk
import tkinter as ttk

raiz = Tk()

raiz.title("interface ejercicio 2")
raiz.config()

mainFrameprincipal = ttk.Frame(raiz,bg="black")#donde se coloca todos los demas Frames
mainFrameprincipal.grid()

mainFramearribabarras = ttk.Frame(mainFrameprincipal,bg="black")#Frame donde se colocan las 2 barras de arriba
mainFramearribabarras.grid(column=0,row=0)

mainFramearriba = ttk.Frame(mainFramearribabarras,bg="white")#mainFrame de la parte de arriba color blanco
mainFramearriba.grid(column=0,row=0)

mainFramearribaazul = ttk.Frame(mainFramearribabarras,bg="#097479")#mainFrame arriba de color azul 
mainFramearribaazul.grid(pady=0,padx=0,column=0,row=1,sticky=W)

mainFramefondoconbarra = ttk.Frame(mainFrameprincipal,bg="black")#Frame para que se acomoden las barras de arriba (azul y blanca)
mainFramefondoconbarra.grid()

mainFramefondo = ttk.Frame(mainFramefondoconbarra,bg="black")#mainFrame de fondo color negro donde iran los indicadores y tablas
mainFramefondo.grid(padx=90)

mainFrameacomdolateral = ttk.Frame(mainFramefondo,bg="black")#Frame donde se coloca todolo que ira a la izquierda
mainFrameacomdolateral.grid(column=0,row=0,pady=5)

#Frames de indicadores arriba
mainFrameindicadoresarriba = ttk.Frame(mainFrameacomdolateral,bg="black")#Frame para acomodar los subframes de arriba
mainFrameindicadoresarriba.grid(column=0,row=0)

mainFrametablas = ttk.Frame(mainFrameindicadoresarriba,bg="#333333")
mainFrametablas.grid(padx=7)

mainFrametablasa = ttk.Frame(mainFrametablas,bg="#333333")
mainFrametablasa.grid(column=0,row=0)

mainFrametablasacomdo = ttk.Frame(mainFrametablas,background="#333333")
mainFrametablasacomdo.grid()

mainFrame1 = ttk.Frame(mainFrametablasacomdo,bg="#333333")
mainFrame1.grid(column=0,row=1)

mainFrametablas2fondo = ttk.Frame(mainFrameindicadoresarriba,bg="#333333")
mainFrametablas2fondo.grid(column=1,row=0,sticky=N)

mainFrametablas2 = ttk.Frame(mainFrametablas2fondo,bg="#333333")
mainFrametablas2.grid()

mainFrame2 = ttk.Frame(mainFrametablas2fondo,bg="#333333")
mainFrame2.grid(row=1)

#Frames de la parte de abajo
mainFrameindicadoresabajo = ttk.Frame(mainFrameacomdolateral,bg="black")#Frame para acomodar los 2 frames de abajo
mainFrameindicadoresabajo.grid(column=0,row=1,pady=3)

mainFramebomba = ttk.Frame(mainFrameindicadoresabajo,bg="#333333")
mainFramebomba.grid(column=0,row=0,pady=3)

mainFrametanque = ttk.Frame(mainFrameindicadoresabajo,bg="#333333")
mainFrametanque.grid(column=1,row=0,sticky=N,padx=3,pady=3)

#Frame grafica de lado derecho
mainFramegrafica = ttk.Frame(mainFramefondo,bg="#333333")
mainFramegrafica.grid(column=1,row=0,sticky=N,padx=3,pady=5)

mainFramegraficaabajo = ttk.Frame(mainFramegrafica,bg="#333333")
mainFramegraficaabajo.grid(column=0,row=2)

#Frame barra lateral
mainFramebarral = ttk.Frame(mainFramefondoconbarra)
mainFramebarral.grid(column=2,row=0)



#A partir de aqui empieza el acomdo, creacion de botones, graficas y Labels
#mainframearriba
ttk.Label(mainFramearriba,text=" ",background="white").grid(column=1,row=0,padx=713)
#mainFramearribaazul
ttk.Label(mainFramearribaazul,text="SPAI 4.0",background="#097479",fg="white",font=("Arial",10,"bold")).grid(column=1,row=0,sticky=E,padx=0)

imagenmenu = PhotoImage(file="menu.png") #imagen boton menu de arriba
btnImagen = ttk.Button(mainFramearribaazul,borderwidth=0)
btnImagen.grid(column=0,row=0)
btnImagen.configure(background="#097479")
btnImagen['image']=imagenmenu

ttk.Label(mainFramearribaazul,text=" ",background="#097479").grid(column=2,row=0,padx=661)

#mainFrametablas
#mainFrame1 (texto al lado de botones)
ttk.Label(mainFrametablasa,text="Indicadores digitales",background="#333333",fg="#097479",font=("Calibri",12,"bold")).grid(column=0,row=0,padx=28,pady=10)
ttk.Label(mainFrame1,text="Linea 1:",background="#333333",fg="white").grid(column=0,row=0,sticky=W,padx=10,pady=10)
ttk.Label(mainFrame1,text="Linea 2:",background="#333333",fg="white").grid(column=0,row=1,sticky=W,padx=10,pady=10)
ttk.Label(mainFrame1,text="Linea 1:",background="#333333",fg="white").grid(column=0,row=2,sticky=W,padx=10,pady=10)
ttk.Label(mainFrame1,text="   Gabinete:",background="#333333",fg="white").grid(column=0,row=3,sticky=W,padx=0,pady=10)
ttk.Label(mainFrame1,text="Alarma:",background="#333333",fg="white").grid(column=0,row=4,sticky=W,padx=10,pady=10)
ttk.Label(mainFrame1,text="Alarma 2:",background="#333333",fg="white").grid(column=0,row=5,sticky=W,padx=10,pady=10.5)

#mainFrame2 (botones)
ttk.Button(mainFrame1,text="On",background="#333333",borderwidth=0,fg="white",font=("Arial",11,"bold")).grid(column=1,row=0)
ttk.Button(mainFrame1,text="On",background="#333333",borderwidth=0,fg="white",font=("Arial",11,"bold")).grid(column=1,row=1)
ttk.Button(mainFrame1,text="On",background="#333333",borderwidth=0,fg="white",font=("Arial",11,"bold")).grid(column=1,row=2)
ttk.Button(mainFrame1,text="Abierto",background="#333333",borderwidth=0,fg="white",font=("Arial",11,"bold")).grid(column=1,row=3,sticky=E)
ttk.Button(mainFrame1,text="On",background="#333333",borderwidth=0,fg="white",font=("Arial",11,"bold")).grid(column=1,row=4)
ttk.Button(mainFrame1,text="Off",background="#333333",borderwidth=0,fg="white",font=("Arial",11,"bold")).grid(column=1,row=5)

#imagen botones
imagenbotonverde = PhotoImage(file="botonverde.png")
btnImagen = ttk.Button(mainFrame1,borderwidth=0)
btnImagen.grid(column=2,row=0)
btnImagen.configure(background="#333333")
btnImagen['image']=imagenbotonverde

btnImagen = ttk.Button(mainFrame1,borderwidth=0)
btnImagen.grid(column=2,row=1)
btnImagen.configure(background="#333333")
btnImagen['image']=imagenbotonverde

btnImagen = ttk.Button(mainFrame1,borderwidth=0)
btnImagen.grid(column=2,row=2)
btnImagen.configure(background="#333333")
btnImagen['image']=imagenbotonverde

imagenbotonrojo = PhotoImage(file="botonrojo.png")
btnImagen = ttk.Button(mainFrame1,borderwidth=0)
btnImagen.grid(column=2,row=3)
btnImagen.configure(background="#333333")
btnImagen['image']=imagenbotonrojo

btnImagen = ttk.Button(mainFrame1,borderwidth=0)
btnImagen.grid(column=2,row=4)
btnImagen.configure(background="#333333")
btnImagen['image']=imagenbotonrojo

btnImagen = ttk.Button(mainFrame1,borderwidth=0)
btnImagen.grid(column=2,row=5)
btnImagen.configure(background="#333333")
btnImagen['image']=imagenbotonverde


#mainFrametablas2 (temperaturas)
ttk.Label(mainFrametablas2,text="Temperaturas",background="#333333",fg="#097479",font=("Calibri",12,"bold")).grid(column=0,row=0,padx=18,pady=5.1,sticky=W)
ttk.Label(mainFrametablas2,text="Temperatura 1:",background="#333333",fg="white").grid(column=0,row=1,pady=10,padx=25)
ttk.Label(mainFrametablas2,text="Temperatura 2:",background="#333333",fg="white").grid(column=1,row=1,pady=10,padx=25)

imagent1 = PhotoImage(file="temperatura1.png")#imagen temperatura 1
btnImagen = ttk.Button(mainFrametablas2,borderwidth=0)
btnImagen.grid(column=0,row=2,padx=23)
btnImagen.configure(background="#333333")
btnImagen['image']=imagent1

imagent2 = PhotoImage(file="temperatura2.png")#imagen temperatura 2
btnImagen = ttk.Button(mainFrametablas2,borderwidth=0)
btnImagen.grid(column=1,row=2,padx=23)
btnImagen.configure(background="#333333")
btnImagen['image']=imagent2


ttk.Label(mainFrame2,text="Temp. Agua: 58°C",background="#333333",fg="white").grid(pady=20)
ttk.Label(mainFrame2,text="Temp. Ambiente: 32°C",background="#333333",fg="white").grid(pady=15)

#mainFramebomba
ttk.Label(mainFramebomba,text="  ",background="#333333").grid(column=0,row=0,pady=10)
ttk.Label(mainFramebomba,text="        Velocidad bomba:     ",background="#333333",fg="White",font=("Calibri",16)).grid(column=0,row=1,pady=2,padx=10,sticky=W)
imagentbomba = PhotoImage(file="bomba2.png")#imagen bomba
btnImagen = ttk.Button(mainFramebomba,borderwidth=0)
btnImagen.grid(column=0,row=2,padx=25)
btnImagen.configure(background="#333333")
btnImagen['image']=imagentbomba


#mainFrametanque
ttk.Label(mainFrametanque,text="Nivel del tanque",background="#333333",fg="#097479",font=("Calibri",12,"bold")).grid(sticky=W,pady=9,padx=15)
imagenttanque = PhotoImage(file="tanque.png")#imagen tanque
btnImagen = ttk.Button(mainFrametanque,borderwidth=0)
btnImagen.grid(column=0,row=1,padx=20)
btnImagen.configure(background="#333333")
btnImagen['image']=imagenttanque
ttk.Label(mainFrametanque,text="  ",background="#333333").grid(column=1,row=1)#hacer espacio hacia un lado sin que se desacomode lo demas

#mainFramegrafica
ttk.Label(mainFramegrafica,text="Produccion",background="#333333",fg="#097479",font=("Calibri",12,"bold")).grid(row=0,sticky=W,padx=10,pady=5.1)

imagentgrafica = PhotoImage(file="grafica.png")#imagen grafica
btnImagen = ttk.Button(mainFramegrafica,borderwidth=0)
btnImagen.grid(column=0,row=1,padx=10)
btnImagen.configure(background="#333333")
btnImagen['image']=imagentgrafica
#Frames para poner en negritas los numeros y no se desacomoden
mainFrameacomdopalabrasgrafica = ttk.Label(mainFramegraficaabajo,background="#333333")
mainFrameacomdopalabrasgrafica.grid(column=0,row=2)
mainFrameacomdopalabrasgrafica2 = ttk.Label(mainFramegraficaabajo,background="#333333")
mainFrameacomdopalabrasgrafica2.grid(column=0,row=3)
#texto debajo de la grafica
ttk.Label(mainFrameacomdopalabrasgrafica,text="Piezas producidas: ",background="#333333",fg="white").grid(pady=20)
ttk.Label(mainFrameacomdopalabrasgrafica,text="50",background="#333333",fg="white",font=("Calibri",12,"bold")).grid(column=1,row=0)
ttk.Label(mainFrameacomdopalabrasgrafica2,text="Piezas defectuosas:",background="#333333",fg="white").grid(pady=15)
ttk.Label(mainFrameacomdopalabrasgrafica2,text="12",background="#333333",fg="white",font=("Calibri",12,"bold")).grid(column=1,row=0)

#mainFramebarralateral
imagentbarral = PhotoImage(file="barral.png")
btnImagen = ttk.Button(mainFramebarral,borderwidth=0)
btnImagen.grid(column=0,row=0)
btnImagen.configure(background="#333333")
btnImagen['image']=imagentbarral

raiz.mainloop()
