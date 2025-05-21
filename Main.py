from tkinter import *
import csv
#import Func.py
import random
import time

ventana=Tk()
ventana.geometry("350x350")
ventana.config(background="#808080")


global RespuestasRandom
RespuestasRandom = []
global puntos
puntos=[]
global preguntas
preguntas=[]
global respuestas
respuestas=[]

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

def traerdatos():
    with open('datos.csv') as file:
        csv_reader = csv.DictReader(file, delimiter=',')
        for row in csv_reader:
            puntos.append(row['punto'])
            preguntas.append(row['pregunta'])
            respuestas.append(row['respuesta'])

def GenerarRespuestasRandom():
    global ResRandom
    ResRandom = respuestas[random.randint(0,ultimopunto-1)]
    if ResRandom in RespuestasRandom:
        GenerarRespuestasRandom()
    else:
        return ResRandom           
 
def BotoneraRandom():
    
    global ultimopunto
    global preguntarandom
    global RespuestaCorrecta

    ultimopunto = int(puntos[-1])
    puntorandom = random.randint(0,ultimopunto)
    preguntarandom = preguntas[puntorandom - 1]
    RespuestaCorrecta = respuestas[puntorandom - 1]
    RespuestasRandom.append(RespuestaCorrecta)

    for i in range(ultimopunto-1):
        RespuestasRandom.append(GenerarRespuestasRandom()) 
    
    random.shuffle(RespuestasRandom)
    return RespuestasRandom
    
    
def respuestaevento():
    if respuestaapretada == RespuestaCorrecta:
        global ResultadoLabel
        ventana.config(background='#00FF00')
        ResultadoLabel = Label(ventana, text = 'Correcto',bg="#00FF00")
        ResultadoLabel.grid(row = 4, column = 8, sticky = W, pady = 30)
        nuevapregunta()

    else:
        ventana.config(background='#FF0000')
        ResultadoLabel = Label(ventana, text = 'Inorrecto',bg="#FF0000")
        ResultadoLabel.grid(row = 4, column = 8, sticky = W, pady = 30)
    

def nuevapregunta():
    a=0
    for i in range(10000000):
       a+=1
    RespuestasRandom = []
    ventana.config(background="#808080")
    traerdatos()
    BorrarMemoria()
    PantallaMemoria()
        
def respuesta1evento(event):
    global respuestaapretada
    respuestaapretada = Res
    respuestaevento()        
    
def respuesta2evento(event):
    global respuestaapretada
    respuestaapretada = Res1
    respuestaevento()        
    
def respuesta3evento(event):
    global respuestaapretada
    respuestaapretada = Res2
    respuestaevento()        
    
def respuesta4evento(event):
    global respuestaapretada
    respuestaapretada = Res3
    respuestaevento()        
    
def respuesta5evento(event):
    global respuestaapretada
    respuestaapretada = Res4
    respuestaevento()        

def memorizarevento(event):
    traerdatos()
    borrar()
    PantallaMemoria()
    
def BorrarMemoria():
    PreguntaLabel.destroy()
    RespuestaLabel.destroy()
    Respuesta1Label.destroy()
    Respuesta2Label.destroy()
    Respuesta3Label.destroy()
    Respuesta4Label.destroy()   
    if 'ResultadoLabel' in globals():
        ResultadoLabel.destroy()
    
def ActivarLabelsMemoria():
    PreguntaLabel.place()
    RespuestaLabel.place()
    Respuesta1Label.place()
    Respuesta2Label.place()
    Respuesta3Label.place()
    Respuesta4Label.place()
    ResultadoLabel.place()

def textobotones():  
    Respuesta4Label.configure(text = Res4)
    Respuesta3Label.configure(text = Res3)
    Respuesta2Label.configure(text = Res2)
    Respuesta1Label.configure(text = Res1)
    RespuestaLabel.configure(text = Res)
    PreguntaLabel.configure(text=Preg1)
    
def PantallaMemoria():
    
    global ListaRespuestasRandom
    ListaRespuestasRandom = BotoneraRandom()
    
    ventana.config(background="#808080")
    global Preg1
    Preg1 = (str(preguntarandom))
    global PreguntaLabel
    PreguntaLabel = Label(ventana,bg="#808080")
    PreguntaLabel.grid(row = 1, column = 1, sticky = W, pady = 10,columnspan=4)
    
    global Res
    Res = str(ListaRespuestasRandom[0])
    global RespuestaLabel
    RespuestaLabel = Button(ventana,bg="#808080")
    RespuestaLabel.grid(row = 3, column = 1, sticky = W, pady = 10)   
    RespuestaLabel.bind("<Button>",respuesta1evento)
        
    global Res1
    Res1 = str(ListaRespuestasRandom[1])
    global Respuesta1Label
    Respuesta1Label = Button(ventana,bg="#808080")
    Respuesta1Label.grid(row = 3, column = 2, sticky = W, pady = 10)
    Respuesta1Label.bind("<Button>",respuesta2evento)
               
    global Res2              
    Res2 = str(ListaRespuestasRandom[2])
    global Respuesta2Label    
    Respuesta2Label = Button(ventana,bg="#808080")
    Respuesta2Label.grid(row = 3, column = 3, sticky = W, pady = 10)
    Respuesta2Label.bind("<Button>",respuesta3evento)
                 
    global Res3                
    Res3 = str(ListaRespuestasRandom[3])  
    global Respuesta3Label
    Respuesta3Label = Button(ventana,bg="#808080")
    Respuesta3Label.grid(row = 3, column = 4, sticky = W, pady = 10)
    Respuesta3Label.bind("<Button>",respuesta4evento)
                
    global Res4                     
    Res4 = str(ListaRespuestasRandom[4])  
    global Respuesta4Label
    Respuesta4Label = Button(ventana,bg="#808080")
    Respuesta4Label.grid(row = 3, column = 5, sticky = W, pady = 10)
    Respuesta4Label.bind("<Button>",respuesta5evento)
    
    textobotones()

def PantallaInicio():

    global PuntoLabel
    global CajaRespuesta
    global pregunta
    global CajaPregunta
    global RespuestaLabel
    global respuesta
    global botonEnviar
    global botonMemorizar
    global PreguntaLabel
    global CajaPunto
    global punto
    
    PuntoLabel = Label(ventana, text = "Punto:",bg="#808080")
    PuntoLabel.grid(row = 0, column = 0, sticky = W, pady = 2)
    
    punto=StringVar()
    CajaPunto= Entry(ventana,textvariable=punto)
    CajaPunto.grid(row = 0, column = 1, pady = 2)
    PreguntaLabel = Label(ventana, text = "Pregunta:",bg="#808080")
    PreguntaLabel.grid(row = 1, column = 0, sticky = W, pady = 2)

    pregunta=StringVar()
    CajaPregunta= Entry(ventana,textvariable=pregunta)
    CajaPregunta.grid(row = 1, column = 1, sticky = W, pady = 2)
    
    RespuestaLabel = Label(ventana, text = "Respuesta:",bg="#808080")
    RespuestaLabel.grid(row = 2, column = 0, sticky = W, pady = 2)
    
    respuesta=StringVar()
    CajaRespuesta= Entry(ventana,textvariable=respuesta)
    CajaRespuesta.grid(row = 2, column = 1, sticky = W, pady = 2)

    botonEnviar = Button(text="Enviar")
    botonEnviar.grid(row = 3, column = 0, sticky = W, pady = 2)
    botonEnviar.bind("<Button>",enviarevento)

    botonMemorizar = Button(text="Memorizar")
    botonMemorizar.grid(row = 3, column = 1, sticky = W, pady = 2)
    botonMemorizar.bind("<Button>",memorizarevento)

PantallaInicio()
ventana.mainloop()