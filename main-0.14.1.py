#!/usr/bin/python3
version = "0.14.1"

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from random import randrange

#Pedir permisos android---------------------------------------------------------
#from android.permissions import request_permissions, Permission
#request_permissions([Permission.READ_EXTERNAL_STORAGE])
#-------------------------------------------------------------------------------

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
                consola = Label(text = '''La ecuación de Drake identifica los
factores específicos que, se cree, tienen
un papel importante en el desarrollo de
las civilizaciones.

Aunque en la actualidad no hay datos
suficientes para resolver la ecuación,
la comunidad científica ha aceptado
su relevancia como primera aproximación
teórica al problema, y varios científicos
la han utilizado como herramienta para
plantear distintas hipótesis.''')
                pag = pag + 1
            else:
                if pag == 2:
                    consola = Label(text = '''Nuestro Sol es solo una estrella
solitaria en la abundancia de 7×10^22
estrellas en el universo observable.

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
                if SeleccionEcuacion == "R*" or SeleccionEcuacion == vR:
                    vR = resultadoAintroducir
                    global Var1
                    Var1 = float(vR)
                else:
                    if SeleccionEcuacion == "Fp" or SeleccionEcuacion == vFp:
                        vFp = resultadoAintroducir
                        global Var2
                        Var2 = float(vFp)
                    else:
                        if SeleccionEcuacion == "Ne" or SeleccionEcuacion == vNe:
                            vNe = resultadoAintroducir
                            global Var3
                            Var3 = float(vNe)
                        else:
                            if SeleccionEcuacion == "Fl" or SeleccionEcuacion == vFl:
                                vFl = resultadoAintroducir
                                global Var4
                                Var4 = float(vFl)
                            else:
                                if SeleccionEcuacion == "Fi" or SeleccionEcuacion == vFi:
                                    vFi = resultadoAintroducir
                                    global Var5
                                    Var5 = float(vFi)
                                else:
                                    if SeleccionEcuacion == "Fc" or SeleccionEcuacion == vFc:
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
        consola = Label(text = "Seleccione el valor")

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

    global contadorBloqueo
    contadorBloqueo = 0

    def build(self):

        global contadorBloqueo

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

            global contadorBloqueo

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

                    contadorBloqueo = 0

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

                        contadorBloqueo = 1

                        superBox.remove_widget(pie)
                        superBox.remove_widget(cuerpo)
                        superBox.remove_widget(cabecera)
                        MathGameDrake().run()

                    else:
                        if contadorBloqueo == 0:
                            global SeleccionEcuacion
                            SeleccionEcuacion = Seleccion

                            superBox.remove_widget(pie)
                            superBox.remove_widget(cuerpo)
                            superBox.remove_widget(cabecera)
                            MathGameDrakeV().run()
                        else:
                            superBox.remove_widget(pie)
                            superBox.remove_widget(cuerpo)
                            superBox.remove_widget(cabecera)
                            MathGameDrake().run()
        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='vertical',size_hint =(1, 0.5)) #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        try:
            resultadoDrake = Var1*Var2*Var3*Var4*Var5*Var6*Var7
            strResultadoDrake = str(resultadoDrake)
            N = Label(text = strResultadoDrake,size_hint =(1, 0.01))

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

        if contadorBloqueo == 1:
                R = Button(text = vR,background_color = (0.1,0.2,0.6,0.3),size_hint =(1, 0.25))
                Fp = Button(text = vFp,background_color = (0.1,0.2,0.6,0.3),size_hint =(1, 0.25))
                Ne = Button(text = vNe,background_color = (0.1,0.2,0.6,0.3),size_hint =(1, 0.25))
                Fl = Button(text = vFl,background_color = (0.1,0.2,0.6,0.3),size_hint =(1, 0.25))
                Fi = Button(text = vFi,background_color = (0.1,0.2,0.6,0.3),size_hint =(1, 0.25))
                Fc = Button(text = vFc,background_color = (0.1,0.2,0.6,0.3),size_hint =(1, 0.25))
                L = Button(text = vL,background_color = (0.1,0.2,0.6,0.3),size_hint =(1, 0.25))
        else:
                R = Button(text = vR,background_color = (0.1,0.2,0.6,0.6),size_hint =(1, 0.25))
                Fp = Button(text = vFp,background_color = (0.1,0.2,0.6,0.6),size_hint =(1, 0.25))
                Ne = Button(text = vNe,background_color = (0.1,0.2,0.6,0.6),size_hint =(1, 0.25))
                Fl = Button(text = vFl,background_color = (0.1,0.2,0.6,0.6),size_hint =(1, 0.25))
                Fi = Button(text = vFi,background_color = (0.1,0.2,0.6,0.6),size_hint =(1, 0.25))
                Fc = Button(text = vFc,background_color = (0.1,0.2,0.6,0.6),size_hint =(1, 0.25))
                L = Button(text = vL,background_color = (0.1,0.2,0.6,0.6),size_hint =(1, 0.25))

        R.bind(on_press=callback)
        Fp.bind(on_press=callback)
        Ne.bind(on_press=callback)
        Fl.bind(on_press=callback)
        Fi.bind(on_press=callback)
        Fc.bind(on_press=callback)
        L.bind(on_press=callback)

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
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal') #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        if modo_ajustes == 1:
            consola = Label(text = "Vas a realizar: "+operacion)
        else:
            consola = Label(text = "Vamos a seleccionar los parámetros deseados")

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        vale = Button(text = "Vale",background_color = (0.1,0.2,0.6,0.6))
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

    if firstRun == 1:
        #El modo ajustes se inicia en la clase principal (cambiar allí)-------------
        mostrar_modo_ajustes = "(No)"
        #---------------------------------------------------------------------------
        mostrar_modo_dificultad = "(Seleccionar)"
        mostrar_modo_numPreguntas = "(Seleccionar)"
        mostrar_modo_problemas = "(Seleccionar)"
        volver_bloquear = 0
        bloquear = 1
    else:
        mostrar_modo_ajustes = "(Si)"
        volver_bloquear = 1
        bloquear = 0

    def build(self):

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

            Seleccion = instance.text #contiene el string del boton
            print(instance.text)

            if Seleccion == "Dificultad: "+mostrar_modo_dificultad:
                if modo_ajustes == 1:
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)
                    MathGameD().run()
                else:
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)
                    MathGameAjustes().run()
            else:
                if Seleccion == "Nº preguntas: "+mostrar_modo_numPreguntas:
                    if modo_ajustes == 1:
                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)
                        MathGameS().run()
                    else:
                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)
                        MathGameAjustes().run()
                else:
                    if Seleccion == "Problemas: "+mostrar_modo_problemas:
                        if modo_ajustes == 1:
                            superBox.remove_widget(pie)
                            superBox.remove_widget(cabecera)
                            MathGameSelOpe().run()
                        else:
                            superBox.remove_widget(pie)
                            superBox.remove_widget(cabecera)
                            MathGameAjustes().run()
                    else:
                        if Seleccion == "Volver":
                            if modo_ajustes == 1:
                                if mostrar_modo_dificultad == "(Seleccionar)":
                                    superBox.remove_widget(pie)
                                    superBox.remove_widget(cabecera)
                                    MathGameAjustes().run()
                                else:
                                    if mostrar_modo_numPreguntas == "(Seleccionar)":
                                        superBox.remove_widget(pie)
                                        superBox.remove_widget(cabecera)
                                        MathGameAjustes().run()
                                    else:
                                        if mostrar_modo_problemas == "(Seleccionar)":
                                            superBox.remove_widget(pie)
                                            superBox.remove_widget(cabecera)
                                            MathGameAjustes().run()
                                        else:
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

                                            superBox.remove_widget(pie)
                                            superBox.remove_widget(cabecera)
                                            MathGame().run()
                            else:
                                superBox.remove_widget(pie)
                                superBox.remove_widget(cabecera)
                                MathGame().run()
                        else:
                            if modo_ajustes == 1:
                                modo_ajustes = 0
                                mostrar_modo_ajustes = "(No)"
                                volver_bloquear = 0
                                bloquear = 1

                                #Borrar el archivo de config--------------------
                                ajustesFile = open("./ajustes.txt", "w")
                                ajustesFile.write("0")
                                ajustesFile.close()
                                #-----------------------------------------------
                                #Borrar config con guardado activo--------------
                                ajustesDif = open("./ajustes2.txt", "w")
                                ajustesDif.write("0")
                                ajustesDif.close()
                                #-----------------------------------------------
                            else:
                                modo_ajustes = 1
                                mostrar_modo_ajustes = "(Sí)"
                                bloquear = 0

                                if mostrar_modo_dificultad == "(Seleccionar)" or mostrar_modo_numPreguntas == "(Seleccionar)" or mostrar_modo_problemas == "(Seleccionar)":
                                    volver_bloquear = 1
                                else:
                                    #Guardar configuración al activar el guardado---
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
                                    #-------------------------------------------
                                    #Guardar config con guardado activo---------
                                    ajustesDif = open("./ajustes2.txt", "w")
                                    ajustesDif.write(respuestaOperaciones)
                                    ajustesDif.close()
                                    #-------------------------------------------

                            superBox.remove_widget(pie)
                            superBox.remove_widget(cabecera)
                            MathGameAjustes().run()
        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal') #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        consola = Label(text = "Ajustes - v"+version)

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        if bloquear == 0:
            dificultad = Button(text = "Dificultad: "+mostrar_modo_dificultad,background_color = (0.1,0.2,0.6,0.6))
            dificultad.bind(on_press=callback)

            preguntas = Button(text = "Nº preguntas: "+mostrar_modo_numPreguntas,background_color = (0.1,0.2,0.6,0.6))
            preguntas.bind(on_press=callback)

            problemas = Button(text = "Problemas: "+mostrar_modo_problemas,background_color = (0.1,0.2,0.6,0.6))
            problemas.bind(on_press=callback)
        else:
            dificultad = Button(text = "Dificultad: "+mostrar_modo_dificultad,background_color = (0.1,0.2,0.6,0.3))
            dificultad.bind(on_press=callback)

            preguntas = Button(text = "Nº preguntas: "+mostrar_modo_numPreguntas,background_color = (0.1,0.2,0.6,0.3))
            preguntas.bind(on_press=callback)

            problemas = Button(text = "Problemas: "+mostrar_modo_problemas,background_color = (0.1,0.2,0.6,0.3))
            problemas.bind(on_press=callback)

        mantener = Button(text = "Mantener ajustes: "+mostrar_modo_ajustes,background_color = (0.1,0.2,0.6,0.6))
        mantener.bind(on_press=callback)

        null = Label(text = "")

        if volver_bloquear == 0:
            volver = Button(text = "Volver",background_color = (0.1,0.2,0.6,0.6))
            volver.bind(on_press=callback)
        else:
            if mostrar_modo_dificultad != "(Seleccionar)" and mostrar_modo_numPreguntas != "(Seleccionar)" and mostrar_modo_problemas != "(Seleccionar)":
                volver = Button(text = "Volver",background_color = (0.1,0.2,0.6,0.6))
                volver.bind(on_press=callback)
            else:
                volver = Button(text = "Volver",background_color = (0.1,0.2,0.6,0.3))
                volver.bind(on_press=callback)

        #Añadir elementos al pie------------------------------------------------
        pie.add_widget(dificultad)
        pie.add_widget(preguntas)
        pie.add_widget(problemas)
        pie.add_widget(mantener)
        pie.add_widget(null)
        pie.add_widget(volver)

        #Añadir cada división al layout global----------------------------------
        superBox.add_widget(cabecera)
        superBox.add_widget(pie)

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
        aceptar = Button(text = "Vale",background_color = (0.1,0.2,0.6,0.6))
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

            #victory.play()
            consola = Label(text = "¡Has acertado!")

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical
        pie = BoxLayout(orientation ='vertical')

        aceptar = Button(text = "Vale",background_color = (0.1,0.2,0.6,0.6))
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
        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal')

        consola = Label(text = "Has acertado "+puntuacion+" de un total de "+ContadorPreguntas)

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        bienvenida = Label(text = "¿Quieres seguir realizando operaciones?")

        aceptar = Button(text = "si",background_color = (0.1,0.2,0.6,0.6))
        aceptar.bind(on_press=callback)

        rechazar = Button(text = "no",background_color = (0.1,0.2,0.6,0.6))
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
            #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
            superBox = BoxLayout(orientation ='vertical')

            #Widgets de cabecera añadidos en el plano horizontal----------------
            cabecera = BoxLayout(orientation ='horizontal')

            if modo_supervivencia == 1:

                vidaStr = str(vida)
                if operacion == "Sumas":
                    consola = Label(text = "Tienes "+vidaStr+" vidas "+"|"+" Sumas entre dos numeros: "+mostrarnumero1+" + "+mostrarnumero2)
                else:
                    if operacion == "Restas":
                        consola = Label(text = "Tienes "+vidaStr+" vidas "+"|"+" Restas entre dos numeros: "+mostrarnumero1+" - "+mostrarnumero2)
                    else:
                        if operacion == "Multiplicaciones":
                            consola = Label(text = "Tienes "+vidaStr+" vidas "+"|"+" Multiplicaciones entre dos numeros: "+mostrarnumero1+" x "+mostrarnumero2)
                        else:
                            consola = Label(text = "Tienes "+vidaStr+" vidas "+"|"+" Divisiones entre dos numeros: "+mostrarnumero1+" / "+mostrarnumero2)

            else:

                if operacion == "Sumas":
                    consola = Label(text = "Sumas entre dos numeros: "+mostrarnumero1+" + "+mostrarnumero2)
                else:
                    if operacion == "Restas":
                        consola = Label(text = "Restas entre dos numeros: "+mostrarnumero1+" - "+mostrarnumero2)
                    else:
                        if operacion == "Multiplicaciones":
                            consola = Label(text = "Multiplicaciones entre dos numeros: "+mostrarnumero1+" x "+mostrarnumero2)
                        else:
                            consola = Label(text = "Divisiones entre dos numeros: "+mostrarnumero1+" / "+mostrarnumero2)

            cabecera.add_widget(consola)

            #Widgets de pie de página añadidos en el plano vertical-------------
            pie = BoxLayout(orientation ='vertical')

            bienvenida = Button(text = "Seleccione la respuesta",background_color = (0.1,0.2,0.6,0.6))
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

        finalOperacion = 1

        #InterfazFinal----------------------------------------------------------
        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal')

        if modo_supervivencia == 1:

            vidaStr = str(vida)
            consola = Label(text = "Te has quedado sin vidas")

        else:

            consola = Label(text = "Has finalizado")

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        vale = Button(text = "Vale",background_color = (0.1,0.2,0.6,0.6))
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

            if respuestaOperaciones == "Sumas":
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
                if respuestaOperaciones == "Restas":
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
                    if respuestaOperaciones == "Multiplicaciones":
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

        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal
        cabecera = BoxLayout(orientation ='horizontal')

        consola = Label(text = "Empecemos con la configuración")

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical
        pie = BoxLayout(orientation ='vertical')

        bienvenida = Label(text = "Seleccione tipo de problemas")

        sumas = Button(text = "Sumas",background_color = (0.1,0.2,0.6,0.6))
        sumas.bind(on_press=callback)

        restas = Button(text = "Restas",background_color = (0.1,0.2,0.6,0.6))
        restas.bind(on_press=callback)

        multiplicaciones = Button(text = "Multiplicaciones",background_color = (0.1,0.2,0.6,0.6))
        multiplicaciones.bind(on_press=callback)

        divisiones = Button(text = "Divisiones",background_color = (0.1,0.2,0.6,0.6))
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

        #Interfaz---------------------------------------------------------------
        #Layout completo subdividido en dos sublayouts, uno vertical y otro horizontal
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal')

        #Elementos de cabecera--------------------------------------------------
        consola = Label(text = "Empecemos con la configuración")

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Elementos del pie------------------------------------------------------
        bienvenida = Label(text = "Cuántas preguntas quieres (del 1 al 5)")

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
            if respuestaSupervivencia == "Si":

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

        #Interfaz---------------------------------------------------------------
        #Layout global----------------------------------------------------------
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal')

        consola = Label(text = "Empecemos con la configuración")

        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Creación de elementos--------------------------------------------------
        bienvenida = Label(text = "¿Quieres activar el modo supervivencia?")

        aceptar = Button(text = "Si",background_color = (0.1,0.2,0.6,0.6))
        aceptar.bind(on_press=callback)

        rechazar = Button(text = "No",background_color = (0.1,0.2,0.6,0.6))
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
            if dificultadSeleccionada == "Fácil":
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
                if dificultadSeleccionada == "Normal":
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

        #Interfaz---------------------------------------------------------------
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal') #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        consola = Label(text = "Empecemos con la configuración")

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        bienvenida = Label(text = "Seleccione dificultad")

        dificultadFacil = Button(text = "Fácil",background_color = (0.1,0.2,0.6,0.6))
        dificultadFacil.bind(on_press=callback)

        dificultadNormal = Button(text = "Normal",background_color = (0.1,0.2,0.6,0.6))
        dificultadNormal.bind(on_press=callback)

        dificultadDificil = Button(text = "Dificil",background_color = (0.1,0.2,0.6,0.6))
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

    if firstRun == 1:
        global modo_ajustes
        modo_ajustes = 0 #(boolean (Descomentar al quitar archivos))------------

    def build(self):

        #Función que detecta el texto del botón seleccionado en pantalla--------
        def callback(instance):

            Seleccion = instance.text #contiene el string del boton
            print(instance.text)
            if Seleccion == "Jugar":
                superBox.remove_widget(pie)
                superBox.remove_widget(cabecera)
                MathGameIntermission().run()
            else:
                if Seleccion == "Puntuación":
                    superBox.remove_widget(pie)
                    superBox.remove_widget(cabecera)
                    MathGamePuntuacion().run()
                else:
                    if Seleccion == "Ajustes":
                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)
                        MathGameAjustes().run()
                    else:
                        superBox.remove_widget(pie)
                        superBox.remove_widget(cabecera)
                        MathGameExtras().run()
        #-----------------------------------------------------------------------

        #Interfaz---------------------------------------------------------------
        #Layout global de superBox cada widget dispuestos uno encima de otro----
        superBox = BoxLayout(orientation ='vertical')

        #Widgets de cabecera añadidos en el plano horizontal--------------------
        cabecera = BoxLayout(orientation ='horizontal') #Primer div-------------

        #Crear elementos de cabecera--------------------------------------------
        consola = Label(text = "¡Bienvenido a MathGame Android Edition!")

        #Añadir elementos a cabecera--------------------------------------------
        cabecera.add_widget(consola)

        #Widgets de pie de página añadidos en el plano vertical-----------------
        pie = BoxLayout(orientation ='vertical')

        #Crear elementos del pie------------------------------------------------
        jugar = Button(text = "Jugar",background_color = (0.1,0.2,0.6,0.6))
        jugar.bind(on_press=callback)

        puntuacion = Button(text = "Puntuación",background_color = (0.1,0.2,0.6,0.6))
        puntuacion.bind(on_press=callback)

        ajustes = Button(text = "Ajustes",background_color = (0.1,0.2,0.6,0.6))
        ajustes.bind(on_press=callback)

        extras = Button(text = "Extras",background_color = (0.1,0.2,0.6,0.6))
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
