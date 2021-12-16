#!/usr/bin/python3
version = "0.8.2"

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from random import randrange

#Permitir la recursividad (temporal)--------------------------------------------
import sys
sys.setrecursionlimit(5000)
#-------------------------------------------------------------------------------

import subprocess #Necesario para usar el sistema y sus funciones
clear = lambda: subprocess.call('cls||clear', shell=True) #Llamada al sistema

#Creacion Archivo Puntuaciones--------------------------------------------------
try:
    archivo = open("./points.txt", "x")
    archivo.write("0")
    archivo.close()
except:
    print("Archivo 1")
#-------------------------------------------------------------------------------

class MathGamePuntuacion(App):

    def build(self):

        #Función que detecta el texto del botón seleccionado en pantalla--------
        def callback(instance):

            superBox.remove_widget(pie)
            superBox.remove_widget(cabecera)
            MathGame().run()
        #-----------------------------------------------------------------------

        archivo = open("./points.txt", "r") #Abrir archivo----------------------

        #Interfaz---------------------------------------------------------------
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal') #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        consola = Label(text = "Puntuación: "+archivo.read())

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        aceptar = Button(text = "Vale",background_color = (0,0.4,1,0.8))
        aceptar.bind(on_press=callback)

        null = Label(text = "")
        null2 = Label(text = "")

        #Añadir elementos al pie------------------------------------------------
        pie.add_widget(null)
        pie.add_widget(null2)
        pie.add_widget(aceptar)

        #Añadir cada división al layout global----------------------------------
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

        #Mostrar layout completo------------------------------------------------
        return superBox
        #Fin Interfaz-----------------------------------------------------------

class MathGameComprobacion(App):

    global resultadoreal
    global comprobacion
    global operacion
    operacion = ""
    global resultadoAintroducir

    def build(self):

        global vidaMostrar

        #Función que registra botón seleccionado--------------------------------
        def callback(instance):

            global operacion

            #Sin este código se mantiene la introducción anterior por teclado---
            global resultadoAintroducir
            resultadoAintroducir = 998003
            #-------------------------------------------------------------------

            if operacion == "Sumas":
                superBox.remove_widget(cabecera)
                superBox.remove_widget(pie)
                MathGameSumas().run()
            else:
                if operacion == "Restas":
                    superBox.remove_widget(cabecera)
                    superBox.remove_widget(pie)
                    MathGameRestas().run()
                else:
                    if operacion == "Multiplicaciones":
                        superBox.remove_widget(cabecera)
                        superBox.remove_widget(pie)
                        MathGameMultiplicaciones().run()
                    else:
                        superBox.remove_widget(cabecera)
                        superBox.remove_widget(pie)
                        MathGameDivisiones().run()
        #-----------------------------------------------------------------------

        global operacion

        #Interfaz---------------------------------------------------------------
        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal
        cabecera = BoxLayout(orientation ='horizontal')

        if comprobacion == 0:

            if modo_supervivencia == 1:

                global vida
                vida = vida - 1

            resultadoMostrar = str(resultadoreal)
            consola = Label(text = "El resultado era "+resultadoMostrar)

        else:

            consola = Label(text = "¡Has acertado!")

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical
        pie = BoxLayout(orientation ='vertical')

        aceptar = Button(text = "Vale",background_color = (0,0.4,1,0.8))
        aceptar.bind(on_press=callback)

        null = Label(text = "")
        null2 = Label(text = "")

        pie.add_widget(null)
        pie.add_widget(null2)
        pie.add_widget(aceptar)

        #Salida por pantalla final----------------------------------------------
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

        #Mostrar layout completo------------------------------------------------
        return superBox
        #Fin interfaz-----------------------------------------------------------

class MathGameResultado(App):

    def build(self):

        global ContadorPreguntas
        global puntuacion
        global MultiPuntuacion

        #Abrir archivo, lectura y procesamiento---------------------------------
        archivo = open("./points.txt", "r")

        contenido = archivo.read()
        contenidoInt = int(contenido)

        puntuacionMultiplicada = puntuacion*MultiPuntuacion

        InputArchivo = contenidoInt+puntuacionMultiplicada
        InputArchivo = str(InputArchivo)

        archivo = open("./points.txt", "w")
        archivo.write(InputArchivo)
        archivo.close()
        #-----------------------------------------------------------------------

        #Función que registra el botón seleccionado-----------------------------
        def callback(instance):

            global operacion
            global ContadorPreguntas
            global puntuacion
            global modo_supervivencia
            global vida

            respuestaSeleccionada = instance.text #contiene el string del boton
            print(instance.text)

            if respuestaSeleccionada == "si":

                ContadorPreguntas = int(ContadorPreguntas)
                puntuacion = int(puntuacion)

                ContadorPreguntas = 0
                puntuacion = 0

                if modo_supervivencia == 1:
                    vida = 5

                if operacion == "Sumas":

                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)
                    MathGameSumas().run()

                else:

                    if operacion == "Restas":

                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)
                        MathGameRestas().run()

                    else:

                        if operacion == "Multiplicaciones":

                            superBox.remove_widget(pie)
                            superBox.remove_widget(cabecera)
                            MathGameMultiplicaciones().run()

                        else:

                            superBox.remove_widget(pie)
                            superBox.remove_widget(cabecera)
                            MathGameDivisiones().run()

            else:

                ContadorPreguntas = int(ContadorPreguntas)
                puntuacion = int(puntuacion)

                ContadorPreguntas = 0
                puntuacion = 0

                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGame().run()
        #-----------------------------------------------------------------------

        print(ContadorPreguntas)
        print(puntuacion)

        ContadorPreguntas = str(ContadorPreguntas)
        puntuacion = str(puntuacion)

        #Interfaz---------------------------------------------------------------
        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal')

        consola = Label(text = "Has acertado "+puntuacion+" de un total de "+ContadorPreguntas)

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        bienvenida = Label(text = "¿Quieres seguir realizando operaciones?")

        aceptar = Button(text = "si",background_color = (0,0.4,1,0.8))
        aceptar.bind(on_press=callback)

        rechazar = Button(text = "no",background_color = (0,0.4,1,0.8))
        rechazar.bind(on_press=callback)

        pie.add_widget(bienvenida)
        pie.add_widget(aceptar)
        pie.add_widget(rechazar)

        #Salida por pantalla final----------------------------------------------
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

        #Mostrar layout completo------------------------------------------------
        return superBox
        #Fin interfaz-----------------------------------------------------------

class MathGameDivisiones(App):

    global ContadorPreguntas
    ContadorPreguntas = 0

    global puntuacion
    puntuacion = 0

    def build(self):

        global resultadoreal
        resultadoreal = 0

        global vidaMostrar
        global vida
        global vidascii

        #Función que registra el botón seleccionado-----------------------------
        def callback(instance):

            global puntuacion
            global ContadorPreguntas
            global comprobacion

            #Gestión de la excepción al presionar botón sin introducir nada-----
            try:
                respuestaOperaciones = resultadoAintroducir #contiene el string del boton
            except:
                respuestaOperaciones = 998003
            #-------------------------------------------------------------------

            print(respuestaOperaciones)
            if respuestaOperaciones == resultadoreal:
                puntuacion = puntuacion + 1
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                ContadorPreguntas = ContadorPreguntas + 1
                comprobacion = 1
                MathGameComprobacion().run()
            else:
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                ContadorPreguntas = ContadorPreguntas + 1
                comprobacion = 0
                MathGameComprobacion().run()
        #-----------------------------------------------------------------------

        #Funcion que registra contenido del input-------------------------------
        def on_text(instance, value):

            global resultadoAintroducir
            print('The widget', instance, 'have:', value)

            try:
                value = int(value)
                resultadoAintroducir = value
            except:
                resultadoAintroducir = 998003
        #-----------------------------------------------------------------------

        while ContadorPreguntas < numPreguntas or vida != 0:

            #Modulo Sumas
            randomnumero1 = 0
            randomnumero2 = 0
            resultadoreal = 0
            solucion = 0
            #-------------------------------------------------------------------

            print("Divisiones entre dos numeros:")
            print("")
            randomnumero1=(randrange(RangoMin,RangoMax))          #Rango de suma
            randomnumero2=(randrange(RangoMin,RangoMax))          #Rango de suma
            mostrarnumero1 = str(randomnumero1)
            mostrarnumero2 = str(randomnumero2)
            print(randomnumero1,"/",randomnumero2)

            try:
                resultadoreal = randomnumero1/randomnumero2           #Resultadoreal
            except:
                randomnumero1 = randomnumero1 + 1
                randomnumero2 = randomnumero2 + 1
                resultadoreal = randomnumero1/randomnumero2

            resultadoreal = int(resultadoreal)              #Convertir a Integer

            #Debugging----------------------------------------------------------
            print(resultadoreal)
            #-------------------------------------------------------------------

            #Interfaz-----------------------------------------------------------
            #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
            superBox = BoxLayout(orientation ='vertical')

            #Widgets de cabecera añadidos en el plano horizontal----------------
            cabecera = BoxLayout(orientation ='horizontal')

            if modo_supervivencia == 1:

                vidaStr = str(vida)
                consola = Label(text = "Tienes "+vidaStr+" vidas "+"|"+" Divisiones entre dos numeros: "+mostrarnumero1+" / "+mostrarnumero2)

            else:

                consola = Label(text = "Divisiones entre dos numeros: "+mostrarnumero1+" / "+mostrarnumero2)

            cabecera.add_widget(consola)

            #Widgets de pie de página añadidos en el plano vertical-------------
            pie = BoxLayout(orientation ='vertical')

            bienvenida = Button(text = "Seleccione la respuesta",background_color = (0,0.4,1,0.8))
            bienvenida.bind(on_press=callback)

            textinput = TextInput()
            textinput.bind(text=on_text)

            null = Label(text = "")
            null2 = Label(text = "")

            pie.add_widget(null)
            pie.add_widget(null2)
            pie.add_widget(textinput)
            pie.add_widget(bienvenida)

            #Salida por pantalla final------------------------------------------
            superBox.add_widget(cabecera)
            superBox.add_widget(pie)

            #Mostrar layout completo--------------------------------------------
            return superBox
            #Fin interfaz-------------------------------------------------------

        #Comprobación turnos o vidas--------------------------------------------
        if modo_supervivencia == 0:
            if ContadorPreguntas == numPreguntas:
                MathGameResultado().run()
        else:
            if vida == 0:
                MathGameResultado().run()

class MathGameMultiplicaciones(App):

    global ContadorPreguntas
    ContadorPreguntas = 0

    global puntuacion
    puntuacion = 0

    def build(self):

        global resultadoreal
        resultadoreal = 0

        global vidaMostrar
        global vida
        global vidascii

        #Función que registra el botón seleccionado-----------------------------
        def callback(instance):

            global puntuacion
            global ContadorPreguntas
            global comprobacion

            #Gestión de la excepción al presionar botón sin introducir nada-----
            try:
                respuestaOperaciones = resultadoAintroducir #contiene el string del boton
            except:
                respuestaOperaciones = 998003
            #-------------------------------------------------------------------

            print(respuestaOperaciones)
            if respuestaOperaciones == resultadoreal:
                puntuacion = puntuacion + 1
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                ContadorPreguntas = ContadorPreguntas + 1
                comprobacion = 1
                MathGameComprobacion().run()
            else:
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                ContadorPreguntas = ContadorPreguntas + 1
                comprobacion = 0
                MathGameComprobacion().run()
        #-----------------------------------------------------------------------

        #Funcion que registra contenido del input-------------------------------
        def on_text(instance, value):

            global resultadoAintroducir
            print('The widget', instance, 'have:', value)

            try:
                value = int(value)
                resultadoAintroducir = value
            except:
                resultadoAintroducir = 998003
        #-----------------------------------------------------------------------

        while ContadorPreguntas < numPreguntas or vida != 0:

            #Modulo Sumas
            randomnumero1 = 0
            randomnumero2 = 0
            resultadoreal = 0
            solucion = 0
            #-------------------------------------------------------------------

            print("Multiplicaciones entre dos numeros:")
            print("")
            randomnumero1=(randrange(RangoMin,RangoMax))          #Rango de multiplicaciones
            randomnumero2=(randrange(RangoMin,RangoMax))          #Rango de multiplicaciones
            mostrarnumero1 = str(randomnumero1)
            mostrarnumero2 = str(randomnumero2)
            print(randomnumero1,"+",randomnumero2)
            resultadoreal = randomnumero1*randomnumero2           #Resultadoreal
            resultadoreal = int(resultadoreal)              #Convertir a Integer

            #Debugging----------------------------------------------------------
            print(resultadoreal)
            #-------------------------------------------------------------------

            #Interfaz-----------------------------------------------------------
            #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
            superBox = BoxLayout(orientation ='vertical')

            #Widgets de cabecera añadidos en el plano horizontal----------------
            cabecera = BoxLayout(orientation ='horizontal')

            if modo_supervivencia == 1:

                vidaStr = str(vida)
                consola = Label(text = "Tienes "+vidaStr+" vidas "+"|"+" Multiplicaciones entre dos numeros: "+mostrarnumero1+" x "+mostrarnumero2)

            else:

                consola = Label(text = "Multiplicaciones entre dos numeros: "+mostrarnumero1+" x "+mostrarnumero2)

            cabecera.add_widget(consola)

            #Widgets de pie de página añadidos en el plano vertical-------------
            pie = BoxLayout(orientation ='vertical')

            bienvenida = Button(text = "Seleccione la respuesta",background_color = (0,0.4,1,0.8))
            bienvenida.bind(on_press=callback)

            textinput = TextInput()
            textinput.bind(text=on_text)

            null = Label(text = "")
            null2 = Label(text = "")

            pie.add_widget(null)
            pie.add_widget(null2)
            pie.add_widget(textinput)
            pie.add_widget(bienvenida)

            #Salida por pantalla final------------------------------------------
            superBox.add_widget(cabecera)
            superBox.add_widget(pie)

            #Mostrar layout completo--------------------------------------------
            return superBox
            #Fin interfaz-------------------------------------------------------

        #Comprobación turnos o vidas--------------------------------------------
        if modo_supervivencia == 0:
            if ContadorPreguntas == numPreguntas:
                MathGameResultado().run()
        else:
            if vida == 0:
                MathGameResultado().run()

class MathGameRestas(App):

    global ContadorPreguntas
    ContadorPreguntas = 0

    global puntuacion
    puntuacion = 0

    def build(self):

        global resultadoreal
        resultadoreal = 0

        global vidaMostrar
        global vida
        global vidascii

        #Función que registra el botón seleccionado-----------------------------
        def callback(instance):

            global ContadorPreguntas
            global puntuacion
            global comprobacion

            #Gestión de la excepción al presionar botón sin introducir nada-----
            try:
                respuestaOperaciones = resultadoAintroducir #contiene el string del boton
            except:
                respuestaOperaciones = 998003
            #-------------------------------------------------------------------

            print(respuestaOperaciones)
            if respuestaOperaciones == resultadoreal:
                puntuacion = puntuacion + 1
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                ContadorPreguntas = ContadorPreguntas + 1
                comprobacion = 1
                MathGameComprobacion().run()
            else:
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                ContadorPreguntas = ContadorPreguntas + 1
                comprobacion = 0
                MathGameComprobacion().run()
        #-----------------------------------------------------------------------

        #Función que registra contenido del input box---------------------------
        def on_text(instance, value):

            global resultadoAintroducir
            print('The widget', instance, 'have:', value)

            try:
                value = int(value)
                resultadoAintroducir = value
            except:
                resultadoAintroducir = 998003
        #-----------------------------------------------------------------------

        while ContadorPreguntas < numPreguntas or vida != 0:

            #Modulo Restas
            randomnumero1 = 0
            randomnumero2 = 0
            resultadoreal = 0
            solucion = 0
            #-------------------------------------------------------------------

            print("Restas entre dos numeros:")
            print("")
            randomnumero1=(randrange(RangoMin,RangoMax))          #Rango de resta
            randomnumero2=(randrange(RangoMin,RangoMax))          #Rango de resta
            mostrarnumero1 = str(randomnumero1)
            mostrarnumero2 = str(randomnumero2)
            print(randomnumero1,"-",randomnumero2)
            resultadoreal = randomnumero1-randomnumero2           #Resultadoreal
            resultadoreal = int(resultadoreal)              #Convertir a Integer

            #Debugging----------------------------------------------------------
            print(resultadoreal)
            #-------------------------------------------------------------------

            #Interfaz-----------------------------------------------------------
            #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
            superBox = BoxLayout(orientation ='vertical')

            #Widgets de cabecera añadidos en el plano horizontal----------------
            cabecera = BoxLayout(orientation ='horizontal')

            if modo_supervivencia == 1:

                vidaStr = str(vida)
                consola = Label(text = "Tienes "+vidaStr+" vidas "+"|"+" Restas entre dos numeros: "+mostrarnumero1+" - "+mostrarnumero2)

            else:

                consola = Label(text = "Sumas entre dos numeros: "+mostrarnumero1+" + "+mostrarnumero2)

            cabecera.add_widget(consola)

            #Widgets de pie de página añadidos en el plano vertical-------------
            pie = BoxLayout(orientation ='vertical')

            bienvenida = Button(text = "Seleccione la respuesta",background_color = (0,0.4,1,0.8))
            bienvenida.bind(on_press=callback)

            textinput = TextInput()
            textinput.bind(text=on_text)

            null = Label(text = "")
            null2 = Label(text = "")

            pie.add_widget(null)
            pie.add_widget(null2)
            pie.add_widget(textinput)
            pie.add_widget(bienvenida)

            #Salida por pantalla final------------------------------------------
            superBox.add_widget(cabecera)
            superBox.add_widget(pie)

            #Mostrar layout completo--------------------------------------------
            return superBox
            #Fin interfaz-------------------------------------------------------

        #Comprobación turnos o vidas--------------------------------------------
        if modo_supervivencia == 0:
            if ContadorPreguntas == numPreguntas:
                MathGameResultado().run()
        else:
            if vida == 0:
                MathGameResultado().run()

class MathGameSumas(App):

    global ContadorPreguntas
    ContadorPreguntas = 0

    global puntuacion
    puntuacion = 0

    def build(self):

        global resultadoreal
        resultadoreal = 0

        global vidaMostrar
        global vida
        global vidascii

        #Función que registra el botón seleccionado-----------------------------
        def callback(instance):

            global puntuacion
            global ContadorPreguntas
            global comprobacion

            #Gestión de la excepción al presionar botón sin introducir nada-----
            try:
                respuestaOperaciones = resultadoAintroducir #contiene el string del boton
            except:
                respuestaOperaciones = 998003
            #-------------------------------------------------------------------

            print(respuestaOperaciones)
            if respuestaOperaciones == resultadoreal:
                puntuacion = puntuacion + 1
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                ContadorPreguntas = ContadorPreguntas + 1
                comprobacion = 1
                MathGameComprobacion().run()
            else:
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                ContadorPreguntas = ContadorPreguntas + 1
                comprobacion = 0
                MathGameComprobacion().run()
        #-----------------------------------------------------------------------

        #Funcion que registra contenido del input-------------------------------
        def on_text(instance, value):

            global resultadoAintroducir
            print('The widget', instance, 'have:', value)

            try:
                value = int(value)
                resultadoAintroducir = value
            except:
                resultadoAintroducir = 998003
        #-----------------------------------------------------------------------

        while ContadorPreguntas < numPreguntas or vida != 0:

            #Modulo Sumas
            randomnumero1 = 0
            randomnumero2 = 0
            resultadoreal = 0
            solucion = 0
            #-------------------------------------------------------------------

            print("Sumas entre dos numeros:")
            print("")
            randomnumero1=(randrange(RangoMin,RangoMax))          #Rango de suma
            randomnumero2=(randrange(RangoMin,RangoMax))          #Rango de suma
            mostrarnumero1 = str(randomnumero1)
            mostrarnumero2 = str(randomnumero2)
            print(randomnumero1,"+",randomnumero2)
            resultadoreal = randomnumero1+randomnumero2           #Resultadoreal
            resultadoreal = int(resultadoreal)              #Convertir a Integer

            #Debugging----------------------------------------------------------
            print(resultadoreal)
            #-------------------------------------------------------------------

            #Interfaz-----------------------------------------------------------
            #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
            superBox = BoxLayout(orientation ='vertical')

            #Widgets de cabecera añadidos en el plano horizontal----------------
            cabecera = BoxLayout(orientation ='horizontal')

            if modo_supervivencia == 1:

                vidaStr = str(vida)
                consola = Label(text = "Tienes "+vidaStr+" vidas "+"|"+" Sumas entre dos numeros: "+mostrarnumero1+" + "+mostrarnumero2)

            else:

                consola = Label(text = "Sumas entre dos numeros: "+mostrarnumero1+" + "+mostrarnumero2)

            cabecera.add_widget(consola)

            #Widgets de pie de página añadidos en el plano vertical-------------
            pie = BoxLayout(orientation ='vertical')

            bienvenida = Button(text = "Seleccione la respuesta",background_color = (0,0.4,1,0.8))
            bienvenida.bind(on_press=callback)

            textinput = TextInput()
            textinput.bind(text=on_text)

            null = Label(text = "")
            null2 = Label(text = "")

            pie.add_widget(null)
            pie.add_widget(null2)
            pie.add_widget(textinput)
            pie.add_widget(bienvenida)

            #Salida por pantalla final------------------------------------------
            superBox.add_widget(cabecera)
            superBox.add_widget(pie)

            #Mostrar layout completo--------------------------------------------
            return superBox
            #Fin interfaz-------------------------------------------------------

        #Comprobación turnos o vidas--------------------------------------------
        if modo_supervivencia == 0:
            if ContadorPreguntas == numPreguntas:
                MathGameResultado().run()
        else:
            if vida == 0:
                MathGameResultado().run()

class MathGameSelOpe(App):

    def build(self):

        #Función que registra el botón seleccionado-----------------------------
        def callback(instance):

            global operacion

            respuestaOperaciones = instance.text #contiene el string del boton
            print(instance.text)

            if respuestaOperaciones == "Sumas":
                operacion = "Sumas"
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameSumas().run()
            else:
                if respuestaOperaciones == "Restas":
                    operacion = "Restas"
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)
                    MathGameRestas().run()
                else:
                    if respuestaOperaciones == "Multiplicaciones":
                        operacion = "Multiplicaciones"
                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)
                        MathGameMultiplicaciones().run()
                    else:
                        operacion = "Divisiones"
                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)
                        MathGameDivisiones().run()

        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal
        cabecera = BoxLayout(orientation ='horizontal')

        consola = Label(text = "¡Bienvenido a MathGame Android Edition! v"+version)

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical
        pie = BoxLayout(orientation ='vertical')

        bienvenida = Label(text = "Seleccione tipo de problemas")

        sumas = Button(text = "Sumas",background_color = (0,0.4,1,0.8))
        sumas.bind(on_press=callback)

        restas = Button(text = "Restas",background_color = (0,0.4,1,0.8))
        restas.bind(on_press=callback)

        multiplicaciones = Button(text = "Multiplicaciones",background_color = (0,0.4,1,0.8))
        multiplicaciones.bind(on_press=callback)

        divisiones = Button(text = "Divisiones",background_color = (0,0.4,1,0.8))
        divisiones.bind(on_press=callback)

        pie.add_widget(bienvenida)
        pie.add_widget(sumas)
        pie.add_widget(restas)
        pie.add_widget(multiplicaciones)
        pie.add_widget(divisiones)

        #Salida por pantalla final
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

        #Mostrar layout completo
        return superBox

class MathGameP(App):

    def build(self):

        #Funcion que registra el botón seleccionado-----------------------------
        def callback(instance):

            global numPreguntas

            respuestaPreguntas = instance.text #contiene el string del boton
            print(instance.text)
            if respuestaPreguntas == "1":
                numPreguntas = 1
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameSelOpe().run()
            else:
                if respuestaPreguntas == "2":
                    numPreguntas = 2
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)
                    MathGameSelOpe().run()
                else:
                    if respuestaPreguntas == "3":
                        numPreguntas = 3
                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)
                        MathGameSelOpe().run()
                    else:
                        if respuestaPreguntas == "4":
                            numPreguntas = 4
                            superBox.remove_widget(pie)
                            superBox.remove_widget(cabecera)
                            MathGameSelOpe().run()
                        else:
                            numPreguntas = 5
                            superBox.remove_widget(pie)
                            superBox.remove_widget(cabecera)
                            MathGameSelOpe().run()

        #Interfaz---------------------------------------------------------------
        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal')

        #Elementos de cabecera--------------------------------------------------
        consola = Label(text = "¡Bienvenido a MathGame Android Edition! v"+version)

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Elementos del pie------------------------------------------------------
        bienvenida = Label(text = "Cuántas preguntas quieres (del 1 al 5)")

        uno = Button(text = "1",background_color = (0,0.4,1,0.8))
        uno.bind(on_press=callback)

        dos = Button(text = "2",background_color = (0,0.4,1,0.8))
        dos.bind(on_press=callback)

        tres = Button(text = "3",background_color = (0,0.4,1,0.8))
        tres.bind(on_press=callback)

        cuatro = Button(text = "4",background_color = (0,0.4,1,0.8))
        cuatro.bind(on_press=callback)

        cinco = Button(text = "5",background_color = (0,0.4,1,0.8))
        cinco.bind(on_press=callback)

        #Añadir elementos a pie-------------------------------------------------
        pie.add_widget(bienvenida)
        pie.add_widget(uno)
        pie.add_widget(dos)
        pie.add_widget(tres)
        pie.add_widget(cuatro)
        pie.add_widget(cinco)

        #Salida por pantalla final
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

        #Mostrar layout completo
        return superBox
        #Fin Interfaz-----------------------------------------------------------

class MathGameS(App):

    def build(self):

        #Función que registra el texto del botón seleccionado-------------------
        def callback(instance):

            global modo_supervivencia
            global numPreguntas
            global vida
            global vidascii

            respuestaSupervivencia = instance.text #contiene el string del boton
            print(instance.text)
            if respuestaSupervivencia == "Si":

                modo_supervivencia = 1
                vida = 5

                vidascii = "♥"
                numPreguntas = 0

                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameSelOpe().run()

            else:

                modo_supervivencia = 0
                vida = 0
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameP().run()

        #Interfaz---------------------------------------------------------------
        #Layout global----------------------------------------------------------
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal')

        consola = Label(text = "¡Bienvenido a MathGame Android Edition! v"+version)

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Creación de elementos--------------------------------------------------
        bienvenida = Label(text = "¿Quieres activar el modo supervivencia?")

        aceptar = Button(text = "Si",background_color = (0,0.4,1,0.8))
        aceptar.bind(on_press=callback)

        rechazar = Button(text = "No",background_color = (0,0.4,1,0.8))
        rechazar.bind(on_press=callback)

        #Añadir elementos a pie-------------------------------------------------
        pie.add_widget(bienvenida)
        pie.add_widget(aceptar)
        pie.add_widget(rechazar)

        #Salida por pantalla final----------------------------------------------
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

        #Mostrar layout completo
        return superBox
        #Fin Interfaz-----------------------------------------------------------

class MathGameD(App):

    def build(self):

        #Función que detecta el texto del botón seleccionado en pantalla--------
        def callback(instance):

            global dificultad
            global RangoMin
            global RangoMax
            global MultiPuntuacion

            dificultadSeleccionada = instance.text #contiene el string del boton
            print(instance.text)
            if dificultadSeleccionada == "Fácil":
                dificultad = "F"
                RangoMin = 0
                RangoMax = 9
                MultiPuntuacion = 1
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameS().run()
            else:
                if dificultadSeleccionada == "Normal":
                    dificultad = "N"
                    RangoMin = 10
                    RangoMax = 99
                    MultiPuntuacion = 2
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)
                    MathGameS().run()
                else:
                    dificultad = "D"
                    RangoMin = 100
                    RangoMax = 999
                    MultiPuntuacion = 3
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)
                    MathGameS().run()
        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal') #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        consola = Label(text = "¡Bienvenido a MathGame Android Edition! v"+version)

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        bienvenida = Label(text = "Seleccione dificultad")

        dificultadFacil = Button(text = "Fácil",background_color = (0,0.4,1,0.8))
        dificultadFacil.bind(on_press=callback)

        dificultadNormal = Button(text = "Normal",background_color = (0,0.4,1,0.8))
        dificultadNormal.bind(on_press=callback)

        dificultadDificil = Button(text = "Dificil",background_color = (0,0.4,1,0.8))
        dificultadDificil.bind(on_press=callback)

        #Añadir elementos al pie------------------------------------------------
        pie.add_widget(bienvenida)
        pie.add_widget(dificultadFacil)
        pie.add_widget(dificultadNormal)
        pie.add_widget(dificultadDificil)

        #Añadir cada división al layout global----------------------------------
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

        #Mostrar layout completo------------------------------------------------
        return superBox
        #Fin Interfaz-----------------------------------------------------------

class MathGame(App):

    def build(self):

        #Función que detecta el texto del botón seleccionado en pantalla--------
        def callback(instance):

            Seleccion = instance.text #contiene el string del boton
            print(instance.text)
            if Seleccion == "Jugar":
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameD().run()
            else:
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGamePuntuacion().run()
        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal') #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        consola = Label(text = "¡Bienvenido a MathGame Android Edition! v"+version)

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        jugar = Button(text = "Jugar",background_color = (0,0.4,1,0.8))
        jugar.bind(on_press=callback)

        puntuacion = Button(text = "Puntuación",background_color = (0,0.4,1,0.8))
        puntuacion.bind(on_press=callback)

        null = Label(text = "")
        null2 = Label(text = "")

        #Añadir elementos al pie------------------------------------------------
        pie.add_widget(null)
        pie.add_widget(null2)
        pie.add_widget(jugar)
        pie.add_widget(puntuacion)

        #Añadir cada división al layout global----------------------------------
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

        #Mostrar layout completo------------------------------------------------
        return superBox
        #Fin Interfaz-----------------------------------------------------------

#Constructor--------------------------------------------------------------------
MathGame().run()
