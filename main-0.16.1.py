#!/usr/bin/python3
version = "0.16.1"

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from random import randrange
from kivy.uix.image import Image

#Insertar color al cambiar de ventana-------------------------------------------
from kivy.core.window import Window
Window.clearcolor = (0.1,0.2,0.4,1)
#-------------------------------------------------------------------------------

#Permitir la recursividad (temporal)--------------------------------------------
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29,-1))
sys.setrecursionlimit(10**6)
#-------------------------------------------------------------------------------

#Creación y procesado de archivos-----------------------------------------------
def funArchivos():

    global idiomaApp

    #Creacion Archivo Idioma----------------------------------------------------
    try:

        archivo = open("./idioma.txt", "x")
        archivo.write("")
        archivo.close()
        global idiomaFirstRun
        idiomaFirstRun = 1

    except:

        idiomaDif = open("./idioma.txt", "r")
        contenidoIdioma = idiomaDif.read()

        idiomaApp = contenidoIdioma
    #---------------------------------------------------------------------------

    #Creacion Archivo Puntuaciones----------------------------------------------
    try:
        archivo = open("./points.txt", "x")
        archivo.write("0")
        archivo.close()
    except:
        print("Archivo 1")
    #---------------------------------------------------------------------------

    #Creacion Archivo Ajustes---------------------------------------------------
    global firstRun
    firstRun = 0

    global modo_ajustes

    try:
        ajustesFile = open("./ajustes.txt", "x")
        ajustesFile.write("0")
        ajustesFile.close()
        modo_ajustes = 0
        firstRun = 1
    except:
        global RangoMin
        global RangoMax
        global modo_supervivencia
        global vida
        global numPreguntas
        global MultiPuntuacion
        global mostrar_modo_problemas
        global mostrar_modo_dificultad
        global mostrar_modo_numPreguntas

        ajustesFile = open("./ajustes.txt", "r")
        contenidoAjustes = ajustesFile.read()

        #Procesado del archivo de ajustes---------------------------------------
        if contenidoAjustes == "09150":
            modo_ajustes = 1
            RangoMin = 0
            RangoMax = 9
            modo_supervivencia = 1
            vida = 5
            numPreguntas = 0
            MultiPuntuacion = 1
            mostrar_modo_dificultad = "(Fácil)"
            mostrar_modo_numPreguntas = "(Supervivencia)"

        if contenidoAjustes == "1099150":
            modo_ajustes = 1
            RangoMin = 10
            RangoMax = 99
            modo_supervivencia = 1
            vida = 5
            numPreguntas = 0
            MultiPuntuacion = 2
            mostrar_modo_dificultad = "(Normal)"
            mostrar_modo_numPreguntas = "(Supervivencia)"

        if contenidoAjustes == "100999150":
            modo_ajustes = 1
            RangoMin = 100
            RangoMax = 999
            modo_supervivencia = 1
            vida = 5
            numPreguntas = 0
            MultiPuntuacion = 3
            mostrar_modo_dificultad = "(Dificil)"
            mostrar_modo_numPreguntas = "(Supervivencia)"

        if contenidoAjustes == "09001":
            modo_ajustes = 1
            RangoMin = 0
            RangoMax = 9
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 1
            MultiPuntuacion = 1
            mostrar_modo_dificultad = "(Fácil)"
            mostrar_modo_numPreguntas = "(1)"

        if contenidoAjustes == "09002":
            modo_ajustes = 1
            RangoMin = 0
            RangoMax = 9
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 2
            MultiPuntuacion = 1
            mostrar_modo_dificultad = "(Fácil)"
            mostrar_modo_numPreguntas = "(2)"

        if contenidoAjustes == "09003":
            modo_ajustes = 1
            RangoMin = 0
            RangoMax = 9
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 3
            MultiPuntuacion = 1
            mostrar_modo_dificultad = "(Fácil)"
            mostrar_modo_numPreguntas = "(3)"

        if contenidoAjustes == "09004":
            modo_ajustes = 1
            RangoMin = 0
            RangoMax = 9
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 4
            MultiPuntuacion = 1
            mostrar_modo_dificultad = "(Fácil)"
            mostrar_modo_numPreguntas = "(4)"

        if contenidoAjustes == "09005":
            modo_ajustes = 1
            RangoMin = 0
            RangoMax = 9
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 5
            MultiPuntuacion = 1
            mostrar_modo_dificultad = "(Fácil)"
            mostrar_modo_numPreguntas = "(5)"

        if contenidoAjustes == "1099001":
            modo_ajustes = 1
            RangoMin = 10
            RangoMax = 99
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 1
            MultiPuntuacion = 2
            mostrar_modo_dificultad = "(Normal)"
            mostrar_modo_numPreguntas = "(1)"

        if contenidoAjustes == "1099002":
            modo_ajustes = 1
            RangoMin = 10
            RangoMax = 99
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 2
            MultiPuntuacion = 2
            mostrar_modo_dificultad = "(Normal)"
            mostrar_modo_numPreguntas = "(2)"

        if contenidoAjustes == "1099003":
            modo_ajustes = 1
            RangoMin = 10
            RangoMax = 99
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 3
            MultiPuntuacion = 2
            mostrar_modo_dificultad = "(Normal)"
            mostrar_modo_numPreguntas = "(3)"

        if contenidoAjustes == "1099004":
            modo_ajustes = 1
            RangoMin = 10
            RangoMax = 99
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 4
            MultiPuntuacion = 2
            mostrar_modo_dificultad = "(Normal)"
            mostrar_modo_numPreguntas = "(4)"

        if contenidoAjustes == "1099005":
            modo_ajustes = 1
            RangoMin = 10
            RangoMax = 99
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 5
            MultiPuntuacion = 2
            mostrar_modo_dificultad = "(Normal)"
            mostrar_modo_numPreguntas = "(5)"

        if contenidoAjustes == "100999001":
            modo_ajustes = 1
            RangoMin = 100
            RangoMax = 999
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 1
            MultiPuntuacion = 3
            mostrar_modo_dificultad = "(Dificil)"
            mostrar_modo_numPreguntas = "(1)"

        if contenidoAjustes == "100999002":
            modo_ajustes = 1
            RangoMin = 100
            RangoMax = 999
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 2
            MultiPuntuacion = 3
            mostrar_modo_dificultad = "(Dificil)"
            mostrar_modo_numPreguntas = "(2)"

        if contenidoAjustes == "100999003":
            modo_ajustes = 1
            RangoMin = 100
            RangoMax = 999
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 3
            MultiPuntuacion = 3
            mostrar_modo_dificultad = "(Dificil)"
            mostrar_modo_numPreguntas = "(3)"

        if contenidoAjustes == "100999004":
            modo_ajustes = 1
            RangoMin = 100
            RangoMax = 999
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 4
            MultiPuntuacion = 3
            mostrar_modo_dificultad = "(Dificil)"
            mostrar_modo_numPreguntas = "(4)"

        if contenidoAjustes == "100999005":
            modo_ajustes = 1
            RangoMin = 100
            RangoMax = 999
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 5
            MultiPuntuacion = 3
            mostrar_modo_dificultad = "(Dificil)"
            mostrar_modo_numPreguntas = "(5)"

        if contenidoAjustes == "0":
            modo_ajustes = 0
            firstRun = 1
        #-----------------------------------------------------------------------

        print("Archivo Ajustes 1")
    #---------------------------------------------------------------------------

    #Creacion Archivo Dificultad------------------------------------------------
    try:
        ajustesDif = open("./ajustes2.txt", "x")
        ajustesDif.write("0")
        ajustesDif.close()
    except:
        global respuestaOperaciones
        global operacion

        ajustesDif = open("./ajustes2.txt", "r")
        contenidoAjustes2 = ajustesDif.read()

        #Procesado del archivo de ajustes---------------------------------------
        if contenidoAjustes2 == "Sumas":
            respuestaOperaciones = "Sumas"
            operacion = "Sumas"
            mostrar_modo_problemas = "(Sumas)"

        if contenidoAjustes2 == "Restas":
            respuestaOperaciones = "Restas"
            operacion = "Restas"
            mostrar_modo_problemas = "(Restas)"

        if contenidoAjustes2 == "Multiplicaciones":
            respuestaOperaciones = "Multiplicaciones"
            operacion = "Multiplicaciones"
            mostrar_modo_problemas = "(Multiplicaciones)"

        if contenidoAjustes2 == "Divisiones":
            respuestaOperaciones = "Divisiones"
            operacion = "Divisiones"
            mostrar_modo_problemas = "(Divisiones)"
        #-----------------------------------------------------------------------

        print("Archivo Dificultad 1")
    #---------------------------------------------------------------------------
funArchivos()
#-------------------------------------------------------------------------------

#Necesario para la música-------------------------------------------------------
#from kivy.core.audio import SoundLoader
#victory = SoundLoader.load('./data/audio/victory.wav')
#-------------------------------------------------------------------------------

class MathGameSelIdioma(App):

    def build(self):

        #Función que detecta el texto del botón seleccionado en pantalla--------
        def callback(instance):

            global modo_ajustes
            global idiomaFirstRun
            global idiomaApp

            archivo = open("./idioma.txt", "w")

            Seleccion = instance.text #contiene el string del boton
            print(instance.text)

            if Seleccion == "Español":

                archivo.write("Es")
                archivo.close()
                idiomaApp = "Es"

            else:

                archivo.write("En")
                archivo.close()
                idiomaApp = "En"

            idiomaFirstRun = 0 #Se deshabilita la configuración inicial---------

            #Liberación de elementos gráficos-----------------------------------
            superBox.remove_widget(cabecera)
            superBox.remove_widget(pie)
            #-------------------------------------------------------------------

            if modo_ajustes == 1:
                MathGameAjustes().run()
            else:
                MathGame().run()

        #Interfaz---------------------------------------------------------------
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')
        cabecera = BoxLayout(orientation ='vertical')
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos--------------------------------------------------------
        header = Image(source="./data/idiomas.png")

        español = Button(text = "Español",background_color = (0.1,0.2,0.6,0.6))
        español.bind(on_press=callback)

        english = Button(text = "English",background_color = (0.1,0.2,0.6,0.6))
        english.bind(on_press=callback)

        espacio0 = Label()
        espacio1 = Label()

        #Añadir elementos-------------------------------------------------------
        cabecera.add_widget(header)

        pie.add_widget(espacio0)
        pie.add_widget(español)
        pie.add_widget(english)
        pie.add_widget(espacio1)

        superBox.add_widget(cabecera)
        superBox.add_widget(pie)
        #Mostrar layout completo------------------------------------------------
        return superBox
        #Fin Interfaz-----------------------------------------------------------

class MathGameDrakePreview(App):

    global pag
    pag = 0

    def build(self):

        global pag

        #Función que detecta el texto del botón seleccionado en pantalla--------
        def callback(instance):

            Seleccion = instance.text #contiene el string del boton
            print(instance.text)

            global pag

            if pag < 5:
                superBox.remove_widget(cabecera)
                superBox.remove_widget(pie)
                MathGameDrakePreview().run()
            else:
                pag = 0
                superBox.remove_widget(cabecera)
                superBox.remove_widget(pie)
                MathGameDrake().run()
        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal') #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        if pag == 0:
            consola = Label(text = '''La ecuación de Drake o fórmula de Drake es
una ecuación para estimar la cantidad de
civilizaciones en nuestra galaxia, la Vía
Láctea, susceptibles de poseer emisiones
de radio detectables.

Fue concebida en 1961 por el radioastrónomo
Frank Drake, presidente del instituto SETI,
mientras trabajaba en el Observatorio
Nacional de Radioastronomía en Green Bank
(estado de Virginia Occidental [EE. UU.]).''')
            pag = pag + 1
        else:
            if pag == 1:
                consola = Label(text = '''La ecuación de Drake identifica los factores
específicos que, se cree, tienen un papel
importante en el desarrollo de las civilizaciones.

Aunque en la actualidad no hay datos
suficientes para resolver la ecuación,
la comunidad científica ha aceptado su
relevancia como primera aproximación teórica
al problema, y varios científicos la han
utilizado como herramienta para plantear
distintas hipótesis.''')
                pag = pag + 1
            else:
                if pag == 2:
                    consola = Label(text = '''Nuestro Sol es solo una estrella solitaria
en la abundancia de 7×10^22 estrellas en
el universo observable.

La Vía Láctea es solo una de entre las
2 000 000 000 000 [dos billones] de
galaxias del universo.

Parecería entonces que debería haber
plenitud de vida allí afuera.''')
                    pag = pag + 1
                else:
                    if pag == 3:
                        consola = Label(text = '''


La ecuación es la siguiente:

N  = Número de civilizaciones que podrían
        comunicarse en nuestra galaxia,
        la Vía Láctea.

R* = Ritmo anual de formación de estrellas
        "adecuadas" en la galaxia.

Fp = Fracción de estrellas que tienen
        planetas en su órbita.

Ne = Número de esos planetas orbitando
         dentro de la zona de habitabilidad
         de la estrella (las órbitas cuya
         distancia a la estrella no sea tan
         próxima como para ser demasiado
         calientes, ni tan lejana como para
         ser demasiado frías para poder
         albergar vida.''')
                        pag = pag + 1
                    else:
                        consola = Label(text = '''Fl = Fracción de esos planetas
       dentro de la zona de habitabilidad en
       los que la vida se ha desarrollado

Fi = Fracción de esos planetas en los
       que la vida inteligente se ha
       desarrollado.

Fc = Fracción de esos planetas donde
        la vida inteligente ha desarrollado
        una tecnología e intenta comunicarse.

L  = Lapso, medido en años, durante el
       que una civilización inteligente y
       comunicativa puede existir.''')

                        pag = pag + 1

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        aceptar = Button(text = "Siguiente",background_color = (0.1,0.2,0.6,0.6))
        aceptar.bind(on_press=callback)

        null1 = Label()
        null2 = Label()

        #Añadir elementos al pie------------------------------------------------
        pie.add_widget(null1)
        pie.add_widget(null2)
        pie.add_widget(aceptar)

        #Añadir cada división al layout global----------------------------------
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

        #Mostrar layout completo------------------------------------------------
        return superBox
        #Fin Interfaz-----------------------------------------------------------

class MathGameDrakeV(App):

    def build(self):

        global resultadoAintroducir
        resultadoAintroducir = "0"

        #Funcion que registra contenido del input-------------------------------
        def on_text(instance, value):

            global resultadoAintroducir
            print('The widget', instance, 'have:', value)

            resultadoAintroducir = value
            validacionFloat = resultadoAintroducir

            try:
                validacionFloat = float(validacionFloat)
            except:
                resultadoAintroducir = "0"
        #-----------------------------------------------------------------------

        #Función que detecta el texto del botón seleccionado en pantalla--------
        def callback(instance):

            Seleccion = instance.text #contiene el string del boton
            print(instance.text)

            global vR
            global vFp
            global vNe
            global vFl
            global vFi
            global vFc
            global vL

            try:
                if SeleccionEcuacion == "R*":
                    vR = resultadoAintroducir
                    global Var1
                    Var1 = float(vR)
                else:
                    if SeleccionEcuacion == "Fp":
                        vFp = resultadoAintroducir
                        global Var2
                        Var2 = float(vFp)
                    else:
                        if SeleccionEcuacion == "Ne":
                            vNe = resultadoAintroducir
                            global Var3
                            Var3 = float(vNe)
                        else:
                            if SeleccionEcuacion == "Fl":
                                vFl = resultadoAintroducir
                                global Var4
                                Var4 = float(vFl)
                            else:
                                if SeleccionEcuacion == "Fi":
                                    vFi = resultadoAintroducir
                                    global Var5
                                    Var5 = float(vFi)
                                else:
                                    if SeleccionEcuacion == "Fc":
                                        vFc = resultadoAintroducir
                                        global Var6
                                        Var6 = float(vFc)
                                    else:
                                        vL = resultadoAintroducir
                                        global Var7
                                        Var7 = float(vL)
            except:
                print("No se introdujo valor en Drake")

            superBox.remove_widget(cabecera)
            superBox.remove_widget(pie)
            MathGameDrake().run()
        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal') #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        if SeleccionEcuacion == "R*":
            consola = Label(text = '''(R*) Seleccione el ritmo anual de formación
de estrellas adecuadas en la galaxia.

Según datos de la nasa es de 1,379''')
        else:
            if SeleccionEcuacion == "Fp":
                consola = Label(text = '''(Fp) Seleccione la fracción de estrellas que tienen
planetas en su órbita.

Según datos del Observatorio Europeo Austral
es de 0,333''')
            else:
                if SeleccionEcuacion == "Ne":
                    consola = Label(text = '''(Ne) Seleccione el número de esos planetas
orbitando dentro de la zona de habitabilidad de
la estrella.

Se estima que es de 0.005''')
                else:
                    if SeleccionEcuacion == "Fl":
                        consola = Label(text = '''(Fl) Seleccione la fracción de esos planetas dentro
de la zona de habitabilidad en los que la vida se
ha desarrollado.

Se estima que es de 0.13.''')
                    else:
                        if SeleccionEcuacion == "Fi":
                            consola = Label(text = '''(Fi) Seleccione la fracción de esos planetas en los
que la vida inteligente se ha desarrollado.

Se estima que es de 0.000054''')
                        else:
                            if SeleccionEcuacion == "Fc":
                                consola = Label(text = '''(Fc) Seleccione la fracción de esos planetas donde
la vida inteligente ha desarrollado una tecnología
e intenta comunicarse.

Se estima que es de 0.0021''')
                            else:
                                consola = Label(text = '''(L) Seleccione el lapso, medido en años, durante
el que una civilización inteligente y comunicativa
puede existir.

Se estima que es de 420 años.''')

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        aceptar = Button(text = "Vale",background_color = (0.1,0.2,0.6,0.6))
        aceptar.bind(on_press=callback)

        textinput = TextInput()
        textinput.bind(text=on_text)

        null1 = Label()
        null2 = Label()

        #Añadir elementos al pie------------------------------------------------
        pie.add_widget(null1)
        pie.add_widget(null2)
        pie.add_widget(textinput)
        pie.add_widget(aceptar)

        #Añadir cada división al layout global----------------------------------
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

        #Mostrar layout completo------------------------------------------------
        return superBox
        #Fin Interfaz-----------------------------------------------------------

class MathGameDrake(App):

    global vR
    global vFp
    global vNe
    global vFl
    global vFi
    global vFc
    global vL

    vR = "R*"
    vFp = "Fp"
    vNe = "Ne"
    vFl = "Fl"
    vFi = "Fi"
    vFc = "Fc"
    vL = "L"

    def build(self):

        #Función que detecta el texto del botón seleccionado en pantalla--------
        def callback(instance):

            global vR
            global vFp
            global vNe
            global vFl
            global vFi
            global vFc
            global vL

            global Var1
            global Var2
            global Var3
            global Var4
            global Var5
            global Var6
            global Var7

            Seleccion = instance.text #contiene el string del boton
            print(instance.text)

            if Seleccion == "Volver":
                superBox.remove_widget(pie)
                superBox.remove_widget(cuerpo)
                superBox.remove_widget(cabecera)
                MathGame().run()
            else:
                if Seleccion == "Reset":

                    vR = "R*"
                    vFp = "Fp"
                    vNe = "Ne"
                    vFi = "Fi"
                    vFl = "Fl"
                    vFc = "Fc"
                    vL = "L"

                    Var1 = "0"
                    Var2 = "0"
                    Var3 = "0"
                    Var4 = "0"
                    Var5 = "0"
                    Var6 = "0"
                    Var7 = "0"

                    superBox.remove_widget(pie)
                    superBox.remove_widget(cuerpo)
                    superBox.remove_widget(cabecera)
                    MathGameDrake().run()
                else:
                    if Seleccion == "Ecuación Original":

                        vR = "10"
                        vFp = "0.5"
                        vNe = "2"
                        vFi = "1"
                        vFl = "0.01"
                        vFc = "0.01"
                        vL = "10000"

                        Var1 = 10
                        Var2 = 0.5
                        Var3 = 2
                        Var4 = 1
                        Var5 = 0.01
                        Var6 = 0.01
                        Var7 = 10000

                        superBox.remove_widget(pie)
                        superBox.remove_widget(cuerpo)
                        superBox.remove_widget(cabecera)
                        MathGameDrake().run()

                    else:
                        superBox.remove_widget(pie)
                        superBox.remove_widget(cuerpo)
                        superBox.remove_widget(cabecera)
                        MathGameDrake().run()
        #-----------------------------------------------------------------------
        #Binding R*-------------------------------------------------------------
        def funR(instance):

            Seleccion = "R*"

            global SeleccionEcuacion
            SeleccionEcuacion = Seleccion

            superBox.remove_widget(pie)
            superBox.remove_widget(cuerpo)
            superBox.remove_widget(cabecera)
            MathGameDrakeV().run()
        #-----------------------------------------------------------------------

        #Binding Fp*-------------------------------------------------------------
        def funFp(instance):

            Seleccion = "Fp"

            global SeleccionEcuacion
            SeleccionEcuacion = Seleccion

            superBox.remove_widget(pie)
            superBox.remove_widget(cuerpo)
            superBox.remove_widget(cabecera)
            MathGameDrakeV().run()
        #-----------------------------------------------------------------------

        #Binding Ne*-------------------------------------------------------------
        def funNe(instance):

            Seleccion = "Ne"

            global SeleccionEcuacion
            SeleccionEcuacion = Seleccion

            superBox.remove_widget(pie)
            superBox.remove_widget(cuerpo)
            superBox.remove_widget(cabecera)
            MathGameDrakeV().run()
        #-----------------------------------------------------------------------

        #Binding Fl*-------------------------------------------------------------
        def funFl(instance):

            Seleccion = "Fl"

            global SeleccionEcuacion
            SeleccionEcuacion = Seleccion

            superBox.remove_widget(pie)
            superBox.remove_widget(cuerpo)
            superBox.remove_widget(cabecera)
            MathGameDrakeV().run()
        #-----------------------------------------------------------------------

        #Binding Fi-------------------------------------------------------------
        def funFi(instance):

            Seleccion = "Fi"

            global SeleccionEcuacion
            SeleccionEcuacion = Seleccion

            superBox.remove_widget(pie)
            superBox.remove_widget(cuerpo)
            superBox.remove_widget(cabecera)
            MathGameDrakeV().run()
        #-----------------------------------------------------------------------

        #Binding Fc-------------------------------------------------------------
        def funFc(instance):

            Seleccion = "Fc"

            global SeleccionEcuacion
            SeleccionEcuacion = Seleccion

            superBox.remove_widget(pie)
            superBox.remove_widget(cuerpo)
            superBox.remove_widget(cabecera)
            MathGameDrakeV().run()
        #-----------------------------------------------------------------------

        #Binding L--------------------------------------------------------------
        def funL(instance):

            Seleccion = "L"

            global SeleccionEcuacion
            SeleccionEcuacion = Seleccion

            superBox.remove_widget(pie)
            superBox.remove_widget(cuerpo)
            superBox.remove_widget(cabecera)
            MathGameDrakeV().run()
        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='vertical',size_hint =(1, 0.5))

        #Crear elementos de cabecera--------------------------------------------
        try:
            resultadoDrake = Var1*Var2*Var3*Var4*Var5*Var6*Var7
            strResultadoDrake = str(resultadoDrake)
            N = Label(text = "Posibles civilizaciones detectables: "+strResultadoDrake,size_hint =(1, 0.01))

            contadorBloqueo = 1
        except:
            N = Label(text = "N =",size_hint =(1, 0.01))

        null = Label()

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(null)
        cabecera.add_widget(N)
        #-----------------------------------------------------------------------

        #Widgets de Mitad de página añadidos en el plano vertical---------------
        cuerpo = BoxLayout(orientation ='horizontal',size_hint =(1, 0.5))

        R = Button(text = vR,background_color = (0.1,0.2,0.6,0.6),size_hint =(1, 0.25))
        Fp = Button(text = vFp,background_color = (0.1,0.2,0.6,0.6),size_hint =(1, 0.25))
        Ne = Button(text = vNe,background_color = (0.1,0.2,0.6,0.6),size_hint =(1, 0.25))
        Fl = Button(text = vFl,background_color = (0.1,0.2,0.6,0.6),size_hint =(1, 0.25))
        Fi = Button(text = vFi,background_color = (0.1,0.2,0.6,0.6),size_hint =(1, 0.25))
        Fc = Button(text = vFc,background_color = (0.1,0.2,0.6,0.6),size_hint =(1, 0.25))
        L = Button(text = vL,background_color = (0.1,0.2,0.6,0.6),size_hint =(1, 0.25))

        R.bind(on_press=funR)
        Fp.bind(on_press=funFp)
        Ne.bind(on_press=funNe)
        Fl.bind(on_press=funFl)
        Fi.bind(on_press=funFi)
        Fc.bind(on_press=funFc)
        L.bind(on_press=funL)

        X = Label(text = "x",size_hint =(0.5, 0.25))
        X2 = Label(text = "x",size_hint =(0.5, 0.25))
        X3 = Label(text = "x",size_hint =(0.5, 0.25))
        X4 = Label(text = "x",size_hint =(0.5, 0.25))
        X5 = Label(text = "x",size_hint =(0.5, 0.25))
        X6 = Label(text = "x",size_hint =(0.5, 0.25))

        #Añadir elementos a cuerpo----------------------------------------------
        cuerpo.add_widget(R)
        cuerpo.add_widget(X)
        cuerpo.add_widget(Fp)
        cuerpo.add_widget(X2)
        cuerpo.add_widget(Ne)
        cuerpo.add_widget(X3)
        cuerpo.add_widget(Fl)
        cuerpo.add_widget(X4)
        cuerpo.add_widget(Fi)
        cuerpo.add_widget(X5)
        cuerpo.add_widget(Fc)
        cuerpo.add_widget(X6)
        cuerpo.add_widget(L)
        #-----------------------------------------------------------------------

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical',size_hint =(1, 1))

        #Crear elementos del pie------------------------------------------------
        volver = Button(text = "Volver",background_color = (0.1,0.2,0.6,0.6))
        volver.bind(on_press=callback)

        reset = Button(text = "Reset",background_color = (0.1,0.2,0.6,0.6))
        reset.bind(on_press=callback)

        original = Button(text = "Ecuación Original",background_color = (0.1,0.2,0.6,0.6))
        original.bind(on_press=callback)

        null = Label()
        null2 = Label()

        #Añadir elementos al pie------------------------------------------------
        pie.add_widget(null)
        pie.add_widget(null2)
        pie.add_widget(original)
        pie.add_widget(reset)
        pie.add_widget(volver)

        #Añadir cada división al layout global----------------------------------
        superBox.add_widget(cabecera)
        superBox.add_widget(cuerpo)
        superBox.add_widget(pie)

        #Mostrar layout completo------------------------------------------------
        return superBox
        #Fin Interfaz-----------------------------------------------------------

class MathGameExtras(App):

    def build(self):

        #Función que detecta el texto del botón seleccionado en pantalla--------
        def callback(instance):

            Seleccion = instance.text #contiene el string del boton
            print(instance.text)

            if Seleccion == "Ecuación de Drake":
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameDrakePreview().run()
            else:
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGame().run()
        #-----------------------------------------------------------------------

        #Idioma-----------------------------------------------------------------
        if idiomaApp == "Es":
            texto_extras = "Extras"
            texto_drake = "Ecuación de Drake"
            texto_volver = "Volver"

        if idiomaApp  == "En":
            texto_extras = "Extras"
            texto_drake = "Drake's Equation"
            texto_volver = "Back"

        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal') #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        consola = Label(text = texto_extras)

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        drake = Button(text = texto_drake,background_color = (0.1,0.2,0.6,0.6))
        drake.bind(on_press=callback)

        volver = Button(text = texto_volver,background_color = (0.1,0.2,0.6,0.6))
        volver.bind(on_press=callback)

        null = Label(text = "")
        null2 = Label(text = "")

        #Añadir elementos al pie------------------------------------------------
        pie.add_widget(null)
        pie.add_widget(drake)
        pie.add_widget(null2)
        pie.add_widget(volver)

        #Añadir cada división al layout global----------------------------------
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

        #Mostrar layout completo------------------------------------------------
        return superBox
        #Fin Interfaz-----------------------------------------------------------

class MathGameIntermission(App):

    def build(self):

        global modo_ajustes
        global operacion

        #Función que detecta el texto del botón seleccionado en pantalla--------
        def callback(instance):

            print(instance.text)

            if modo_ajustes == 1:
                if operacion == "Sumas":
                    superBox.remove_widget(cabecera)
                    superBox.remove_widget(pie)
                    MathGameOperaciones().run()
                else:
                    if operacion == "Restas":
                        superBox.remove_widget(cabecera)
                        superBox.remove_widget(pie)
                        MathGameOperaciones().run()
                    else:
                        if operacion == "Multiplicaciones":
                            superBox.remove_widget(cabecera)
                            superBox.remove_widget(pie)
                            MathGameOperaciones().run()
                        else:
                            superBox.remove_widget(cabecera)
                            superBox.remove_widget(pie)
                            MathGameOperaciones().run()
            else:
                superBox.remove_widget(cabecera)
                superBox.remove_widget(pie)
                MathGameD().run()
        #-----------------------------------------------------------------------

        #Idioma-----------------------------------------------------------------
        if idiomaApp == "Es":
            texto_realizar = "Vas a realizar: "
            texto_parametros = "Vamos a seleccionar los parámetros deseados"
            texto_aceptar = "Vale"

        if idiomaApp  == "En":
            texto_realizar = "You are going to do: "
            texto_parametros = "Let's select the desired parameters"
            texto_aceptar = "Okay"

        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal') #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        if modo_ajustes == 1:
            consola = Label(text = texto_realizar+operacion)
        else:
            consola = Label(text = texto_parametros)

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        vale = Button(text = texto_aceptar,background_color = (0.1,0.2,0.6,0.6))
        vale.bind(on_press=callback)

        null = Label(text = "")
        null2 = Label(text = "")

        #Añadir elementos al pie------------------------------------------------
        pie.add_widget(null)
        pie.add_widget(null2)
        pie.add_widget(vale)

        #Añadir cada división al layout global----------------------------------
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

        #Mostrar layout completo------------------------------------------------
        return superBox
        #Fin Interfaz-----------------------------------------------------------

class MathGameAjustes(App):

    global firstRun
    global mostrar_modo_ajustes
    global mostrar_modo_dificultad
    global mostrar_modo_numPreguntas
    global mostrar_modo_problemas
    global volver_bloquear
    global bloquear
    global texto_seleccionar

    #Idioma---------------------------------------------------------------------
    texto_seleccionar = "(Seleccionar)"

    try:
        if idiomaApp == "Es":
            texto_seleccionar = "(Seleccionar)"

        if idiomaApp  == "En":
            texto_seleccionar = "(Choose)"
    except:
        print()
    #---------------------------------------------------------------------------

    if firstRun == 1:
        #El modo ajustes se inicia en la clase principal (cambiar allí)---------
        mostrar_modo_ajustes = "(No)"
        #-----------------------------------------------------------------------
        mostrar_modo_dificultad = texto_seleccionar
        mostrar_modo_numPreguntas = texto_seleccionar
        mostrar_modo_problemas = texto_seleccionar
        volver_bloquear = 0
        bloquear = 1
    else:
        mostrar_modo_ajustes = "(Si)"
        volver_bloquear = 1
        bloquear = 0

    def build(self):

        def limpiarGUI():
            superBox.remove_widget(espacio2)
            superBox.remove_widget(header)
            superBox.remove_widget(espacio3)
            superBox.remove_widget(dificultad)
            superBox.remove_widget(preguntas)
            superBox.remove_widget(problemas)
            superBox.remove_widget(mantener)
            superBox.remove_widget(espacio0)
            superBox.remove_widget(idioma)
            superBox.remove_widget(espacio1)
            superBox.remove_widget(volver)

        #Función que detecta el texto del botón seleccionado en pantalla--------
        def callback(instance):

            global modo_ajustes
            global mostrar_modo_ajustes
            global volver_bloquear
            global bloquear
            global RangoMin
            global RangoMax
            global modo_supervivencia
            global vida
            global numPreguntas
            global respuestaOperaciones
            global texto_seleccionar

            Seleccion = instance.text #contiene el string del boton
            print(instance.text)

            if Seleccion == texto_dificultad+mostrar_modo_dificultad:
                if modo_ajustes == 1:
                    limpiarGUI()
                    MathGameD().run()
                #Else omitido para que termine la comprobación manteniendo la pantalla
            else:
                if Seleccion == texto_preguntas+mostrar_modo_numPreguntas:
                    if modo_ajustes == 1:
                        limpiarGUI()
                        MathGameS().run()
                    #Else omitido para que termine la comprobación manteniendo la pantalla
                else:
                    if Seleccion == texto_problemas+mostrar_modo_problemas:
                        if modo_ajustes == 1:
                            limpiarGUI()
                            MathGameSelOpe().run()
                        #Else omitido para que termine la comprobación manteniendo la pantalla
                    else:
                        if Seleccion == texto_idioma:
                            limpiarGUI()
                            MathGameSelIdioma().run()
                        else:

                            if Seleccion == texto_volver:
                                if modo_ajustes == 1:
                                    if mostrar_modo_dificultad == texto_seleccionar:
                                        #Comprobación para mantener la pantalla dada la condición
                                        print()
                                    else:
                                        if mostrar_modo_numPreguntas == texto_seleccionar:
                                            #Comprobación para mantener la pantalla dada la condición
                                            print()
                                        else:
                                            if mostrar_modo_problemas == texto_seleccionar:
                                                #Comprobación para mantener la pantalla dada la condición
                                                print()
                                            else:

                                                #Si se puede almacenar el estado
                                                if modo_ajustes == 1:
                                                    #Guardar config con guardado activo-----
                                                    ajustesFile = open("./ajustes.txt", "w")

                                                    RangoMinStr = str(RangoMin)
                                                    ajustesFile.write(RangoMinStr)

                                                    RangoMaxStr = str(RangoMax)
                                                    ajustesFile.write(RangoMaxStr)

                                                    modo_supervivenciaStr = str(modo_supervivencia)
                                                    ajustesFile.write(modo_supervivenciaStr)

                                                    vidaStr = str(vida)
                                                    ajustesFile.write(vidaStr)

                                                    numPreguntasStr = str(numPreguntas)
                                                    ajustesFile.write(numPreguntasStr)

                                                    ajustesFile.close()
                                                    #-------------------------------
                                                    #Guardar config con guardado activo-----
                                                    ajustesDif = open("./ajustes2.txt", "w")
                                                    ajustesDif.write(respuestaOperaciones)
                                                    ajustesDif.close()
                                                    #-------------------------------

                                                limpiarGUI()
                                                MathGame().run()
                                else:
                                    limpiarGUI()
                                    MathGame().run()
                            else:
                                if modo_ajustes == 1:
                                    modo_ajustes = 0
                                    mostrar_modo_ajustes = texto_no
                                    volver_bloquear = 0
                                    bloquear = 1

                                    #Borrar el archivo de config----------------
                                    ajustesFile = open("./ajustes.txt", "w")
                                    ajustesFile.write("0")
                                    ajustesFile.close()
                                    #-------------------------------------------
                                    #Borrar config con guardado activo----------
                                    ajustesDif = open("./ajustes2.txt", "w")
                                    ajustesDif.write("0")
                                    ajustesDif.close()
                                    #-------------------------------------------
                                else:
                                    modo_ajustes = 1
                                    mostrar_modo_ajustes = texto_si
                                    bloquear = 0

                                    if mostrar_modo_dificultad == texto_seleccionar or mostrar_modo_numPreguntas == texto_seleccionar or mostrar_modo_problemas == texto_seleccionar:
                                        volver_bloquear = 1
                                    else:
                                        #Guardar configuración al activar el guardado
                                        ajustesFile = open("./ajustes.txt", "w")

                                        RangoMinStr = str(RangoMin)
                                        ajustesFile.write(RangoMinStr)

                                        RangoMaxStr = str(RangoMax)
                                        ajustesFile.write(RangoMaxStr)

                                        modo_supervivenciaStr = str(modo_supervivencia)
                                        ajustesFile.write(modo_supervivenciaStr)

                                        vidaStr = str(vida)
                                        ajustesFile.write(vidaStr)

                                        numPreguntasStr = str(numPreguntas)
                                        ajustesFile.write(numPreguntasStr)

                                        ajustesFile.close()
                                        #---------------------------------------
                                        #Guardar config con guardado activo-----
                                        ajustesDif = open("./ajustes2.txt", "w")
                                        ajustesDif.write(respuestaOperaciones)
                                        ajustesDif.close()
                                        #---------------------------------------

                                limpiarGUI()
                                MathGameAjustes().run()
        #-----------------------------------------------------------------------

        #Idioma-----------------------------------------------------------------
        if idiomaApp == "Es":
            texto_ajustes = "Ajustes - v"
            texto_dificultad = "Dificultad: "
            texto_preguntas = "Nº preguntas: "
            texto_problemas = "Problemas: "
            texto_idioma = "Idioma"
            texto_mantener = "Mantener ajustes: "
            texto_volver = "Volver"
            texto_si = "(Sí)"
            texto_no = "(No)"

        if idiomaApp  == "En":
            texto_ajustes = "Settings - v"
            texto_dificultad = "Difficulty: "
            texto_preguntas = "Nº of Problems: "
            texto_problemas = "Problems: "
            texto_idioma = "Language"
            texto_mantener = "Keep Settings: "
            texto_volver = "Back"
            texto_si = "(Yes)"
            texto_no = "(No)"

        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Crear elementos de cabecera--------------------------------------------
        header = Label(text = texto_ajustes+version)

        #Crear elementos del pie------------------------------------------------
        if bloquear == 0:
            dificultad = Button(text = texto_dificultad+mostrar_modo_dificultad,background_color = (0.1,0.2,0.6,0.6))
            dificultad.bind(on_press=callback)

            preguntas = Button(text = texto_preguntas+mostrar_modo_numPreguntas,background_color = (0.1,0.2,0.6,0.6))
            preguntas.bind(on_press=callback)

            problemas = Button(text = texto_problemas+mostrar_modo_problemas,background_color = (0.1,0.2,0.6,0.6))
            problemas.bind(on_press=callback)

        else:
            dificultad = Button(text = texto_dificultad+mostrar_modo_dificultad,background_color = (0.1,0.2,0.6,0.3))
            dificultad.bind(on_press=callback)

            preguntas = Button(text = texto_preguntas+mostrar_modo_numPreguntas,background_color = (0.1,0.2,0.6,0.3))
            preguntas.bind(on_press=callback)

            problemas = Button(text = texto_problemas+mostrar_modo_problemas,background_color = (0.1,0.2,0.6,0.3))
            problemas.bind(on_press=callback)


        idioma = Button(text = texto_idioma,background_color = (0.1,0.2,0.6,0.6))
        idioma.bind(on_press=callback)

        mantener = Button(text = texto_mantener+mostrar_modo_ajustes,background_color = (0.1,0.2,0.6,0.6))
        mantener.bind(on_press=callback)

        espacio0 = Label()
        espacio1 = Label()
        espacio2 = Label()
        espacio3 = Label()

        if volver_bloquear == 0:
            volver = Button(text = texto_volver,background_color = (0.1,0.2,0.6,0.6))
            volver.bind(on_press=callback)
        else:
            if mostrar_modo_dificultad != texto_seleccionar and mostrar_modo_numPreguntas != texto_seleccionar and mostrar_modo_problemas != texto_seleccionar:
                volver = Button(text = texto_volver,background_color = (0.1,0.2,0.6,0.6))
                volver.bind(on_press=callback)
            else:
                volver = Button(text = texto_volver,background_color = (0.1,0.2,0.6,0.3))
                volver.bind(on_press=callback)

        #Añadir elementos al pie------------------------------------------------
        superBox.add_widget(espacio2)
        superBox.add_widget(header)
        superBox.add_widget(espacio3)
        superBox.add_widget(dificultad)
        superBox.add_widget(preguntas)
        superBox.add_widget(problemas)
        superBox.add_widget(mantener)
        superBox.add_widget(espacio0)
        superBox.add_widget(idioma)
        superBox.add_widget(espacio1)
        superBox.add_widget(volver)

        #Mostrar layout completo------------------------------------------------
        return superBox
        #Fin Interfaz-----------------------------------------------------------

class MathGamePuntuacion(App):

    def build(self):

        #Función que detecta el texto del botón seleccionado en pantalla--------
        def callback(instance):

            superBox.remove_widget(pie)
            superBox.remove_widget(cabecera)
            MathGame().run()
        #-----------------------------------------------------------------------

        archivo = open("./points.txt", "r") #Abrir archivo----------------------

        #Idioma-----------------------------------------------------------------
        if idiomaApp == "Es":
            texto_puntuacion = "Puntuación: "
            texto_aceptar = "Vale"

        if idiomaApp  == "En":
            texto_puntuacion = "Score: "
            texto_aceptar = "Okay"
        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal') #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        consola = Label(text = texto_puntuacion+archivo.read())

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        aceptar = Button(text = texto_aceptar,background_color = (0.1,0.2,0.6,0.6))
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
                MathGameOperaciones().run()
            else:
                if operacion == "Restas":
                    superBox.remove_widget(cabecera)
                    superBox.remove_widget(pie)
                    MathGameOperaciones().run()
                else:
                    if operacion == "Multiplicaciones":
                        superBox.remove_widget(cabecera)
                        superBox.remove_widget(pie)
                        MathGameOperaciones().run()
                    else:
                        superBox.remove_widget(cabecera)
                        superBox.remove_widget(pie)
                        MathGameOperaciones().run()
        #-----------------------------------------------------------------------

        global operacion

        #Idioma-----------------------------------------------------------------
        if idiomaApp == "Es":
            texto_resultado = "El resultado era "
            texto_acierto = "¡Has acertado!"
            texto_aceptar = "Vale"

        if idiomaApp  == "En":
            texto_resultado = "The correct answer was "
            texto_acierto = "You nailed it!"
            texto_aceptar = "Okay"
        #-----------------------------------------------------------------------

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
            consola = Label(text = texto_resultado+resultadoMostrar)

        else:

            #victory.play()
            consola = Label(text = texto_acierto)

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical
        pie = BoxLayout(orientation ='vertical')

        aceptar = Button(text = texto_aceptar,background_color = (0.1,0.2,0.6,0.6))
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

            if respuestaSeleccionada == texto_si:

                ContadorPreguntas = int(ContadorPreguntas)
                puntuacion = int(puntuacion)

                ContadorPreguntas = 0
                puntuacion = 0

                if modo_supervivencia == 1: vida = 5

                if operacion == "Sumas":

                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)
                    MathGameOperaciones().run()

                else:

                    if operacion == "Restas":

                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)
                        MathGameOperaciones().run()

                    else:

                        if operacion == "Multiplicaciones":

                            superBox.remove_widget(pie)
                            superBox.remove_widget(cabecera)
                            MathGameOperaciones().run()

                        else:

                            superBox.remove_widget(pie)
                            superBox.remove_widget(cabecera)
                            MathGameOperaciones().run()

            else:

                if modo_supervivencia == 1: vida = 5

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

        #Idioma-----------------------------------------------------------------
        if idiomaApp == "Es":
            texto_aciertos = "Has acertado "
            texto_total = " de un total de "
            texto_pregunta = "¿Quieres seguir realizando operaciones?"
            texto_si = "Si"
            texto_no = "No"

        if idiomaApp  == "En":
            texto_aciertos = "You have guessed "
            texto_total = " of a total of "
            texto_pregunta = "¿Do you want to repeat?"
            texto_si = "Yes"
            texto_no = "No"
        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal')

        consola = Label(text = texto_aciertos+puntuacion+texto_total+ContadorPreguntas)

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        bienvenida = Label(text = texto_pregunta)

        aceptar = Button(text = texto_si,background_color = (0.1,0.2,0.6,0.6))
        aceptar.bind(on_press=callback)

        rechazar = Button(text = texto_no,background_color = (0.1,0.2,0.6,0.6))
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

class MathGameOperaciones(App):

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
        global finalOperacion
        finalOperacion = 0
        global operacion

        #Función que registra el botón seleccionado-----------------------------
        def callback(instance):

            global puntuacion
            global ContadorPreguntas
            global comprobacion

            Seleccion = instance.text #contiene el string del boton
            print(instance.text)

            if Seleccion == texto_salir:
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameResultado().run()

            #Gestión de la excepción al presionar botón sin introducir nada-----
            try:
                respuestaOperaciones = resultadoAintroducir #contiene el string del boton
            except:
                respuestaOperaciones = 998003
            #-------------------------------------------------------------------

            if finalOperacion == 0:

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
            else:

                #Comprobación turnos o vidas------------------------------------
                if modo_supervivencia == 0:
                    if ContadorPreguntas == numPreguntas:
                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)
                        MathGameResultado().run()
                else:
                    if vida == 0:
                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)
                        MathGameResultado().run()
            #-------------------------------------------------------------------

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

            randomnumero1=(randrange(RangoMin,RangoMax))          #Rango de suma
            randomnumero2=(randrange(RangoMin,RangoMax))          #Rango de suma
            mostrarnumero1 = str(randomnumero1)
            mostrarnumero2 = str(randomnumero2)

            if operacion == "Sumas": resultadoreal = randomnumero1+randomnumero2           #Resultadoreal
            if operacion == "Restas": resultadoreal = randomnumero1-randomnumero2           #Resultadoreal
            if operacion == "Multiplicaciones": resultadoreal = randomnumero1*randomnumero2           #Resultadoreal
            if operacion == "Divisiones": resultadoreal = randomnumero1/randomnumero2           #Resultadoreal

            resultadoreal = int(resultadoreal)              #Convertir a Integer

            #Debugging----------------------------------------------------------
            print(resultadoreal)
            #-------------------------------------------------------------------

            #Idioma-------------------------------------------------------------
            if idiomaApp == "Es":
                texto_tienes = "Tienes "
                texto_vidas = " vidas"
                texto_sumas = "Sumas entre dos números: "
                texto_restas = "Restas entre dos números: "
                texto_multiplicaciones = "Multiplicaciones entre dos números: "
                texto_divisiones = "Divisiones entre dos números: "
                texto_respuesta = "Seleccione la respuesta"
                texto_salir = "Salir"

            if idiomaApp  == "En":
                texto_tienes = "You have "
                texto_vidas = " lifes"
                texto_sumas = "Sums between two numbers: "
                texto_restas = "Subtractions between two numbers: "
                texto_multiplicaciones = "Multiplications between two numbers: "
                texto_divisiones = "Divisions between two numbers: "
                texto_respuesta = "Choose the answer"
                texto_salir = "Exit"
            #-------------------------------------------------------------------

            #Interfaz-----------------------------------------------------------
            #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
            superBox = BoxLayout(orientation ='vertical')

            #Widgets de cabecera añadidos en el plano horizontal----------------
            cabecera = BoxLayout(orientation ='horizontal')

            if modo_supervivencia == 1:

                vidaStr = str(vida)
                if operacion == "Sumas":
                    consola = Label(text = texto_tienes+vidaStr+texto_vidas+" | "+texto_sumas+mostrarnumero1+" + "+mostrarnumero2)
                else:
                    if operacion == "Restas":
                        consola = Label(text = texto_tienes+vidaStr+texto_vidas+" | "+texto_restas+mostrarnumero1+" - "+mostrarnumero2)
                    else:
                        if operacion == "Multiplicaciones":
                            consola = Label(text = texto_tienes+vidaStr+texto_vidas+" | "+texto_multiplicaciones+mostrarnumero1+" x "+mostrarnumero2)
                        else:
                            consola = Label(text = texto_tienes+vidaStr+texto_vidas+" | "+texto_divisiones+mostrarnumero1+" / "+mostrarnumero2)

            else:

                if operacion == "Sumas":
                    consola = Label(text = texto_sumas+mostrarnumero1+" + "+mostrarnumero2)
                else:
                    if operacion == "Restas":
                        consola = Label(text = texto_restas+mostrarnumero1+" - "+mostrarnumero2)
                    else:
                        if operacion == "Multiplicaciones":
                            consola = Label(text = texto_multiplicaciones+mostrarnumero1+" x "+mostrarnumero2)
                        else:
                            consola = Label(text = texto_divisiones+mostrarnumero1+" / "+mostrarnumero2)

            cabecera.add_widget(consola)

            #Widgets de pie de página añadidos en el plano vertical-------------
            pie = BoxLayout(orientation ='vertical')

            bienvenida = Button(text = texto_respuesta,background_color = (0.1,0.2,0.6,0.6))
            bienvenida.bind(on_press=callback)

            salidaOperaciones = Button(text = texto_salir,background_color = (0.1,0.2,0.6,0.6))
            salidaOperaciones.bind(on_press=callback)

            textinput = TextInput()
            textinput.bind(text=on_text)

            null = Label(text = "")

            pie.add_widget(null)
            pie.add_widget(textinput)
            pie.add_widget(bienvenida)
            pie.add_widget(salidaOperaciones)

            #Salida por pantalla final------------------------------------------
            superBox.add_widget(cabecera)
            superBox.add_widget(pie)

            #Mostrar layout completo--------------------------------------------
            return superBox
            #Fin interfaz-------------------------------------------------------

        finalOperacion = 1

        #Idioma-----------------------------------------------------------------
        if idiomaApp == "Es":
            texto_sinvidas = "Te has quedado sin vidas"
            texto_finalizar = "Has finalizado"
            texto_aceptar = "Vale"

        if idiomaApp  == "En":
            texto_sinvidas = "You have lost all lifes"
            texto_finalizar = "You have finished"
            texto_aceptar = "Okay"
        #-----------------------------------------------------------------------

        #InterfazFinal----------------------------------------------------------
        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal')

        if modo_supervivencia == 1:

            vidaStr = str(vida)
            consola = Label(text = texto_sinvidas)

        else:

            consola = Label(text = texto_finalizar)

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        vale = Button(text = texto_aceptar,background_color = (0.1,0.2,0.6,0.6))
        vale.bind(on_press=callback)

        null = Label(text = "")
        null2 = Label(text = "")

        pie.add_widget(null)
        pie.add_widget(null2)
        pie.add_widget(vale)

        #Salida por pantalla final----------------------------------------------
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

        #Mostrar layout completo------------------------------------------------
        return superBox
        #Fin interfaz-----------------------------------------------------------

class MathGameSelOpe(App):

    def build(self):

        #Función que registra el botón seleccionado-----------------------------
        def callback(instance):

            global operacion
            global modo_ajustes
            global mostrar_modo_problemas
            global respuestaOperaciones

            respuestaOperaciones = instance.text #contiene el string del boton
            print(instance.text)

            if respuestaOperaciones == texto_sumas:
                operacion = "Sumas"
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)

                if modo_ajustes == 1:
                    mostrar_modo_problemas = "(Sumas)"
                    MathGameAjustes().run()
                else:
                    mostrar_modo_problemas = "(Seleccionar)"
                    MathGameOperaciones().run()
            else:
                if respuestaOperaciones == texto_restas:
                    operacion = "Restas"
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)

                    if modo_ajustes == 1:
                        mostrar_modo_problemas = "(Restas)"
                        MathGameAjustes().run()
                    else:
                        mostrar_modo_problemas = "(Seleccionar)"
                        MathGameOperaciones().run()
                else:
                    if respuestaOperaciones == texto_multiplicaciones:
                        operacion = "Multiplicaciones"
                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)

                        if modo_ajustes == 1:
                            mostrar_modo_problemas = "(Multiplicaciones)"
                            MathGameAjustes().run()
                        else:
                            mostrar_modo_problemas = "(Seleccionar)"
                            MathGameOperaciones().run()
                    else:
                        operacion = "Divisiones"
                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)

                        if modo_ajustes == 1:
                            mostrar_modo_problemas = "(Divisiones)"
                            MathGameAjustes().run()
                        else:
                            mostrar_modo_problemas = "(Seleccionar)"
                            MathGameOperaciones().run()

        #Idioma-----------------------------------------------------------------
        if idiomaApp == "Es":
            intro = "Empecemos con la configuración"
            texto_preguntas = "Seleccione tipo de problemas"
            texto_sumas = "Sumas"
            texto_restas = "Restas"
            texto_multiplicaciones = "Multiplicaciones"
            texto_divisiones = "Divisiones"

        if idiomaApp  == "En":
            intro = "Let's start"
            texto_preguntas = "Choose problems"
            texto_sumas = "Sums"
            texto_restas = "Subtractions"
            texto_multiplicaciones = "Multiplications"
            texto_divisiones = "Divisions"
        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal
        cabecera = BoxLayout(orientation ='horizontal')

        consola = Label(text = intro)

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical
        pie = BoxLayout(orientation ='vertical')

        bienvenida = Label(text = texto_preguntas)

        sumas = Button(text = texto_sumas,background_color = (0.1,0.2,0.6,0.6))
        sumas.bind(on_press=callback)

        restas = Button(text = texto_restas,background_color = (0.1,0.2,0.6,0.6))
        restas.bind(on_press=callback)

        multiplicaciones = Button(text = texto_multiplicaciones,background_color = (0.1,0.2,0.6,0.6))
        multiplicaciones.bind(on_press=callback)

        divisiones = Button(text = texto_divisiones,background_color = (0.1,0.2,0.6,0.6))
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
        #-----------------------------------------------------------------------

class MathGameP(App):

    def build(self):

        #Funcion que registra el botón seleccionado-----------------------------
        def callback(instance):

            global numPreguntas
            global modo_ajustes
            global mostrar_modo_numPreguntas

            respuestaPreguntas = instance.text #contiene el string del boton
            print(instance.text)
            if respuestaPreguntas == "1":
                numPreguntas = 1
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)

                if modo_ajustes == 1:
                    mostrar_modo_numPreguntas = "(1)"
                    MathGameAjustes().run()
                else:
                    mostrar_modo_numPreguntas = "(Seleccionar)"
                    MathGameSelOpe().run()
            else:
                if respuestaPreguntas == "2":
                    numPreguntas = 2
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)

                    if modo_ajustes == 1:
                        mostrar_modo_numPreguntas = "(2)"
                        MathGameAjustes().run()
                    else:
                        mostrar_modo_numPreguntas = "(Seleccionar)"
                        MathGameSelOpe().run()
                else:
                    if respuestaPreguntas == "3":
                        numPreguntas = 3
                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)

                        if modo_ajustes == 1:
                            mostrar_modo_numPreguntas = "(3)"
                            MathGameAjustes().run()
                        else:
                            mostrar_modo_numPreguntas = "(Seleccionar)"
                            MathGameSelOpe().run()
                    else:
                        if respuestaPreguntas == "4":
                            numPreguntas = 4
                            superBox.remove_widget(pie)
                            superBox.remove_widget(cabecera)

                            if modo_ajustes == 1:
                                mostrar_modo_numPreguntas = "(4)"
                                MathGameAjustes().run()
                            else:
                                mostrar_modo_numPreguntas = "(Seleccionar)"
                                MathGameSelOpe().run()
                        else:
                            numPreguntas = 5
                            superBox.remove_widget(pie)
                            superBox.remove_widget(cabecera)

                            if modo_ajustes == 1:
                                mostrar_modo_numPreguntas = "(5)"
                                MathGameAjustes().run()
                            else:
                                mostrar_modo_numPreguntas = "(Seleccionar)"
                                MathGameSelOpe().run()

        #Idioma-----------------------------------------------------------------
        if idiomaApp == "Es":
            intro = "Empecemos con la configuración"
            texto_preguntas = "Cuántas preguntas quieres (del 1 al 5)"

        if idiomaApp  == "En":
            intro = "Let's start"
            texto_preguntas = "How many problems do you want (from 1 to 5)"
        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal')

        #Elementos de cabecera--------------------------------------------------
        consola = Label(text = intro)

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Elementos del pie------------------------------------------------------
        bienvenida = Label(text = texto_preguntas)

        uno = Button(text = "1",background_color = (0.1,0.2,0.6,0.6))
        uno.bind(on_press=callback)

        dos = Button(text = "2",background_color = (0.1,0.2,0.6,0.6))
        dos.bind(on_press=callback)

        tres = Button(text = "3",background_color = (0.1,0.2,0.6,0.6))
        tres.bind(on_press=callback)

        cuatro = Button(text = "4",background_color = (0.1,0.2,0.6,0.6))
        cuatro.bind(on_press=callback)

        cinco = Button(text = "5",background_color = (0.1,0.2,0.6,0.6))
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
            global modo_ajustes
            global mostrar_modo_numPreguntas

            respuestaSupervivencia = instance.text #contiene el string del boton
            print(instance.text)
            if respuestaSupervivencia == texto_si:

                modo_supervivencia = 1
                vida = 5

                vidascii = "♥"
                numPreguntas = 0

                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)

                if modo_ajustes == 1:
                    mostrar_modo_numPreguntas = "(Supervivencia)"
                    MathGameAjustes().run()
                else:
                    mostrar_modo_numPreguntas = "(Seleccionar)"
                    MathGameSelOpe().run()

            else:

                modo_supervivencia = 0
                vida = 0
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameP().run()

        #Idioma-----------------------------------------------------------------
        if idiomaApp == "Es":
            intro = "Empecemos con la configuración"
            texto_modo = "¿Quieres activar el modo supervivencia?"
            texto_si = "Si"
            texto_no = "No"

        if idiomaApp  == "En":
            intro = "Let's start"
            texto_modo = "Do you want to enable survival mode?"
            texto_si = "Yes"
            texto_no = "No"
        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout global----------------------------------------------------------
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal')

        consola = Label(text = intro)

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Creación de elementos--------------------------------------------------
        bienvenida = Label(text = texto_modo)

        aceptar = Button(text = texto_si,background_color = (0.1,0.2,0.6,0.6))
        aceptar.bind(on_press=callback)

        rechazar = Button(text = texto_no,background_color = (0.1,0.2,0.6,0.6))
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
            global modo_ajustes
            global mostrar_modo_dificultad

            dificultadSeleccionada = instance.text #contiene el string del boton
            print(instance.text)
            if dificultadSeleccionada == texto_facil:
                dificultad = "F"
                RangoMin = 0
                RangoMax = 9
                MultiPuntuacion = 1
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)

                if modo_ajustes == 1:
                    mostrar_modo_dificultad = "(Fácil)"
                    MathGameAjustes().run()
                else:
                    mostrar_modo_dificultad = "(Seleccionar)"
                    MathGameS().run()
            else:
                if dificultadSeleccionada == texto_normal:
                    dificultad = "N"
                    RangoMin = 10
                    RangoMax = 99
                    MultiPuntuacion = 2
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)

                    if modo_ajustes == 1:
                        mostrar_modo_dificultad = "(Normal)"
                        MathGameAjustes().run()
                    else:
                        mostrar_modo_dificultad = "(Seleccionar)"
                        MathGameS().run()
                else:
                    dificultad = "D"
                    RangoMin = 100
                    RangoMax = 999
                    MultiPuntuacion = 3
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)

                    if modo_ajustes == 1:
                        mostrar_modo_dificultad = "(Dificil)"
                        MathGameAjustes().run()
                    else:
                        mostrar_modo_dificultad = "(Seleccionar)"
                        MathGameS().run()
        #-----------------------------------------------------------------------

        #Idioma-----------------------------------------------------------------
        if idiomaApp == "Es":
            intro = "Empecemos con la configuración"
            texto_dificultad = "Seleccione dificultad"
            texto_facil = "Fácil"
            texto_normal = "Normal"
            texto_dificil = "Dificil"

        if idiomaApp  == "En":
            intro = "Let's start"
            texto_dificultad = "Choose difficulty"
            texto_facil = "Easy"
            texto_normal = "Normal"
            texto_dificil = "Hard"
        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal') #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        consola = Label(text = intro)

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        bienvenida = Label(text = texto_dificultad)

        dificultadFacil = Button(text = texto_facil,background_color = (0.1,0.2,0.6,0.6))
        dificultadFacil.bind(on_press=callback)

        dificultadNormal = Button(text = texto_normal,background_color = (0.1,0.2,0.6,0.6))
        dificultadNormal.bind(on_press=callback)

        dificultadDificil = Button(text = texto_dificil,background_color = (0.1,0.2,0.6,0.6))
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

    global firstRun
    global idiomaFirstRun

    if firstRun == 1:
        global modo_ajustes
        modo_ajustes = 0 #(boolean (Descomentar al quitar archivos))------------

    def build(self):

        try:
            if idiomaFirstRun == 1:
                MathGameSelIdioma().run()
        except:
            #Se confirma que no es el primer run--------------------------------
            print()

        #Función que detecta el texto del botón seleccionado en pantalla--------
        def callback(instance):

            Seleccion = instance.text #contiene el string del boton
            print(instance.text)
            if Seleccion == Jugar:
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameIntermission().run()
            else:
                if Seleccion == Puntuación:
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)
                    MathGamePuntuacion().run()
                else:
                    if Seleccion == Ajustes:
                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)
                        MathGameAjustes().run()
                    else:
                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)
                        MathGameExtras().run()
        #-----------------------------------------------------------------------

        #Idioma-----------------------------------------------------------------
        if idiomaApp == "Es":
            Jugar = "Jugar"
            Puntuación = "Puntuación"
            Ajustes = "Ajustes"
            Extras = "Extras"

        if idiomaApp  == "En":
            Jugar = "Play"
            Puntuación = "Score"
            Ajustes = "Settings"
            Extras = "Extras"
        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal') #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        consola = Image(source="./data/cabecera.png")

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        jugar = Button(text = Jugar,background_color = (0.1,0.2,0.6,0.6))
        jugar.bind(on_press=callback)

        puntuacion = Button(text = Puntuación,background_color = (0.1,0.2,0.6,0.6))
        puntuacion.bind(on_press=callback)

        ajustes = Button(text = Ajustes,background_color = (0.1,0.2,0.6,0.6))
        ajustes.bind(on_press=callback)

        extras = Button(text = Extras,background_color = (0.1,0.2,0.6,0.6))
        extras.bind(on_press=callback)

        null = Label()

        #Añadir elementos al pie------------------------------------------------
        pie.add_widget(jugar)
        pie.add_widget(extras)
        pie.add_widget(puntuacion)
        pie.add_widget(null)
        pie.add_widget(ajustes)

        #Añadir cada división al layout global----------------------------------
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

        #Mostrar layout completo------------------------------------------------
        return superBox
        #Fin Interfaz-----------------------------------------------------------

#Constructor--------------------------------------------------------------------
if __name__ == '__main__':
    MathGame().run()
