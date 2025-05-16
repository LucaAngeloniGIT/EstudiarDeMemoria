from tkinter import *
import csv
#import Func.py
import random

gris = "#808080"

ventana=Tk()
ventana.geometry("350x350")
ventana.config(background=gris)

def borrar():
    PuntoLabel.destroy()
    PreguntaLabel.destroy()
    RespuestaLabel.destroy()
    CajaPunto.destroy()
    CajaPregunta.destroy()
    CajaRespuesta.destroy()
    botonEnviar.destroy()
    botonMemorizar.destroy()
    
def enviarevento(event):
    with open('datos.csv', 'a', newline='') as archivo:
        DatosCSV = csv.writer(archivo, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        DatosCSV.writerow([punto.get()]+[pregunta.get()]+[respuesta.get()])
    
def memorizarevento(event):
    borrar()
    Memoria()

def traerdatos():
    with open('datos.csv') as file:
        csv_reader = csv.DictReader(file, delimiter=',')
        puntos=[]
        preguntas=[]
        respuestas=[]
        for row in csv_reader:
            puntos.append(row['punto'])
            preguntas.append(row['pregunta'])
            respuestas.append(row['respuesta'])
    return puntos,preguntas,respuestas

def Memoria():  
    puntos1,preguntas1,respuestas1 = traerdatos()
    ultimopunto = puntos1[-1]
    puntorandom = random.randint(0,int(ultimopunto))
    preguntarandom = preguntas1[puntorandom]
    RespuestaApregunta = respuestas1[puntorandom]
    
    PreguntaLabel = Label(ventana, text = str(preguntarandom),bg="#808080")
    PreguntaLabel.grid(row = 0, column = 1, sticky = W, pady = 10)
    
    ultimarespuesta = puntos1[-1]
    ListaRespuestasRandom = []
    ListaDesordenadaRespuestasRandom = []
    for i in range(4):
        numerorandom = random.randint(0,int(ultimarespuesta))
        ListaRespuestasRandom.append(respuestas1[numerorandom])
    ListaRespuestasRandom.append(RespuestaApregunta)
    ListaDesordenadaRespuestasRandom = random.shuffle(ListaRespuestasRandom)

    RespuestaLabel = Button(ventana, text = str(ListaDesordenadaRespuestasRandom[0]),bg="#808080")
    RespuestaLabel.grid(row = 2, column = 1, sticky = W, pady = 10)   

    Respuesta1Label = Button(ventana, text = str(ListaDesordenadaRespuestasRandom[1]),bg="#808080")
    Respuesta1Label.grid(row = 2, column = 2, sticky = W, pady = 10)
    
    Respuesta2Label = Button(ventana, text = str(ListaDesordenadaRespuestasRandom[2]),bg="#808080")
    Respuesta2Label.grid(row = 2, column = 3, sticky = W, pady = 10)
    
    Respuesta3Label = Button(ventana, text = str(ListaDesordenadaRespuestasRandom[3]),bg="#808080")
    Respuesta3Label.grid(row = 2, column = 4, sticky = W, pady = 10)
    
    Respuesta4Label = Button(ventana, text =str(ListaDesordenadaRespuestasRandom[4]),bg="#808080")
    Respuesta4Label.grid(row = 2, column = 5, sticky = W, pady = 10)

    
    
def Inicio():
    global PuntoLabel
    PuntoLabel = Label(ventana, text = "Punto:",bg="#808080")
    PuntoLabel.grid(row = 0, column = 0, sticky = W, pady = 2)
    
    punto=StringVar()
    global CajaPunto
    CajaPunto= Entry(ventana,textvariable=punto)
    CajaPunto.grid(row = 0, column = 1, pady = 2)

    global PreguntaLabel
    PreguntaLabel = Label(ventana, text = "Pregunta:",bg="#808080")
    PreguntaLabel.grid(row = 1, column = 0, sticky = W, pady = 2)

    pregunta=StringVar()
    global CajaPregunta
    CajaPregunta= Entry(ventana,textvariable=pregunta)
    CajaPregunta.grid(row = 1, column = 1, sticky = W, pady = 2)
    
    global RespuestaLabel
    RespuestaLabel = Label(ventana, text = "Respuesta:",bg="#808080")
    RespuestaLabel.grid(row = 2, column = 0, sticky = W, pady = 2)
    
    respuesta=StringVar()
    global CajaRespuesta
    CajaRespuesta= Entry(ventana,textvariable=respuesta)
    CajaRespuesta.grid(row = 2, column = 1, sticky = W, pady = 2)

    global botonEnviar
    botonEnviar = Button(text="Enviar")
    botonEnviar.grid(row = 3, column = 0, sticky = W, pady = 2)
    botonEnviar.bind("<Button>",enviarevento)

    global botonMemorizar
    botonMemorizar = Button(text="Memorizar")
    botonMemorizar.grid(row = 3, column = 1, sticky = W, pady = 2)
    botonMemorizar.bind("<Button>",memorizarevento)

Inicio()
ventana.mainloop()