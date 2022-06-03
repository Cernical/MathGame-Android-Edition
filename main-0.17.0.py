#!/usr/bin/python3
version = "0.17.0"

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

#Traductor de texto-------------------------------------------------------------
def funTraductor(palabra):

    global idiomaApp

    #Variables idioma
    global tJugar
    global tExtras
    global tPuntuacion
    global tAjustes
    global tVamos
    global tAceptar
    global tEmpecemos
    global tSeleccione
    global tFacil
    global tNormal
    global tDificil
    global tQuieresSupervivencia
    global tSi
    global tNo
    global tCuantas
    global tProblemas
    global tSumas
    global tRestas
    global tMultiplicaciones
    global tDivisiones
    global tEntreOperandos
    global tRespuesta
    global tSalir
    global tFinalizado
    global tVidas1
    global tVidas2
    global tResultado
    global tAcertar1
    global tAcertar2
    global tSeguir
    global tPuntuacionL
    global tDificultad
    global tPreguntas
    global tProblemasB
    global tMantener
    global tIdioma
    global tVolver
    global tExtrasL
    global tDrake
    global tSeleccionar
    global tSiAjustes
    global tNoAjustes
    global tVersion
    global tSupervivencia
    global tVas
    global tSinvidas
    global tSumasentre
    global tRestasentre
    global tMultientre
    global tDivisionentre
    global tHasacertado

    if idiomaApp == "Es":
        if palabra == "MathGame":
            #Clase MathGame-----------------------------------------------------
            tJugar = "Jugar"
            tExtras = "Extras"
            tPuntuacion = "Puntuación"
            tAjustes = "Ajustes"
            #-------------------------------------------------------------------
        if palabra == "MathGameIntermission":
            #Clase MathGameIntermission-----------------------------------------
            tVas = "Vas a realizar: "
            tVamos = "Vamos a seleccionar los parámetros deseados"
            tAceptar = "Vale"
            #-------------------------------------------------------------------
        if palabra == "MathGameD":
            #Clase MathGameD----------------------------------------------------
            tEmpecemos = "Empecemos con la configuración"
            tSeleccione = "Seleccione dificultad"
            tFacil = "Fácil"
            tNormal = "Normal"
            tDificil = "Dificil"
            tSeleccionar = "(Seleccionar)"
            #-------------------------------------------------------------------
        if palabra == "MathGameS":
            #Clase MathGameS----------------------------------------------------
            tEmpecemos = "Empecemos con la configuración"
            tQuieresSupervivencia = "¿Quieres activar el modo supervivencia?"
            tSi = "Si"
            tNo = "No"
            tSupervivencia = "(Supervivencia)"
            tSeleccionar = "(Seleccionar)"
            #-------------------------------------------------------------------
        if palabra == "MathGameP":
            #Clase MathGameP----------------------------------------------------
            tEmpecemos = "Empecemos con la configuración"
            tCuantas = "Cuántas preguntas quieres (del 1 al 5)"
            tSeleccionar = "(Seleccionar)"
            #-------------------------------------------------------------------
        if palabra == "MathGameSelOpe":
            #Clase MathGameSelOpe-----------------------------------------------
            tEmpecemos = "Empecemos con la configuración"
            tProblemas = "Seleccione tipo de problemas"
            tSumas = "Sumas"
            tRestas = "Restas"
            tMultiplicaciones = "Multiplicaciones"
            tDivisiones = "Divisiones"
            tSeleccionar = "(Seleccionar)"
            #-------------------------------------------------------------------
        if palabra == "MathGameOperaciones":
            #Clase MathGameOperaciones------------------------------------------
            tEntreOperandos = "entre dos números: "
            tRespuesta = "Seleccione la respuesta"
            tSalir = "Salir"
            tFinalizado = "Has finalizado"
            tAceptar = "Vale"
            tSumasentre = " Sumas entre dos números: "
            tRestasentre = " Restas entre dos números: "
            tMultientre = " Multiplicaciones entre dos números: "
            tDivisionentre = " Divisiones entre dos números: "
            #Supervivencia------------------------------------------------------
            tVidas1 = "Tienes "
            tVidas2 = " vidas "
            tSinvidas = "Te has quedado sin vidas"
            #-------------------------------------------------------------------
        if palabra == "MathGameComprobacion":
            #Clase MathGameComprobacion-----------------------------------------
            tResultado = "El resultado era "
            tAceptar = "Vale"
            tHasacertado = "¡Has acertado!"
            #-------------------------------------------------------------------
            tAcertar1 = "Has acertado "
            tAcertar2 = " de un total de "
            tSeguir = "¿Quieres seguir realizando operaciones?"
            tSi = "Si"
            tNo = "No"
            #-------------------------------------------------------------------
        if palabra == "MathGamePuntuacion":
            #Clase MathGamePuntuacion-------------------------------------------
            tPuntuacionL = "Puntuación: "
            tAceptar = "Vale"
            #-------------------------------------------------------------------
        if palabra == "MathGameAjustes":
            #Clase MathGameAjustes----------------------------------------------
            tVersion = "Ajustes - v"
            tDificultad = "Dificultad: "
            tPreguntas = "Nº preguntas: "
            tProblemasB = "Problemas: "
            tMantener = "Mantener ajustes: "
            tIdioma = "Idioma: "
            tVolver = "Volver"
            tSeleccionar = "(Seleccionar)"
            tSiAjustes = "(Si)"
            tNoAjustes = "(No)"
            #-------------------------------------------------------------------
        if palabra == "MathGameExtras":
            #Clase MathGameExtras-----------------------------------------------
            tExtrasL = "Extras"
            tDrake = "Ecuación de Drake"
            tVolver = "Volver"
            #-------------------------------------------------------------------
        if palabra == "funArchivos":
            #Funcion de archivos------------------------------------------------
            tFacil = "Fácil"
            tNormal = "Normal"
            tDificil = "Dificil"
            tSupervivencia = "(Supervivencia)"
            #-------------------------------------------------------------------

    if idiomaApp == "En":
        if palabra == "MathGame":
            #Clase MathGame-----------------------------------------------------
            tJugar = "Play"
            tExtras = "Extras"
            tPuntuacion = "Score"
            tAjustes = "Settings"
            #-------------------------------------------------------------------
        if palabra == "MathGameIntermission":
            #Clase MathGameIntermission-----------------------------------------
            tVas = "You will do: "
            tVamos = "Let's choose the desired parameters"
            tAceptar = "Vale"
            #-------------------------------------------------------------------
        if palabra == "MathGameD":
            #Clase MathGameD----------------------------------------------------
            tEmpecemos = "Let's start"
            tSeleccione = "Choose difficulty"
            tFacil = "Easy"
            tNormal = "Normal"
            tDificil = "Hard"
            tSeleccionar = "(Choose)"
            #-------------------------------------------------------------------
        if palabra == "MathGameS":
            #Clase MathGameS----------------------------------------------------
            tEmpecemos = "Let's start"
            tQuieresSupervivencia = "Do you want to enable survival mode?"
            tSi = "Yes"
            tNo = "No"
            tSupervivencia = "(Survival)"
            tSeleccionar = "(Choose)"
            #-------------------------------------------------------------------
        if palabra == "MathGameP":
            #Clase MathGameP----------------------------------------------------
            tEmpecemos = "Let's start"
            tCuantas = "How many problems do you want? (from 1 to 5)"
            tSeleccionar = "(Choose)"
            #-------------------------------------------------------------------
        if palabra == "MathGameSelOpe":
            #Clase MathGameSelOpe-----------------------------------------------
            tEmpecemos = "Let's start"
            tProblemas = "Choose type of problems"
            tSumas = "Sums"
            tRestas = "Subtractions"
            tMultiplicaciones = "Multiplications"
            tDivisiones = "Divisions"
            tSeleccionar = "(Choose)"
            #-------------------------------------------------------------------
        if palabra == "MathGameOperaciones":
            #Clase MathGameOperaciones------------------------------------------
            tEntreOperandos = "Between two numbers: "
            tRespuesta = "Choose the answer"
            tSalir = "Exit"
            tFinalizado = "You have finished"
            tAceptar = "Okay"
            tSumasentre = " Sums between two numbers: "
            tRestasentre = " Subtractions between two numbers: "
            tMultientre = " Multiplications between two numbers: "
            tDivisionentre = " Divisions between two numbers: "
            #Supervivencia------------------------------------------------------
            tVidas1 = "You have "
            tVidas2 = " lifes "
            tSinvidas = "You have lost all lifes"
            #-------------------------------------------------------------------
        if palabra == "MathGameComprobacion":
            #Clase MathGameComprobacion-----------------------------------------
            tResultado = "The answer was "
            tAceptar = "Okay"
            tHasacertado = "¡You nailed it!"
            #-------------------------------------------------------------------
            tAcertar1 = "You have answered correctly "
            tAcertar2 = " from a total of "
            tSeguir = "Do you want to repeat?"
            tSi = "Yes"
            tNo = "No"
            #-------------------------------------------------------------------
        if palabra == "MathGamePuntuacion":
            #Clase MathGamePuntuacion-------------------------------------------
            tPuntuacionL = "Score: "
            tAceptar = "Okay"
            #-------------------------------------------------------------------
        if palabra == "MathGameAjustes":
            #Clase MathGameAjustes----------------------------------------------
            tVersion = "Settings - v"
            tDificultad = "Difficulty: "
            tPreguntas = "Nº problems: "
            tProblemasB = "Problems: "
            tMantener = "Keep settings: "
            tIdioma = "Language: "
            tVolver = "Back"
            tSeleccionar = "(Choose)"
            tSiAjustes = "(Yes)"
            tNoAjustes = "(No)"
            #-------------------------------------------------------------------
        if palabra == "MathGameExtras":
            #Clase MathGameExtras-----------------------------------------------
            tExtrasL = "Extras"
            tDrake = "Drake's equation"
            tVolver = "Back"
            #-------------------------------------------------------------------
        if palabra == "funArchivos":
            #Funcion de archivos------------------------------------------------
            tFacil = "Easy"
            tNormal = "Normal"
            tDificil = "Hard"
            tSupervivencia = "(Survival)"
            #-------------------------------------------------------------------
#-------------------------------------------------------------------------------

#Creación y procesado de archivos-----------------------------------------------
def funArchivos():

    #Creacion Archivo Idioma----------------------------------------------------
    global idiomaApp
    global inicializarIdioma

    try:

        archivo = open("./idioma.txt", "x")
        archivo.write("")
        archivo.close()

        inicializarIdioma = 1

    except:

        idiomaDif = open("./idioma.txt", "r")
        contenidoIdioma = idiomaDif.read()

        idiomaApp = contenidoIdioma

        inicializarIdioma = 0
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
        funTraductor("funArchivos")

        if contenidoAjustes == "09150":
            modo_ajustes = 1
            RangoMin = 0
            RangoMax = 9
            modo_supervivencia = 1
            vida = 5
            numPreguntas = 0
            MultiPuntuacion = 1
            mostrar_modo_dificultad = tFacil
            mostrar_modo_numPreguntas = tSupervivencia

        if contenidoAjustes == "1099150":
            modo_ajustes = 1
            RangoMin = 10
            RangoMax = 99
            modo_supervivencia = 1
            vida = 5
            numPreguntas = 0
            MultiPuntuacion = 2
            mostrar_modo_dificultad = tNormal
            mostrar_modo_numPreguntas = tSupervivencia

        if contenidoAjustes == "100999150":
            modo_ajustes = 1
            RangoMin = 100
            RangoMax = 999
            modo_supervivencia = 1
            vida = 5
            numPreguntas = 0
            MultiPuntuacion = 3
            mostrar_modo_dificultad = tDificil
            mostrar_modo_numPreguntas = tSupervivencia

        if contenidoAjustes == "09001":
            modo_ajustes = 1
            RangoMin = 0
            RangoMax = 9
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 1
            MultiPuntuacion = 1
            mostrar_modo_dificultad = tFacil
            mostrar_modo_numPreguntas = "(1)"

        if contenidoAjustes == "09002":
            modo_ajustes = 1
            RangoMin = 0
            RangoMax = 9
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 2
            MultiPuntuacion = 1
            mostrar_modo_dificultad = tFacil
            mostrar_modo_numPreguntas = "(2)"

        if contenidoAjustes == "09003":
            modo_ajustes = 1
            RangoMin = 0
            RangoMax = 9
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 3
            MultiPuntuacion = 1
            mostrar_modo_dificultad = tFacil
            mostrar_modo_numPreguntas = "(3)"

        if contenidoAjustes == "09004":
            modo_ajustes = 1
            RangoMin = 0
            RangoMax = 9
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 4
            MultiPuntuacion = 1
            mostrar_modo_dificultad = tFacil
            mostrar_modo_numPreguntas = "(4)"

        if contenidoAjustes == "09005":
            modo_ajustes = 1
            RangoMin = 0
            RangoMax = 9
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 5
            MultiPuntuacion = 1
            mostrar_modo_dificultad = tFacil
            mostrar_modo_numPreguntas = "(5)"

        if contenidoAjustes == "1099001":
            modo_ajustes = 1
            RangoMin = 10
            RangoMax = 99
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 1
            MultiPuntuacion = 2
            mostrar_modo_dificultad = tNormal
            mostrar_modo_numPreguntas = "(1)"

        if contenidoAjustes == "1099002":
            modo_ajustes = 1
            RangoMin = 10
            RangoMax = 99
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 2
            MultiPuntuacion = 2
            mostrar_modo_dificultad = tNormal
            mostrar_modo_numPreguntas = "(2)"

        if contenidoAjustes == "1099003":
            modo_ajustes = 1
            RangoMin = 10
            RangoMax = 99
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 3
            MultiPuntuacion = 2
            mostrar_modo_dificultad = tNormal
            mostrar_modo_numPreguntas = "(3)"

        if contenidoAjustes == "1099004":
            modo_ajustes = 1
            RangoMin = 10
            RangoMax = 99
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 4
            MultiPuntuacion = 2
            mostrar_modo_dificultad = tNormal
            mostrar_modo_numPreguntas = "(4)"

        if contenidoAjustes == "1099005":
            modo_ajustes = 1
            RangoMin = 10
            RangoMax = 99
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 5
            MultiPuntuacion = 2
            mostrar_modo_dificultad = tNormal
            mostrar_modo_numPreguntas = "(5)"

        if contenidoAjustes == "100999001":
            modo_ajustes = 1
            RangoMin = 100
            RangoMax = 999
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 1
            MultiPuntuacion = 3
            mostrar_modo_dificultad = tDificil
            mostrar_modo_numPreguntas = "(1)"

        if contenidoAjustes == "100999002":
            modo_ajustes = 1
            RangoMin = 100
            RangoMax = 999
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 2
            MultiPuntuacion = 3
            mostrar_modo_dificultad = tDificil
            mostrar_modo_numPreguntas = "(2)"

        if contenidoAjustes == "100999003":
            modo_ajustes = 1
            RangoMin = 100
            RangoMax = 999
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 3
            MultiPuntuacion = 3
            mostrar_modo_dificultad = tDificil
            mostrar_modo_numPreguntas = "(3)"

        if contenidoAjustes == "100999004":
            modo_ajustes = 1
            RangoMin = 100
            RangoMax = 999
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 4
            MultiPuntuacion = 3
            mostrar_modo_dificultad = tDificil
            mostrar_modo_numPreguntas = "(4)"

        if contenidoAjustes == "100999005":
            modo_ajustes = 1
            RangoMin = 100
            RangoMax = 999
            modo_supervivencia = 0
            vida = 0
            numPreguntas = 5
            MultiPuntuacion = 3
            mostrar_modo_dificultad = tDificil
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

class MathGameSelIdioma(App):

    def build(self):

        #Función que detecta el texto del botón seleccionado en pantalla--------
        def callback(instance):

            global modo_ajustes
            global idiomaApp
            global inicializarIdioma

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

            inicializarIdioma = 0

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

        #Interfaz---------------------------------------------------------------
        funTraductor("MathGameExtras")
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal') #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        consola = Label(text = "Extras")

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        drake = Button(text = "Ecuación de Drake",background_color = (0.1,0.2,0.6,0.6))
        drake.bind(on_press=callback)

        volver = Button(text = "Volver",background_color = (0.1,0.2,0.6,0.6))
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

        #Interfaz---------------------------------------------------------------
        funTraductor("MathGameIntermission")
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal') #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        if modo_ajustes == 1:
            consola = Label(text = tVas+mostrar_modo_problemas)
        else:
            consola = Label(text = tVamos)

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        vale = Button(text = tAceptar,background_color = (0.1,0.2,0.6,0.6))
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

    global mantener_toggle
    mantener_toggle = 0

    def build(self):

        global volver_toggle
        volver_toggle = 0

        #Función que detecta el texto del botón seleccionado en pantalla--------
        def funDificultad(instance):

            global modo_ajustes

            print(instance.text)

            modo_ajustes = 1
            superBox.remove_widget(cabecera)
            MathGameD().run()

        def funPreguntas(instance):

            global modo_ajustes

            print(instance.text)

            modo_ajustes = 1
            superBox.remove_widget(cabecera)
            MathGameS().run()

        def funProblemas(instance):

            global modo_ajustes

            print(instance.text)

            modo_ajustes = 1
            superBox.remove_widget(cabecera)
            MathGameSelOpe().run()

        def funVolver(instance):

            global modo_ajustes
            global mantener_toggle

            print(instance.text)

            if mantener_toggle == 1:
                #Guardar config con guardado activo-----------------------------
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
                #---------------------------------------------------------------
                #Guardar config con guardado activo-----------------------------
                ajustesDif = open("./ajustes2.txt", "w")
                ajustesDif.write(respuestaOperaciones)
                ajustesDif.close()
                #---------------------------------------------------------------

            superBox.remove_widget(cabecera)
            MathGame().run()

        def funIdioma(instance):

            global modo_ajustes

            print(instance.text)

            modo_ajustes = 1
            superBox.remove_widget(cabecera)
            MathGameSelIdioma().run()

        def funMantener(instance):

            global modo_ajustes
            global mantener_toggle

            print(instance.text)

            if mantener_toggle == 0:
                mantener_toggle = 1
            else:
                mantener_toggle = 0

            superBox.remove_widget(cabecera)
            MathGameAjustes().run()
        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        funTraductor("MathGameAjustes")

        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='vertical') #Primer div---------------

        #Crear elementos de cabecera--------------------------------------------
        consola = Label(text = tVersion+version)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        #Dificultad-------------------------------------------------------------
        try:
            dificultad = Button(text = tDificultad+mostrar_modo_dificultad,background_color = (0.1,0.2,0.6,0.6))
            dificultad.bind(on_press=funDificultad)

        except:
            dificultad = Button(text = tDificultad+tSeleccionar,background_color = (0.1,0.2,0.6,0.6))
            volver_toggle = volver_toggle + 1
            dificultad.bind(on_press=funDificultad)

        #Número preguntas-------------------------------------------------------
        try:
            preguntas = Button(text = tPreguntas+mostrar_modo_numPreguntas,background_color = (0.1,0.2,0.6,0.6))
            preguntas.bind(on_press=funPreguntas)

        except:
            preguntas = Button(text = tPreguntas+tSeleccionar,background_color = (0.1,0.2,0.6,0.6))
            volver_toggle = volver_toggle + 1
            preguntas.bind(on_press=funPreguntas)

        #Problemas--------------------------------------------------------------
        try:
            problemas = Button(text = tProblemasB+mostrar_modo_problemas,background_color = (0.1,0.2,0.6,0.6))
            problemas.bind(on_press=funProblemas)

        except:
            problemas = Button(text = tProblemasB+tSeleccionar,background_color = (0.1,0.2,0.6,0.6))
            volver_toggle = volver_toggle + 1
            problemas.bind(on_press=funProblemas)

        #Volver-----------------------------------------------------------------
        if mantener_toggle == 1 and volver_toggle != 0:
            volver = Button(text = tVolver,background_color = (0.1,0.2,0.6,0.3))
        else:
            volver = Button(text = tVolver,background_color = (0.1,0.2,0.6,0.6))
            volver.bind(on_press=funVolver)

        #Mantener---------------------------------------------------------------
        if mantener_toggle == 0:
            mantener = Button(text = tMantener+tNoAjustes,background_color = (0.1,0.2,0.6,0.6))
            mantener.bind(on_press=funMantener)
        else:
            mantener = Button(text = tMantener+tSiAjustes,background_color = (0.1,0.2,0.6,0.6))
            mantener.bind(on_press=funMantener)

        #Idioma-----------------------------------------------------------------
        idioma = Button(text = tIdioma+idiomaApp,background_color = (0.1,0.2,0.6,0.6))
        idioma.bind(on_press=funIdioma)

        espacio0 = Label(text = "")
        espacio1 = Label(text = "")
        espacio2 = Label(text = "")
        espacio3 = Label(text = "")

        #Añadir elementos al pie------------------------------------------------
        cabecera.add_widget(espacio3)
        cabecera.add_widget(consola)
        cabecera.add_widget(espacio2)
        cabecera.add_widget(dificultad)
        cabecera.add_widget(preguntas)
        cabecera.add_widget(problemas)
        cabecera.add_widget(mantener)
        cabecera.add_widget(espacio0)
        cabecera.add_widget(idioma)
        cabecera.add_widget(espacio1)
        cabecera.add_widget(volver)

        #Añadir cada división al layout global----------------------------------
        superBox.add_widget(cabecera)

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

        #Interfaz---------------------------------------------------------------
        funTraductor("MathGamePuntuacion")
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal') #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        consola = Label(text = tPuntuacionL+archivo.read())

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        aceptar = Button(text = tAceptar,background_color = (0.1,0.2,0.6,0.6))
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

        #Interfaz---------------------------------------------------------------
        funTraductor("MathGameComprobacion")
        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal
        cabecera = BoxLayout(orientation ='horizontal')

        if comprobacion == 0:

            if modo_supervivencia == 1:

                global vida
                vida = vida - 1

            resultadoMostrar = str(resultadoreal)
            consola = Label(text = tResultado+resultadoMostrar)

        else:

            #victory.play()
            consola = Label(text = tHasacertado)

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical
        pie = BoxLayout(orientation ='vertical')

        aceptar = Button(text = tAceptar,background_color = (0.1,0.2,0.6,0.6))
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

            if respuestaSeleccionada == tSi:

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

        #Interfaz---------------------------------------------------------------
        funTraductor("MathGameComprobacion")

        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal')

        consola = Label(text = tAcertar1+puntuacion+tAcertar2+ContadorPreguntas)

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        bienvenida = Label(text = tSeguir)

        aceptar = Button(text = tSi,background_color = (0.1,0.2,0.6,0.6))
        aceptar.bind(on_press=callback)

        rechazar = Button(text = tNo,background_color = (0.1,0.2,0.6,0.6))
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

            if Seleccion == tSalir:
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

            #Interfaz-----------------------------------------------------------
            funTraductor("MathGameOperaciones")

            #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
            superBox = BoxLayout(orientation ='vertical')

            #Widgets de cabecera añadidos en el plano horizontal----------------
            cabecera = BoxLayout(orientation ='horizontal')

            if modo_supervivencia == 1:

                vidaStr = str(vida)
                if operacion == "Sumas":
                    consola = Label(text = tVidas1+vidaStr+tVidas2+"|"+tSumasentre+mostrarnumero1+" + "+mostrarnumero2)
                else:
                    if operacion == "Restas":
                        consola = Label(text = tVidas1+vidaStr+tVidas2+"|"+tRestasentre+mostrarnumero1+" - "+mostrarnumero2)
                    else:
                        if operacion == "Multiplicaciones":
                            consola = Label(text = tVidas1+vidaStr+tVidas2+"|"+tMultientre+mostrarnumero1+" x "+mostrarnumero2)
                        else:
                            consola = Label(text = tVidas1+vidaStr+tVidas2+"|"+tDivisionentre+mostrarnumero1+" / "+mostrarnumero2)

            else:

                if operacion == "Sumas":
                    consola = Label(text = tSumasentre+mostrarnumero1+" + "+mostrarnumero2)
                else:
                    if operacion == "Restas":
                        consola = Label(text = tRestasentre+mostrarnumero1+" - "+mostrarnumero2)
                    else:
                        if operacion == "Multiplicaciones":
                            consola = Label(text = tMultientre+mostrarnumero1+" x "+mostrarnumero2)
                        else:
                            consola = Label(text = tDivisionentre+mostrarnumero1+" / "+mostrarnumero2)

            cabecera.add_widget(consola)

            #Widgets de pie de página añadidos en el plano vertical-------------
            pie = BoxLayout(orientation ='vertical')

            bienvenida = Button(text = tRespuesta,background_color = (0.1,0.2,0.6,0.6))
            bienvenida.bind(on_press=callback)

            salidaOperaciones = Button(text = tSalir,background_color = (0.1,0.2,0.6,0.6))
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

        #InterfazFinal----------------------------------------------------------
        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal')

        if modo_supervivencia == 1:

            vidaStr = str(vida)
            consola = Label(text = tSinvidas)

        else:

            consola = Label(text = tFinalizado)

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        vale = Button(text = tAceptar,background_color = (0.1,0.2,0.6,0.6))
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

        funTraductor("MathGameSelOpe")

        #Función que registra el botón seleccionado-----------------------------
        def callback(instance):

            funTraductor("MathGameSelOpe")

            global operacion
            global modo_ajustes
            global mostrar_modo_problemas
            global respuestaOperaciones

            respuestaOperaciones = instance.text #contiene el string del boton
            print(instance.text)

            if respuestaOperaciones == tSumas:
                operacion = "Sumas"
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)

                if modo_ajustes == 1:
                    mostrar_modo_problemas = tSumas
                    MathGameAjustes().run()
                else:
                    mostrar_modo_problemas = tSeleccionar
                    MathGameOperaciones().run()
            else:
                if respuestaOperaciones == tRestas:
                    operacion = "Restas"
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)

                    if modo_ajustes == 1:
                        mostrar_modo_problemas = tRestas
                        MathGameAjustes().run()
                    else:
                        mostrar_modo_problemas = tSeleccionar
                        MathGameOperaciones().run()
                else:
                    if respuestaOperaciones == tMultiplicaciones:
                        operacion = "Multiplicaciones"
                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)

                        if modo_ajustes == 1:
                            mostrar_modo_problemas = tMultiplicaciones
                            MathGameAjustes().run()
                        else:
                            mostrar_modo_problemas = tSeleccionar
                            MathGameOperaciones().run()
                    else:
                        operacion = "Divisiones"
                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)

                        if modo_ajustes == 1:
                            mostrar_modo_problemas = tDivisiones
                            MathGameAjustes().run()
                        else:
                            mostrar_modo_problemas = tSeleccionar
                            MathGameOperaciones().run()

        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal
        cabecera = BoxLayout(orientation ='horizontal')

        consola = Label(text = tEmpecemos)

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical
        pie = BoxLayout(orientation ='vertical')

        bienvenida = Label(text = tProblemas)

        sumas = Button(text = tSumas,background_color = (0.1,0.2,0.6,0.6))
        sumas.bind(on_press=callback)

        restas = Button(text = tRestas,background_color = (0.1,0.2,0.6,0.6))
        restas.bind(on_press=callback)

        multiplicaciones = Button(text = tMultiplicaciones,background_color = (0.1,0.2,0.6,0.6))
        multiplicaciones.bind(on_press=callback)

        divisiones = Button(text = tDivisiones,background_color = (0.1,0.2,0.6,0.6))
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

        funTraductor("MathGameP")

        #Funcion que registra el botón seleccionado-----------------------------
        def callback(instance):

            funTraductor("MathGameP")

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
                    mostrar_modo_numPreguntas = tSeleccionar
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
                        mostrar_modo_numPreguntas = tSeleccionar
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
                            mostrar_modo_numPreguntas = tSeleccionar
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
                                mostrar_modo_numPreguntas = tSeleccionar
                                MathGameSelOpe().run()
                        else:
                            numPreguntas = 5
                            superBox.remove_widget(pie)
                            superBox.remove_widget(cabecera)

                            if modo_ajustes == 1:
                                mostrar_modo_numPreguntas = "(5)"
                                MathGameAjustes().run()
                            else:
                                mostrar_modo_numPreguntas = tSeleccionar
                                MathGameSelOpe().run()

        #Interfaz---------------------------------------------------------------
        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal')

        #Elementos de cabecera--------------------------------------------------
        consola = Label(text = tEmpecemos)

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Elementos del pie------------------------------------------------------
        bienvenida = Label(text = tCuantas)

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

        funTraductor("MathGameS")

        #Función que registra el texto del botón seleccionado-------------------
        def callback(instance):

            funTraductor("MathGameS")

            global modo_supervivencia
            global numPreguntas
            global vida
            global vidascii
            global modo_ajustes
            global mostrar_modo_numPreguntas

            respuestaSupervivencia = instance.text #contiene el string del boton
            print(instance.text)
            if respuestaSupervivencia == tSi:

                modo_supervivencia = 1
                vida = 5

                vidascii = "♥"
                numPreguntas = 0

                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)

                if modo_ajustes == 1:
                    mostrar_modo_numPreguntas = tSupervivencia
                    MathGameAjustes().run()
                else:
                    mostrar_modo_numPreguntas = tSeleccionar
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

        consola = Label(text = tEmpecemos)

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Creación de elementos--------------------------------------------------
        bienvenida = Label(text = tQuieresSupervivencia)

        aceptar = Button(text = tSi,background_color = (0.1,0.2,0.6,0.6))
        aceptar.bind(on_press=callback)

        rechazar = Button(text = tNo,background_color = (0.1,0.2,0.6,0.6))
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

        funTraductor("MathGameD")

        #Función que detecta el texto del botón seleccionado en pantalla--------
        def callback(instance):

            funTraductor("MathGameD")

            global dificultad
            global RangoMin
            global RangoMax
            global MultiPuntuacion
            global modo_ajustes
            global mostrar_modo_dificultad

            dificultadSeleccionada = instance.text #contiene el string del boton
            print(instance.text)
            if dificultadSeleccionada == tFacil:
                dificultad = "F"
                RangoMin = 0
                RangoMax = 9
                MultiPuntuacion = 1
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)

                if modo_ajustes == 1:
                    mostrar_modo_dificultad = tFacil
                    MathGameAjustes().run()
                else:
                    mostrar_modo_dificultad = tSeleccionar
                    MathGameS().run()
            else:
                if dificultadSeleccionada == tNormal:
                    dificultad = "N"
                    RangoMin = 10
                    RangoMax = 99
                    MultiPuntuacion = 2
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)

                    if modo_ajustes == 1:
                        mostrar_modo_dificultad = tNormal
                        MathGameAjustes().run()
                    else:
                        mostrar_modo_dificultad = tSeleccionar
                        MathGameS().run()
                else:
                    dificultad = "D"
                    RangoMin = 100
                    RangoMax = 999
                    MultiPuntuacion = 3
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)

                    if modo_ajustes == 1:
                        mostrar_modo_dificultad = tDificil
                        MathGameAjustes().run()
                    else:
                        mostrar_modo_dificultad = tSeleccionar
                        MathGameS().run()
        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal') #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        consola = Label(text = tEmpecemos)

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        bienvenida = Label(text = tSeleccione)

        dificultadFacil = Button(text = tFacil,background_color = (0.1,0.2,0.6,0.6))
        dificultadFacil.bind(on_press=callback)

        dificultadNormal = Button(text = tNormal,background_color = (0.1,0.2,0.6,0.6))
        dificultadNormal.bind(on_press=callback)

        dificultadDificil = Button(text = tDificil,background_color = (0.1,0.2,0.6,0.6))
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

        #Creacion Archivo Idioma------------------------------------------------
        global idiomaApp

        try:

            archivo = open("./idioma.txt", "x")
            archivo.write("")
            archivo.close()

            MathGameSelIdioma().run()

        except:

            if inicializarIdioma == 1:
                MathGameSelIdioma().run()

            idiomaDif = open("./idioma.txt", "r")
            contenidoIdioma = idiomaDif.read()

            idiomaApp = contenidoIdioma
        #-----------------------------------------------------------------------

        #Función que detecta el texto del botón seleccionado en pantalla--------
        def callback(instance):

            Seleccion = instance.text #contiene el string del boton
            print(instance.text)

            if Seleccion == tJugar:
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameIntermission().run()

            if Seleccion == tPuntuacion:
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGamePuntuacion().run()

            if Seleccion == tAjustes:
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameAjustes().run()

            if Seleccion == tExtras:
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameExtras().run()
        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        funTraductor("MathGame")

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
        jugar = Button(text = tJugar,background_color = (0.1,0.2,0.6,0.6))
        jugar.bind(on_press=callback)

        puntuacion = Button(text = tPuntuacion,background_color = (0.1,0.2,0.6,0.6))
        puntuacion.bind(on_press=callback)

        ajustes = Button(text = tAjustes,background_color = (0.1,0.2,0.6,0.6))
        ajustes.bind(on_press=callback)

        extras = Button(text = tExtras,background_color = (0.1,0.2,0.6,0.6))
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
