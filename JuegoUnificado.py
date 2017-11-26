# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

#------MenuInicial---------------------------------------------------------------

class MenuInicial(pilasengine.escenas.Escena):
    def iniciar(self):

#-------Preparando el Fondo---------------------------------------------------

        gFondo = pilas.imagenes.cargar_grilla('Imagenes\FondoMenu.png', 12)
        fondo = pilas.actores.Animacion(gFondo, ciclica=True, velocidad= 10)
        pilas.camara.escala = 2.25
        fondo.z = 10

#-------------------Funciones de las opciones de menues---------------------------

        #def Iniciar_1player():
            #titulo.transparencia =[0, 100], 2
            #menu.transparencia = [0, 100], 2
            #pilas.escenas.MenuPersonajes()

        def Fight():
            pilas.escenas.CombatArena()

        def Menu_Instrucciones():
            pilas.escenas.MenInstrucciones()

        def Menu_Configuracion():
            pilas.escenas.Config()

        def Salir_Juego():
            pilas.terminar()

#---------------------Menu------------------------------------------------------
        
        global menuMI
        menuMI = pilas.actores.Menu(
            [
                #("1 Player", Iniciar_1player),
                ("Jugar", Fight),
                ("Instrucciones", Menu_Instrucciones),
                ("Configuracion", Menu_Configuracion),
                ("Salir", Salir_Juego),
            ])

#---------------Titulo y animacion de inicio-------------------------------------
        
        global tituloMI
        tituloMI = pilas.actores.Actor()
        tituloMI.imagen = "Imagenes\Titulo.png"
        tituloMI.transparencia=100
        menuMI.transparencia=100
        tituloMI.transparencia =[100, 0], 2
        menuMI.transparencia = [100, 100, 0], 2
        tituloMI.escala=.6
        tituloMI.y=60

#---------------------Salteo de animacion de inicio-------------------------

        #pilas.eventos.pulsa_tecla_escape.conectar(self.Skip)
        
    #def Skip(self, evento):
        #tituloMI.transparencia = 0
        #menuMI.transparencia = 0
        
#------------------------------------------------------------------------------






#--------------------------------------------------Clase-------------------------
#----------------------------------------------Instrucciones-------------------

class MenInstrucciones(pilasengine.escenas.Escena):
    def iniciar(self):
                
#-------Preparando el Fondo---------------------------------------------------
                
        gFondo = pilas.imagenes.cargar_grilla('Imagenes\FondoMenu.png', 12)
        fondo = pilas.actores.Animacion(gFondo, ciclica=True, velocidad= 10)
        pilas.camara.escala=2.25
        fondo.z=-10

#---------------------------------Instrucciones del juego----------------------------
                                
        Ins = pilas.actores.Texto("Kombat System es un juego de pelea donde cada personaje puede golpear, bloquear, moverse hacia los lados, saltar y, ademas, tiene una Habilidad Unica, la cual puede usarse una vez cargada la barra de energia,a travez de golpear al contrincante.")
        Ins.ancho=600
        Ins.escala=.8
        Ins.y=-50
        Ins.color= "grisclaro"

#--------------------------Subtexto para volver-------------------------                                
        volver = pilas.actores.Texto("Pulsa escape para volver al menu anterior")
        volver.escala=.5
        volver.x=-150
        volver.y=-220
        volver.color= "grisclaro"

#----------------------------Titulo del juego------------------------------
                                
        titulo = pilas.actores.Actor()
        titulo.imagen = "Imagenes\Titulo.png"
        titulo.escala=.6
        titulo.y=60

#-----------------Volver con escape------------------------------------------
        
        pilas.eventos.pulsa_tecla_escape.conectar(self.Volver)
        
    def Volver(self, evento):
        pilas.escenas.MenuInicial()
        
        
        
        
        
        
#-------------------------------Clase---------------------------------------------
#------------------------------Configuracion-----------------------------------

class Config(pilasengine.escenas.Escena):
    def iniciar(self):
                
#-------Preparando el Fondo---------------------------------------------------
                
        gFondo = pilas.imagenes.cargar_grilla('Imagenes\FondoMenu.png', 12)
        fondo = pilas.actores.Animacion(gFondo, ciclica=True, velocidad= 10)
        pilas.camara.escala=2.25
        fondo.z=10

#--------------------Funciones de opciones menu----------------------------------
                                
        #def Menu_Audio():
            #pilas.escenas.Audio()
            
        def Menu_Controles1():
            pilas.escenas.ControlesP1()
            
        def Menu_Controles2():
            pilas.escenas.ControlesP2()

#---------------------Menu de configuracion------------------------------------------
                                                                
        configuracion = pilas.actores.Menu(
            [
                #("Audio", Menu_Audio),
                ("Controles player 1", Menu_Controles1),
                ("Controles player 2", Menu_Controles2),
            ])

#--------------------------Subtexto para volver-------------------------                                
        volver = pilas.actores.Texto("Pulsa escape para volver al menu anterior")
        volver.escala=.5
        volver.x=-150
        volver.y=-220
        volver.color= "grisclaro"
        
#-----------------Titulo del juego----------------------------------------------------
                                
        titulo = pilas.actores.Actor()
        titulo.imagen = "Imagenes\Titulo.png"
        titulo.escala=.6
        titulo.y=60
        
#-----------------Volver con escape------------------------------------------
        
        pilas.eventos.pulsa_tecla_escape.conectar(self.Volver)
        
    def Volver(self, evento):
        pilas.escenas.MenuInicial()
        
        
        
        
#-----------------------------------------Clase------------------------------------
#-----------------------------Configuracion de audio--------------------------

class Audio(pilasengine.escenas.Escena):
    def iniciar(self):
                       
#-------Preparando el Fondo---------------------------------------------------
    
        gFondo = pilas.imagenes.cargar_grilla('Imagenes\FondoMenu.png', 12)
        fondo = pilas.actores.Animacion(gFondo, ciclica=True, velocidad= 10)
        pilas.camara.escala=2.25
        fondo.z=-10
 
#-----------------------Subtitulo------------------------------------------------------------
         
        subtitulo = pilas.actores.Texto("Audio", y = 80)
        subtitulo.y = 80
                      
#--------------------Nombre de opciones------------------------------------------------
 
        contr = pilas.actores.Texto("General\n \nEfectos de sonido\n \nMusica")
        contr.escala=.5
        contr.x=-120
        contr.y=-50
 
#-----------------------------Configuracion de audio---------------------------------------
           
        Grl = pilas.interfaz.Deslizador(75,-10)
        Efx = pilas.interfaz.Deslizador(75,-50)
        Mus = pilas.interfaz.Deslizador(75,-90)

#-----------------------------Boton de guardado---------------------------------------
            
        BtnGuardar = pilas.interfaz.Boton("Guardar", 50, -200)
            
            
#--------------------------Subtexto para volver-------------------------                                
        volver = pilas.actores.Texto("Pulsa escape para volver al menu anterior")
        volver.escala=.5
        volver.x=-150
        volver.y=-220
        volver.color= "grisclaro"
                
                                 
#-----------------------------Titulo del juego---------------------------------------
              
        titulo = pilas.actores.Actor()
        titulo.imagen = "Imagenes\Titulo.png"
        titulo.escala=.6
        titulo.y=60
        
#-----------------Volver con escape------------------------------------------
        
        pilas.eventos.pulsa_tecla_escape.conectar(self.Volver)
        
    def Volver(self, evento):
        pilas.escenas.Config()        

     
            
                            

#-----------------------------------------Clase---------------------------------
#-----------------------------------Config. player 1--------------------------

class ControlesP1(pilasengine.escenas.Escena):
    def iniciar(self):
                
#-------Preparando el Fondo---------------------------------------------------
                
        gFondo = pilas.imagenes.cargar_grilla('Imagenes\FondoMenu.png', 12)
        fondo = pilas.actores.Animacion(gFondo, ciclica=True, velocidad= 10)
        pilas.camara.escala=2.25
        fondo.z=-10

#-----------------------Subtitulo------------------------------------------------------------
                                        
        subtitulo = pilas.actores.Texto("Controles Player 1")
        subtitulo.y=80
                
#--------------------Nombre de opciones------------------------------------------------
 
        contr = pilas.actores.Texto("Saltar\n \nIzquierda\n \nDerecha\n \nGolpear\n \nBloquear\n \nHabilidad Especial")
        contr.escala=.5
        contr.x=-120
        contr.y=-50

#-----------------------------Definicion de teclas---------------------------------------
           
        Saltar = pilas.interfaz.IngresoDeTexto("Arriba",120,46,100,15)
        Izquierda = pilas.interfaz.IngresoDeTexto("Izquierda",120,6,100,15)
        Derecha = pilas.interfaz.IngresoDeTexto("Derecha",120,-36,100,15)
        Golpear = pilas.interfaz.IngresoDeTexto("J",120,-76,100,15)
        Bloquear = pilas.interfaz.IngresoDeTexto("K",120,-116,100,15)
        HabEspecial = pilas.interfaz.IngresoDeTexto("L",120,-156,100,15)

#--------------------------Boton de guardado---------------------------------------------
          
        BtnGuardar = pilas.interfaz.Boton("Guardar",0,-200)

#--------------------------Guardado de configuracion------------------------------------
           
        def guardar_cont_P1(self,saltar,izquierda,derecha,golpear,bloquear,habEspecial):
            saltar = Saltar.Texto
            izquierda = Izquierda.Texto
            derecha = Derecha.Texto
            golpear = Golpear.Texto
            bloquear = Bloquear.Texto
            habEspecial = HabEspecial.Texto

            
#--------------------------Subtexto para volver-------------------------                                
        volver = pilas.actores.Texto("Pulsa escape para volver al menu anterior")
        volver.escala=.5
        volver.x=-150
        volver.y=-220
        volver.color= "grisclaro"
                                          
                                        
#---------------------------Titulo del juego--------------------------------------------------            
                        
        titulo = pilas.actores.Actor()
        titulo.imagen = "Imagenes\Titulo.png"
        titulo.escala=.6
        titulo.y=60
        
#-----------------Volver con escape------------------------------------------
        
        pilas.eventos.pulsa_tecla_escape.conectar(self.Volver)
        
    def Volver(self, evento):
        pilas.escenas.Config()        







#------------------------Clase-----------------------------------------
#-----------------Config. de player 2-------------------------------

class ControlesP2(pilasengine.escenas.Escena):
    def iniciar(self):
                
#-------Preparando el Fondo---------------------------------------------------
                
        gFondo = pilas.imagenes.cargar_grilla('Imagenes\FondoMenu.png', 12)
        fondo = pilas.actores.Animacion(gFondo, ciclica=True, velocidad= 10)
        pilas.camara.escala=2.25
        fondo.z=-10

#-----------------------Subtitulo------------------------------------------------------------
                                
        subtitulo = pilas.actores.Texto("Controles Player 2")
        subtitulo.y=80
        
#--------------------Nombre de opciones------------------------------------------------
                
        contr = pilas.actores.Texto("Saltar\n \nIzquierda\n \nDerecha\n \nGolpear\n \nBloquear\n \nHabilidad Especial")
        contr.escala=.5
        contr.x=-120
        contr.y=-50

#-----------------------------Definicion de teclas---------------------------------------
                                
        Saltar = pilas.interfaz.IngresoDeTexto("W",120,46,100,15)
        Izquierda = pilas.interfaz.IngresoDeTexto("A",120,6,100,15)
        Derecha = pilas.interfaz.IngresoDeTexto("D",120,-36,100,15)
        Golpear = pilas.interfaz.IngresoDeTexto("F",120,-76,100,15)
        Bloquear = pilas.interfaz.IngresoDeTexto("G",120,-116,100,15)
        HabEspecial = pilas.interfaz.IngresoDeTexto("H",120,-156,100,15)

#--------------------------Boton de guardado---------------------------------------------
                                                                
        BtnGuardar = pilas.interfaz.Boton("Guardar",0,-200)

#--------------------------Guardado de configuracion------------------------------------
                                
        def guardar_cont_P2(self,saltar,izquierda,derecha,golpear,bloquear,habEspecial):
            saltar = Saltar.Texto
            izquierda = Izquierda.Texto
            derecha = Derecha.Texto
            golpear = Golpear.Texto
            bloquear = Bloquear.Texto
            habEspecial = HabEspecial.Texto
            

#--------------------------Subtexto para volver-------------------------                                
        volver = pilas.actores.Texto("Pulsa escape para volver al menu anterior")
        volver.escala=.5
        volver.x=-150
        volver.y=-220
        volver.color= "grisclaro"
                                          
                                        
#---------------------------Titulo del juego--------------------------------------------------            
                        
        titulo = pilas.actores.Actor()
        titulo.imagen = "Imagenes\Titulo.png"
        titulo.escala=.6
        titulo.y=60
        
#-----------------Volver con escape------------------------------------------
        
        pilas.eventos.pulsa_tecla_escape.conectar(self.Volver)
        
    def Volver(self, evento):
        pilas.escenas.Config()
        





#-------------------------------------Clase-------------------------------------
#-------------------------Seleccion de jugador-------------------------------

class MenuPersonajes(pilasengine.escenas.Escena):
    def iniciar(self):
        
#-------Preparando el Fondo---------------------------------------------------
        
        gFondo = pilas.imagenes.cargar_grilla('Imagenes\FondoMenu.png', 12)
        fondo = pilas.actores.Animacion(gFondo, ciclica=True, velocidad= 10)
        pilas.camara.escala=2.25
        fondo.z=10

#------------------Armando los cuadros de seleccion de PJ-------------------------
        global PJFacu                            
        PJFacu = pilas.actores.Actor(imagen = "Imagenes\Fighters\Facu.jpg", x=-60)
        PJFacu.escala = .1
        global PJRami
        PJRami = pilas.actores.Actor(imagen="Imagenes\Fighters\Rami.jpg")
        PJRami.escala = .1
        global PJNacho
        PJNacho = pilas.actores.Actor(imagen="Imagenes\Fighters\Nacho.jpg", x=60)
        PJNacho.escala = .1
        global PJFede
        PJFede = pilas.actores.Actor(imagen="Imagenes\Fighters\Fede.jpg", x=-60, y=-50)
        PJFede.escala = .1
        global PJStefan
        PJStefan = pilas.actores.Actor(imagen="Imagenes\Fighters\Stefan.jpg", y=-50)
        PJStefan.escala = .1
        global PJLucas
        PJLucas = pilas.actores.Actor(imagen="Imagenes\Fighters\Lucas.jpg", x=60, y=-50)
        PJLucas.escala = .1
                
#-------------------Subtitulo--------------------------------------------------------------
                
        subtitulo = pilas.actores.Texto("Selecciones su personaje")
        subtitulo.y=80

#--------------------Boton para empezar la pelea----------------------------------------
                     

#--------------------------Subtexto para volver-------------------------                                
        volver = pilas.actores.Texto("Pulsa escape para volver al menu anterior")
        volver.escala=.5
        volver.x=-150
        volver.y=-220
        volver.color= "grisclaro"
                                          
                                        
#---------------------------Titulo del juego--------------------------------------------------            
                        
        titulo = pilas.actores.Actor()
        titulo.imagen = "Imagenes\Titulo.png"
        titulo.escala=.6
        titulo.y=60
        
#-----------------Volver con escape------------------------------------------
        
        pilas.eventos.pulsa_tecla_escape.conectar(self.Volver)
        pilas.evento.click_de_mouse.conectar(self.seleccionarPJ)
        global contador
        contador = 0
        
        
        #pizarra.rectangulo(0, 0, 4, 4, color = pilas.colores.verde, relleno = True)
        
    def Volver(self, evento):
        pilas.escenas.MenuInicial()
        
    def seleccionarPJ(self, evento):
        pizarra = pilas.actores.Pizarra()
        pizarra.z = 1
        
        if contador == 0:
            
            #Primera fila de jugadores
            if evento.y>-44 and evento.y<46:
                
                #Facu
                if evento.x>-179 and evento.x<-90:
                    pizarra.rectangulo(PJFacu.x-22, PJFacu.y+22, 43, 43, color = pilas.colores.verde, relleno = True)
                    contador = contador + 1
                        
                #Rami
                elif evento.x>-46 and evento.x<43:
                    pizarra.rectangulo(PJRami.x-22, PJRami.y+22, 43, 43, color = pilas.colores.verde, relleno = True)
                    print (cont)
                    contador+1
                    
                #Nacho
                elif evento.x>89 and evento.x<178:
                    pizarra.rectangulo(PJNacho.x-22, PJNacho.y+22, 43, 43, color = pilas.colores.verde, relleno = True)
                    contador+1
            
            #Segunda fila de jugadores        
            elif evento.y>-156 and evento.y<-66:
                
                #Fede
                if evento.x>-179 and evento.x<-90:
                    pizarra.rectangulo(PJFede.x-22, PJFede.y+22, 43, 43, color = pilas.colores.verde, relleno = True)
                    contador+1
                    
                #Stefan
                elif evento.x>-46 and evento.x<43:
                    pizarra.rectangulo(PJStefan.x-22, PJStefan.y+22, 43, 43, color = pilas.colores.verde, relleno = True)
                    contador+1
                    
                #Lucas
                elif evento.x>89 and evento.x<178:
                    pizarra.rectangulo(PJLucas.x-22, PJLucas.y+22, 43, 43, color = pilas.colores.verde, relleno = True)
                    contador+1
                    
        else:
            
            if evento.y>-44 and evento.y<46:
                if evento.x>-179 and evento.x<-90:
                    pizarra.rectangulo(PJFacu.x-22, PJFacu.y+22, 43, 43, color = pilas.colores.azul, relleno = True)
                    
                    BtnSiguiente = pilas.interfaz.Boton("Fight!",0,-200)
                    def Fight():
                        pilas.escenas.CombatArena()
                    BtnSiguiente.conectar(Fight)
                    
                    contador+1
                elif evento.x>-46 and evento.x<43:
                    pizarra.rectangulo(PJRami.x-22, PJRami.y+22, 43, 43, color = pilas.colores.azul, relleno = True)
                    
                    BtnSiguiente = pilas.interfaz.Boton("Fight!",0,-200)
                    def Fight():
                        pilas.escenas.CombatArena()
                    BtnSiguiente.conectar(Fight)
                    
                    contador+1
                elif evento.x>89 and evento.x<178:
                    pizarra.rectangulo(PJNacho.x-22, PJNacho.y+22, 43, 43, color = pilas.colores.azul, relleno = True)
                    
                    BtnSiguiente = pilas.interfaz.Boton("Fight!",0,-200)
                    def Fight():
                        pilas.escenas.CombatArena()
                    BtnSiguiente.conectar(Fight)
                    
                    contador+1
                    
            elif evento.y>-156 and evento.y<-66:
                if evento.x>-179 and evento.x<-90:
                    pizarra.rectangulo(PJFede.x-22, PJFede.y+22, 43, 43, color = pilas.colores.azul, relleno = True)
                    
                    BtnSiguiente = pilas.interfaz.Boton("Fight!",0,-200)
                    def Fight():
                        pilas.escenas.CombatArena()
                    BtnSiguiente.conectar(Fight)
                    
                    contador+1
                elif evento.x>-46 and evento.x<43:
                    pizarra.rectangulo(PJStefan.x-22, PJStefan.y+22, 43, 43, color = pilas.colores.azul, relleno = True)
                    
                    BtnSiguiente = pilas.interfaz.Boton("Fight!",0,-200)
                    def Fight():
                        pilas.escenas.CombatArena()
                    BtnSiguiente.conectar(Fight)
                    
                    contador+1
                elif evento.x>89 and evento.x<178:
                    pizarra.rectangulo(PJLucas.x-22, PJLucas.y+22, 43, 43, color = pilas.colores.azul, relleno = True)
                    
                    BtnSiguiente = pilas.interfaz.Boton("Fight!",0,-200)
                    def Fight():
                        pilas.escenas.CombatArena()
                    BtnSiguiente.conectar(Fight)
                    
                    contador+1
        
        
        
        
#----------------------------------------Clase---------------------------------------
#---------------------------------------Player1--------------------------------------

class Player1(pilasengine.actores.Actor):

    def iniciar(self):
        self.x = -200
        self.y = -150
        self.escala = .7
        self.hacer_inmediatamente(ParadoP1)
        self.sombra = self.pilas.actores.Sombra()
        self.altura_del_salto = 0
        self.numBlocksP1 = 4
        self.YIniP1 = self.y
        
        #Colision de el cuerpo
        global ColiderBodyP1
        ColiderBodyP1 = pilas.actores.Actor()
        ColiderBodyP1.transparencia = 100
        ColiderBodyP1.figura_de_colision = pilas.fisica.Rectangulo(0, 0, 70, 130)
        
        #Colision del golpe
        global ColiderHitP1
        ColiderHitP1 = pilas.actores.Actor()
        ColiderHitP1.transparencia = 100
        ColiderHitP1.figura_de_colision = None
        
        #Vida y energia del jugador 1
        global VidaP1
        VidaP1 = pilas.actores.Energia(progreso=100, ancho=300, alto=25, x=-165, y=220, color_relleno=colores.verde)
        global EnergiaP2
        EnergiaP2 = pilas.actores.Energia(progreso=0, ancho=150, alto=25, x=240, y=190)  
        EnergiaP2.espejado = True
        
        
        teclasP1 = {
            pilas.simbolos.a: 'izquierda',
            pilas.simbolos.d: 'derecha',
            pilas.simbolos.w: 'arriba',
            pilas.simbolos.g: 'abajo',
            pilas.simbolos.f: 'boton',
        }
        
        global mi_controlP1
        mi_controlP1 = pilas.control.Control(teclasP1)
        self.control = mi_controlP1
    
    def set_enemigoP2(self, enemigoP2):
        global EnemyP2
        EnemyP2 = enemigoP2
                
    def actualizar(self):
        self.sombra.x = self.x
        self.sombra.z = self.z + 1
        self.sombra.rotacion = self.rotacion
        
        ColiderBodyP1.x = self.x - 5
        ColiderBodyP1.y = self.y + 80
        
        # Adapta el tamaño y la distancia a la sombra para simular
        # que la sombra está siempre 'pegada' al suelo del escenario.
        self.sombra.y = self.y + 20 - self.altura_del_salto
        self.sombra.escala = self.escala - self.altura_del_salto / 300.0
            
        def golpeadoP1():
            self.y = self.YIniP1
            if self.control.abajo:
                print (self.numBlocksP1)
                if self.numBlocksP1 == 0:
                    self.hacer_inmediatamente(AtackedP1)
                else:
                    self.numBlocksP1 -= 1
            else:
                self.hacer_inmediatamente(AtackedP1)
            
            
        pilas.colisiones.agregar(ColiderBodyP1, EnemyP2, golpeadoP1)

class ParadoP1(pilasengine.comportamientos.Comportamiento):

    def iniciar(self, receptor):
        
        self.receptor = receptor
        self.control = mi_controlP1

        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Imagenes/Fighters/AnimacionesFighters/Player1/P1Idle/FighterIdle10.png", 10, 1)
        self.receptor.centro = ("centro", "abajo")

    def actualizar(self):
        self.receptor.imagen.avanzar(10)
        
        # Si pulsa a los costados comienza a caminar.
        if self.control.derecha or self.control.izquierda:
            self.receptor.hacer_inmediatamente(CaminarP1)
            
        # Si pulsa hacia arriba salta.
        if self.control.arriba:
            self.receptor.hacer_inmediatamente(JumpP1)
            
         # Si pulsa el boton ataca.
        if self.control.boton:
            self.receptor.hacer_inmediatamente(AtackP1)
            
        # Si pulsa hacia abajo bloquea.
        if self.control.abajo:
            self.receptor.hacer_inmediatamente(BlockP1)

class CaminarP1(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP1

        self.moveL = self.pilas.imagenes.cargar_grilla("Imagenes/Fighters/AnimacionesFighters/Player1/P1Move/FighterLeft11.png", 11, 1)
        self.moveR = self.pilas.imagenes.cargar_grilla("Imagenes/Fighters/AnimacionesFighters/Player1/P1Move/FighterRight11.png", 11, 1)
        
    def actualizar(self):
        self.receptor.imagen.avanzar(10)
        
        # Si pulsa a los costados se puede mover.
        if self.control.derecha:
            self.receptor.imagen = self.moveR
            self.receptor.centro = ("centro", "abajo")
            self.receptor.x += 2
        elif self.control.izquierda:
            self.receptor.imagen = self.moveL
            self.receptor.centro = ("centro", "abajo")
            self.receptor.x -= 2
            
        # Si pulsa hacia arriba salta.
        if self.control.arriba:
            self.receptor.hacer_inmediatamente(JumpP1)
            
        # Si suelta las teclas regresa al estado inicial.
        if not self.control.derecha and not self.control.izquierda:
            self.receptor.hacer_inmediatamente(ParadoP1)
            
        # Si pulsa el boton ataca.
        if self.control.boton:
            self.receptor.hacer_inmediatamente(AtackP1)
            
        # Si pulsa hacia abajo bloquea.
        if self.control.abajo:
            self.receptor.hacer_inmediatamente(BlockP1)
            
class BlockP1(pilasengine.comportamientos.Comportamiento):
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP1
        
        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Imagenes/Fighters/AnimacionesFighters/Player1/P1Block/FighterBlocking5.png", 5, 1)
        self.receptor.centro = ("centro", "abajo")
          
    def actualizar(self):
        self.receptor.imagen.avanzar(10)
        
        if not self.control.abajo:
            self.receptor.hacer_inmediatamente(ParadoP1)
            
class AtackedP1(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP1
        
        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Imagenes/Fighters/AnimacionesFighters/Player1/P1Atacked/FighterAtacked11.png", 11, 1)
        self.receptor.centro = ("centro", "abajo")
        
        VidaP1.progreso -= 4
        EnergiaP2.progreso += 8
        
        def recuperado():
            if VidaP1.progreso<1:
                self.receptor.hacer_inmediatamente(MuerteP1)
            else:
                self.receptor.hacer_inmediatamente(ParadoP1)
            
        pilas.tareas.agregar(.2, recuperado)
        
    def actualizar(self):
        self.receptor.imagen.avanzar(15)

class AtackP1(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP1
        
        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Imagenes/Fighters/AnimacionesFighters/Player1/P1Atack/FighterAtack12.png", 12, 1)
        self.receptor.centro = ("centro", "abajo")
        
        
        ColiderHitP1.x = self.receptor.x + 50
        ColiderHitP1.y = self.receptor.y + 100
        ColiderHitP1.figura_de_colision = pilas.fisica.Circulo(radio = 10, sensor = True)
        
        def Timer():
            self.receptor.hacer_inmediatamente(ParadoP1)
            ColiderHitP1.figura_de_colision = None
        
        global TGolpeP1 
        TGolpeP1 = pilas.tareas.agregar(.5, Timer)
        
    def actualizar(self):
        self.receptor.imagen.avanzar(20)
        
         # Si pulsa hacia arriba salta.
        if self.control.arriba and not self.control.derecha and not self.control.izquierda:
            TGolpeP1.terminar()
            ColiderHitP1.figura_de_colision = None
            self.receptor.hacer_inmediatamente(JumpP1)
            
        # Si pulsa a los costados comienza a caminar.
        if self.control.derecha or self.control.izquierda and not self.control.arriba:
            TGolpeP1.terminar()
            ColiderHitP1.figura_de_colision = None
            self.receptor.hacer_inmediatamente(CaminarP1)
            
        # Si pulsa hacia abajo bloquea.
        if self.control.abajo:
            TGolpeP1.terminar()
            ColiderHitP1.figura_de_colision = None
            self.receptor.hacer_inmediatamente(BlockP1)
            
class JumpP1(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP1

        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Imagenes/Fighters/AnimacionesFighters/Player1/P1Jump/FighterJump10.png", 10, 1)
        self.receptor.centro = ("centro", "abajo")
        self.y_inicial = self.receptor.y
        self.vy = 15
        
    def actualizar(self):
        self.receptor.imagen.avanzar(10)
        self.receptor.y += self.vy
        self.vy -= 0.7

        distancia_al_suelo = self.receptor.y - self.y_inicial
        self.receptor.altura_del_salto = distancia_al_suelo

        # Cuando llega al suelo, regresa al estado inicial.
        if distancia_al_suelo < 0:
            self.receptor.y = self.y_inicial
            self.receptor.altura_del_salto = 0
            self.receptor.hacer_inmediatamente(ParadoP1)
            
        # Si pulsa a los costados se puede mover.
        if self.control.derecha:
            self.receptor.x += 4
        elif self.control.izquierda:
            self.receptor.x -= 4
            
            
class MuerteP1(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP1

        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Imagenes/Fighters/AnimacionesFighters/Player1/P1Muerte/FighterDead18.png", 18, 1)
        self.receptor.centro = ("centro", "abajo")
            
        def terminarCaidaP1():
            self.receptor.hacer_inmediatamente(GameOverP1)
        
        def caidaP1():
            self.receptor.x = [self.receptor.x-150], 1
            self.receptor.y = [self.receptor.y+10, self.receptor.y-70], .25
            pilas.tareas.agregar(1.6, terminarCaidaP1)
        
        pilas.tareas.agregar(.1, caidaP1)
        
    def actualizar(self):
        self.receptor.imagen.avanzar(12)
        
class GameOverP1(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor

        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Imagenes/Fighters/AnimacionesFighters/Player1/P1Muerte/FighterDead18.png", 18, 1)
        self.receptor.imagen.definir_cuadro(17)
        self.receptor.centro = ("centro", "abajo")
        
        Cortina =pilas.actores.Actor()
        Cortina.imagen = "Imagenes/cortina.png"
        Cortina.z = -100
        Cortina.escala = 3
        Cortina.transparencia = 100
        Cortina.transparencia = [30]
        
        GameOver = pilas.actores.Actor()
        GameOver.imagen = "Imagenes/GameOver.png"
        GameOver.transparencia = 100
        GameOver.transparencia = [0]
        GameOver.z = -101
        
        WinerP1 = pilas.actores.Actor()
        WinerP1.imagen = "Imagenes/P2Win.png"
        WinerP1.escala = .4
        WinerP1.y -= 70
        WinerP1.z = -101
        
        volver = pilas.actores.Texto("Pulsa escape para volver al Menu Principal")
        volver.escala=.5
        volver.x=-190
        volver.y=-220
        volver.color= "grisclaro"
        
        pilas.eventos.pulsa_tecla_escape.conectar(self.Volver)
        
    def Volver(self, evento):
        pilas.escenas.MenuInicial()
           
                                 
#----------------------------------------Clase---------------------------------------
#---------------------------------------Player2--------------------------------------

class Player2(pilasengine.actores.Actor):

    def iniciar(self):
        self.x = 200
        self.y = -150
        self.escala = .7
        self.espejado = True
        self.hacer_inmediatamente(ParadoP2)
        self.sombra = self.pilas.actores.Sombra()
        self.altura_del_salto = 0
        self.YIniP2 = self.y
        
        #Colision de el cuerpo
        global ColiderBodyP2
        ColiderBodyP2 = pilas.actores.Actor()
        ColiderBodyP2.transparencia = 100
        ColiderBodyP2.figura_de_colision = pilas.fisica.Rectangulo(0, 0, 70, 130)
        
        #Colision del golpe
        global ColiderHitP2
        ColiderHitP2 = pilas.actores.Actor()
        ColiderHitP2.transparencia = 100
        ColiderHitP2.figura_de_colision = None
        
        #Vida y energia del Jugador 2
        global VidaP2
        VidaP2 = pilas.actores.Energia(progreso=100, ancho=300, alto=25, x=165, y=220, color_relleno=colores.verde)
        VidaP2.espejado = True
        global EnergiaP1
        EnergiaP1 = pilas.actores.Energia(progreso=0, ancho=150, alto=25, x=-240, y=190)
        
        teclasP2 = {
            pilas.simbolos.IZQUIERDA: 'izquierda',
            pilas.simbolos.DERECHA: 'derecha',
            pilas.simbolos.ARRIBA: 'arriba',
            pilas.simbolos.k: 'abajo',
            pilas.simbolos.j: 'boton',
        }
        
        global mi_controlP2
        mi_controlP2 = pilas.control.Control(teclasP2)
        self.control = mi_controlP2
    
    def set_enemigoP1(self, enemigoP1):
        global EnemyP1
        EnemyP1 = enemigoP1
            
    def actualizar(self):
        self.sombra.x = self.x
        self.sombra.z = self.z + 1
        self.sombra.rotacion = self.rotacion
        
        ColiderBodyP2.x = self.x - 5
        ColiderBodyP2.y = self.y + 80
        
        # Adapta el tamaño y la distancia a la sombra para simular
        # que la sombra está siempre 'pegada' al suelo del escenario.
        self.sombra.y = self.y + 20 - self.altura_del_salto
        self.sombra.escala = self.escala - self.altura_del_salto / 300.0
            
        def golpeadoP2():
            self.y = self.YIniP2
            if not self.control.abajo:
                self.hacer_inmediatamente(AtackedP2)
            
        pilas.colisiones.agregar(ColiderBodyP2, EnemyP1, golpeadoP2)

class ParadoP2(pilasengine.comportamientos.Comportamiento):

    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP2

        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Imagenes/Fighters/AnimacionesFighters/Player2/P2Idle/FighterIdle8.png", 8, 1)
        self.receptor.centro = ("centro", "abajo")

    def actualizar(self):
        self.receptor.imagen.avanzar(10)
        
        # Si pulsa a los costados comienza a caminar.
        if self.control.derecha or self.control.izquierda:
            self.receptor.hacer_inmediatamente(CaminarP2)
            
        # Si pulsa hacia arriba salta.
        if self.control.arriba:
            self.receptor.hacer_inmediatamente(JumpP2)
            
         # Si pulsa el boton ataca.
        if self.control.boton:
            self.receptor.hacer_inmediatamente(AtackP2)
        # Si pulsa hacia abajo blockea    
        if self.control.abajo:
            self.receptor.hacer_inmediatamente(BlockP2)

class CaminarP2(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP2

        self.moveR = self.pilas.imagenes.cargar_grilla("Imagenes/Fighters/AnimacionesFighters/Player2/P2Move/FighterRight8.png", 8, 1)
        self.moveL = self.pilas.imagenes.cargar_grilla("Imagenes/Fighters/AnimacionesFighters/Player2/P2Move/FighterLeft8.png", 8, 1)
        
    def actualizar(self):
        self.receptor.imagen.avanzar(10)
        
        # Si pulsa a los costados se puede mover.
        if self.control.derecha:
            self.receptor.imagen = self.moveR
            self.receptor.centro = ("centro", "abajo")
            self.receptor.x += 2
        elif self.control.izquierda:
            self.receptor.imagen = self.moveL
            self.receptor.centro = ("centro", "abajo")
            self.receptor.x -= 2
            
        # Si pulsa hacia arriba salta.
        if self.control.arriba:
            self.receptor.hacer_inmediatamente(JumpP2)
            
        # Si suelta las teclas regresa al estado inicial.
        if not self.control.derecha and not self.control.izquierda:
            self.receptor.hacer_inmediatamente(ParadoP2)
            
        # Si pulsa el boton ataca.
        if self.control.boton:
            self.receptor.hacer_inmediatamente(AtackP2)
            
        # Si pulsa hacia abajo blockea    
        if self.control.abajo:
            self.receptor.hacer_inmediatamente(BlockP2)
            
class BlockP2(pilasengine.comportamientos.Comportamiento):
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP2
        
        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Imagenes/Fighters/AnimacionesFighters/Player2/P2Block/FighterBlock6.png", 6, 1)
        self.receptor.centro = ("centro", "abajo")
        
        self.receptor.y -= 20
        
    def actualizar(self):
        self.receptor.imagen.avanzar(10)
        
        if not self.control.abajo:
            self.receptor.y += 20
            self.receptor.hacer_inmediatamente(ParadoP2)
            
class AtackedP2(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP2
        
        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Imagenes/Fighters/AnimacionesFighters/Player2/P2Atacked/FighterAtacked10.png", 10, 1)
        self.receptor.centro = ("centro", "abajo")
     
        VidaP2.progreso -= 4
        EnergiaP1.progreso += 8
        
        def recuperadoP2():
            if VidaP2.progreso<1:
                self.receptor.hacer_inmediatamente(MuerteP2)
            else:
                self.receptor.hacer_inmediatamente(ParadoP2)
            
        pilas.tareas.agregar(.2, recuperadoP2)
        
    def actualizar(self):
        self.receptor.imagen.avanzar(18)

class AtackP2(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP2
        
        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Imagenes/Fighters/AnimacionesFighters/Player2/P2Atack/FighterAtack8.png", 8, 1)
        self.receptor.centro = ("centro", "abajo")
        
        ColiderHitP2.x = self.receptor.x - 50
        ColiderHitP2.y = self.receptor.y + 100
        ColiderHitP2.figura_de_colision = pilas.fisica.Circulo(radio = 10, sensor = True)
        
        def Timer():
            self.receptor.hacer_inmediatamente(ParadoP2)
            ColiderHitP2.figura_de_colision = None
        
        global TGolpeP2 
        TGolpeP2 = pilas.tareas.agregar(.5, Timer)
        
    def actualizar(self):
        self.receptor.imagen.avanzar(15)
        
         # Si pulsa hacia arriba salta.
        if self.control.arriba and not self.control.derecha and not self.control.izquierda:
            TGolpeP2.terminar()
            ColiderHitP2.figura_de_colision = None
            self.receptor.hacer_inmediatamente(JumpP2)
            
        # Si pulsa a los costados comienza a caminar.
        if self.control.derecha or self.control.izquierda and not self.control.arriba:
            TGolpeP2.terminar()
            ColiderHitP2.figura_de_colision = None
            self.receptor.hacer_inmediatamente(CaminarP2)
            
        # Si pulsa hacia abajo bloquea.
        if self.control.abajo:
            TGolpeP2.terminar()
            ColiderHitP2.figura_de_colision = None
            self.receptor.hacer_inmediatamente(BlockP2)
            
class JumpP2(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP2

        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Imagenes/Fighters/AnimacionesFighters/Player2/P2Jump/FighterJump8.png", 8, 1)
        self.receptor.centro = ("centro", "abajo")
        self.y_inicial = self.receptor.y
        self.vy = 15
        
    def actualizar(self):
        self.receptor.imagen.avanzar(10)
        self.receptor.y += self.vy
        self.vy -= 0.7

        distancia_al_suelo = self.receptor.y - self.y_inicial
        self.receptor.altura_del_salto = distancia_al_suelo

        # Cuando llega al suelo, regresa al estado inicial.
        if distancia_al_suelo < 0:
            self.receptor.y = self.y_inicial
            self.receptor.altura_del_salto = 0
            self.receptor.hacer_inmediatamente(ParadoP2)
            
        # Si pulsa a los costados se puede mover.
        if self.control.derecha:
            self.receptor.x += 4
        elif self.control.izquierda:
            self.receptor.x -= 4
            
class MuerteP2(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor
        self.control = mi_controlP2

        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Imagenes/Fighters/AnimacionesFighters/Player2/P2Muerte/FighterDead11.png", 11, 1)
        self.receptor.centro = ("centro", "abajo")
            
        def terminarCaidaP2():
            self.receptor.hacer_inmediatamente(GameOverP2)
        
        def caidaP2():
            self.receptor.x = [self.receptor.x+150], 1
            self.receptor.y = [self.receptor.y+10, self.receptor.y-70], .25
            pilas.tareas.agregar(2, terminarCaidaP2)
        
        pilas.tareas.agregar(.1, caidaP2)
        
    def actualizar(self):
        self.receptor.imagen.avanzar(5)
        
class GameOverP2(pilasengine.comportamientos.Comportamiento):
    
    def iniciar(self, receptor):
        self.receptor = receptor

        self.receptor.imagen = self.pilas.imagenes.cargar_grilla("Imagenes/Fighters/AnimacionesFighters/Player2/P2Muerte/FighterDead11.png", 11, 1)
        self.receptor.imagen.definir_cuadro(10)
        self.receptor.centro = ("centro", "abajo")
        
        Cortina =pilas.actores.Actor()
        Cortina.imagen = "Imagenes/cortina.png"
        Cortina.z = -100
        Cortina.escala = 3
        Cortina.transparencia = 100
        Cortina.transparencia = [30]
        
        GameOver = pilas.actores.Actor()
        GameOver.imagen = "Imagenes/GameOver.png"
        GameOver.transparencia = 100
        GameOver.transparencia = [0]
        GameOver.z = -101
        
        WinerP1 = pilas.actores.Actor()
        WinerP1.imagen = "Imagenes/P1Win.png"
        WinerP1.escala = .4
        WinerP1.y -= 70
        WinerP1.z = -101
        
        volver = pilas.actores.Texto("Pulsa escape para volver al Menu Principal")
        volver.escala=.5
        volver.x=-190
        volver.y=-220
        volver.color= "grisclaro"
        
        pilas.eventos.pulsa_tecla_escape.conectar(self.Volver)
        
    def Volver(self, evento):
        pilas.escenas.MenuInicial()
        
                                                                         
                                                                                                                                                
#----------------------------------------Clase---------------------------------------
#--------------------------------Arena de combate-------------------------------

class CombatArena(pilasengine.escenas.Escena):
    def iniciar(self):
        
#-----------------------------Preparando el fondo---------------------------------------
    
        cFondo = pilas.imagenes.cargar_grilla('Imagenes\CombatArena3.png', 4)
        fondo = pilas.actores.Animacion(cFondo, ciclica=True, velocidad= 10)
        pilas.camara.escala=1.35
        fondo.z=10

#-----------------------------Iniciando a los Jugadores---------------------------------------
        
        P2 = pilas.actores.Player2()
        P1 = pilas.actores.Player1()
        P2.set_enemigoP1(enemigoP1 = ColiderHitP1)
        P1.set_enemigoP2(enemigoP2 = ColiderHitP2)
        
#-----------------------------------------Vinculacion de elementos-------------------------

pilas.actores.vincular(Player2)            
pilas.actores.vincular(Player1)

pilas.comportamientos.vincular(ParadoP1)
pilas.comportamientos.vincular(CaminarP1)
pilas.comportamientos.vincular(JumpP1)
pilas.comportamientos.vincular(AtackedP1)
pilas.comportamientos.vincular(AtackP1)
pilas.comportamientos.vincular(BlockP1)
pilas.comportamientos.vincular(MuerteP1)
pilas.comportamientos.vincular(GameOverP1)

pilas.comportamientos.vincular(ParadoP2)
pilas.comportamientos.vincular(CaminarP2)
pilas.comportamientos.vincular(JumpP2)
pilas.comportamientos.vincular(AtackedP2)
pilas.comportamientos.vincular(AtackP2)
pilas.comportamientos.vincular(BlockP2)
pilas.comportamientos.vincular(MuerteP2)
pilas.comportamientos.vincular(GameOverP2)

pilas.escenas.vincular(MenuInicial)
pilas.escenas.vincular(MenuPersonajes)
pilas.escenas.vincular(CombatArena)
pilas.escenas.vincular(MenInstrucciones)
pilas.escenas.vincular(Config)
pilas.escenas.vincular(Audio)
pilas.escenas.vincular(ControlesP1)
pilas.escenas.vincular(ControlesP2)

pilas.escenas.CombatArena()


pilas.ejecutar()