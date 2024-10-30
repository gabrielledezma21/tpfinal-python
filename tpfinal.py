#validacion general para el tipo de dato
def validarTipo(variable, nombre, tipo):
    if isinstance(variable, tipo):
        return True
    else:
        raise Exception(f"La variable {nombre} debe ser de tipo {tipo}.")

#metodo para validar si un numero se encuentra entre valores    
def between(numero, minimo, maximo) ->bool:
    return minimo <= numero <= maximo

#Validaciones para la clase tiempo
def validarHoras(horas):
    if (validarTipo(horas, "horas", int) and horas > 0 ) or horas == 0:
        return horas
    else:
        raise Exception("Número de horas incorrecto.")

def validarMinutos(minutos):
    if validarTipo(minutos, "minutos", int) and between(minutos,0,59):
        return minutos
    else:
        raise Exception("Número de minutos incorrecto.")

def validarSegundos(segundos):
    if validarTipo(segundos, "segundos", int) and between(segundos,0,59):
        return segundos
    else:
        raise Exception("Número de segundos incorrecto.")

#Cree una clase tiempo para una mejor forma de tratar la duracion de las canciones
class Tiempo:
    def __init__(self, horas:int, minutos:int, segundos:int):
        self.horas = validarHoras(horas)
        self.minutos = validarMinutos(minutos)
        self.segundos = validarSegundos(segundos)

    def __str__(self):
        return f"{self.horas}:{self.minutos}:{self.segundos}"

    def getHoras(self):
        return self.horas

    def getMinutos(self):
        return self.minutos

    def getSegundos(self):
        return self.segundos

# metodo para convertir tiempo de formato HH:mm:ss a segundos
def tiempoASegundos(tiempo:Tiempo) ->int:
    h = tiempo.getHoras() * 3600
    m = tiempo.getMinutos() * 60
    s = tiempo.getSegundos()
    return (h + m + s)

# metodo para convertir tiempo de segundos a formato HH:mm:ss
def tiemposDesdeSegundos(segundos:int)->Tiempo:
    h = segundos // 3600
    segundos -= h * 3600
    m = segundos // 60
    segundos -= m * 60
    s = segundos
    return Tiempo(h,m,s)

# metodo que compara dos tiempos y devuelve el mayor
def mayorDuracion(tiempo1:Tiempo,tiempo2:Tiempo)->Tiempo:
    return tiempo1 if tiempoASegundos(tiempo1) > tiempoASegundos(tiempo2) else tiempo2

#Validaciones para la clase Cancion
def validarNombre(nombre):
    if validarTipo(nombre, "nombre", str) and len(nombre) > 0:
        return nombre.capitalize()
    else:
        raise Exception("El nombre de la canción no puede estar vacío.")
    
def validarArtista(artista):
    if validarTipo(artista, "artista", str) and len(artista) > 0:
        return artista.capitalize()
    else:
        raise Exception("El nombre del artista no puede estar vacío.")
    
def validarDuracion(duracion):
    if validarTipo(duracion, "duración", Tiempo) and tiempoASegundos(duracion) > 0:
        return duracion
    else:
        raise Exception("La duración de la canción debe ser un número entero positivo.")
    
def validarGeneroMusical(generoMusical):
    generos = ["Rock","Jazz","Blues","Funk","Reggae","Rap"]
    if validarTipo(generoMusical, "género musical", str) and (generoMusical.capitalize() in generos):
        return generoMusical.capitalize()
    else:
        raise Exception("El género musical debe ser Rock, Jazz, Blues, Funk, Reggae o Rap")
    
def validarAnio(anio):
    if validarTipo(anio, "año", int) and between(anio,1900,2024):
        return anio
    else:
        raise Exception("El año debe ser mayor a 1900.")
    
def validarCantLikes(cantLikes):
    if validarTipo(cantLikes, "cantidad de likes", int) and cantLikes >= 0:
        return cantLikes
    else:
        raise Exception("La cantidad de likes debe ser mayor o igual a cero.")

class Cancion():
    def __init__(self, nombre:str, artista:str, duracion:Tiempo, generoMusical:str, anio:int, cantLikes:int):
        self.nombre = validarNombre(nombre)
        self.artista = validarArtista(artista)
        self.duracion = validarDuracion(duracion)
        self.generoMusical = validarGeneroMusical(generoMusical)
        self.anio = validarAnio(anio)
        self.cantLikes = validarCantLikes(cantLikes)

    def getNombre(self):
        return self.nombre
    
    def getArtista(self):
        return self.artista
    
    def getDuracion(self):
        return self.duracion
    
    def getGeneroMusical(self):
        return self.generoMusical
    
    def getAnio(self):
        return self.anio
    
    def getCantLikes(self):
        return self.cantLikes

    def __str__(self):
        return f"{self.nombre()} - {self.artista()} ({self.duracion()})"
    
    def mayorDuracion(cancion1, cancion2):
        return cancion1 if tiempoASegundos( cancion1.getDuracion() ) > tiempoASegundos( cancion2.getDuracion() ) else cancion2
    
    def agregaLikes(self, cantidad):
        self.cantLikes += cantidad

    def validarMismoArtista(cancion1, cancion2):
        if cancion1.getArtista() == cancion2.getArtista():
            return True
        else:
            raise Exception("Las canciones NO son del mismo artista.")

    def validarMismoGeneroMusical(cancion1, cancion2):
        if cancion1.getGeneroMusical() == cancion2.getGeneroMusical():
            return True
        else:
            raise Exception("Las canciones NO son del mismo género musical.")

    def masVotada(self,cancion1,cancion2):
        if self.validarMismoArtista(cancion1,cancion2) and self.validarMismoGeneroMusical(cancion1,cancion2):
            return cancion1 if cancion1.getCantLikes() > cancion2.getCantLikes() else cancion2
        else:
            raise Exception("No se pudieron comparar las canciones.")



#Número narcisista o de Armstrong

def esNarcisista(numero:int)->bool:
    aux = str(numero)                            #guardo como string el numero recibido
    suma=0                                       #en esta variable se guardara la sumatoria de los digitos elevados a la cantidad de digitos
    for digito in range(len(aux)):               #genero el bucle para pasar por cada digito del numero
        suma += int(aux[digito]) ** len(aux)     #cada digito del numero es elevado a la cantidad de digitos y sumado al acumulado en la sumatoria
    return suma == numero                        #realizo la verificacion si la sumatoria obtenida es igual al numero recibido

