# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()

class Player1(pilasengine.actores.Actor):

    def iniciar(self, enemigoP2):
        global EnemyP2
        EnemyP2 = enemigoP2
        self.x = -200
        self.y = -150
        self.escala = .7
        self.hacer_inmediatamente(ParadoP1)
        self.sombra = self.pilas.actores.Sombra()
        self.altura_del_salto = 0
        
        #Colision de el cuerpo
        global ColiderBodyP1
        ColiderBodyP1 = pilas.actores.Actor()
        ColiderBodyP1.transparencia = 100
        ColiderBodyP1.figura_de_colision = pilas.fisica.Rectangulo(0, 0, 100, 130)
        
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
        
    def actualizar(self):
        self.sombra.x = self.x
        self.sombra.z = self.z + 1
        self.sombra.rotacion = self.rotacion
        
        ColiderBodyP1.x = self.x
        ColiderBodyP1.y = self.y + 80
        
        # Adapta el tamaño y la distancia a la sombra para simular
        # que la sombra está siempre 'pegada' al suelo del escenario.
        self.sombra.y = self.y + 20 - self.altura_del_salto
        self.sombra.escala = self.escala - self.altura_del_salto / 300.0
            
        def golpeadoP1():
            if not self.control.abajo:
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
        
        VidaP1.progreso -= 2
        EnergiaP2.progreso += 8
        
        def recuperado():
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
            self.receptor.hacer_inmediatamente(Block)
            
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
            
pilas.actores.vincular(Player1)

pilas.comportamientos.vincular(ParadoP1)
pilas.comportamientos.vincular(CaminarP1)
pilas.comportamientos.vincular(JumpP1)
pilas.comportamientos.vincular(AtackedP1)
pilas.comportamientos.vincular(AtackP1)
pilas.comportamientos.vincular(BlockP1)

P1 = pilas.actores.Player1()

pilas.ejecutar()