import pilasengine

#Clase personaje

class Rami(pilasengine.actores.Actor):
    
    #Se inicia el personaje
    def iniciar(self):
        self.x = 0
        self.y = 0
        
        attack = pilas.imagenes.cargar_grilla("RamiAttack.png", 10)
        idle = pilas.imagenes.cargar_grilla("RamiIdle.png", 10)
        jump = pilas.imagenes.cargar_grilla("RamiJump.png", 10)
        damage = pilas.imagenes.cargar_grilla("RamiDamage.png", 10)
        dead = pilas.imagenes.cargar_grilla("RamiDead.png", 10)
        move = pilas.imagenes.cargar_grilla("RamiMove.png", 10)
        block = pilas.imagenes.cargar_grilla("RamiBlock.png", 10)
        
        pilas.actores.Animacion(idle, ciclica=True, velocidad=10 )
    
    #Se chequea los eventos de movimiento y ataque        
    def actualizar(self, Jugador):
        
        self.jugador = Jugador
        
        #Si el jugador es player 1 se mueve con las flechas y ataca con L
        #Si el jugador es player 2 se mueve con w, a, d y ataca con G
        if Jugador = 'player1':
            
            #Izquierda
            if self.pilas.control.izquierdo:
                self.x -= -10
                self.espejado = True
                pilas.actores.Animacion(move, ciclica=True, velocidad=10)
            #Derecha    
            if self.pilas.control.derecho:
                self.x += 10
                self.espejado = False
                pilas.actores.Animacion(move, ciclica=True, velocidad=10)
            #Saltar    
            if self.pilas.control.arriba:
                self.y += 10
                pilas.actores.Animacion(jump, ciclica=True, velocidad=10)
            #Atacar
            if self.pilas.simbolo.l:
                pilas.actores.Animacion(attack, ciclica=True, velocidad=10)
            #Bloquear    
            if self.pilas.control.abajo:
                pilas.actores.Animacion(block, ciclica=True, velocidad=10)
                
        else:
            
            #Izquierda
            if self.pilas.simbolo.a:
                self.x -= -10
                self.espejado = True
                pilas.actores.Animacion(move, ciclica=True, velocidad=10)
                    
            #Derecha    
            if self.pilas.simbolo.d:
                self.x += 10
                self.espejado = False
                pilas.actores.Animacion(move, ciclica=True, velocidad=10)
            
            #Saltar
            if self.pilas.simbolo.w:
                self.y += 10
                pilas.actores.Animacion(jump, ciclica=True, velocidad=10)
                    
            #Atacar    
            if self.pilas.simbolo.g:
                pilas.actores.Animacion(attack, ciclica=True, velocidad=10)
                
           #Bloquear    
            if self.pilas.simbolo.s:
                pilas.actores.Animacion(block, ciclica=True, velocidad=10)