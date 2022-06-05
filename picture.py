from colors import *

class Picture:
  def __init__(self, img):
    self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    return Picture(None)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    imagen = self.img
    nuevaImagen = []
    for i in imagen: #Recorre la cantidad de elementos de la lista
      elemento = ""
      for j in range(57, -1, -1): #58 es la cantidad de caracteres que tiene cada elemento de la lista, se pone 57 porque esta vendría a ser la última posición, -1 para que recorra hasta el primer elemento, y el otro -1 para que vaya disminuyendo. 
        #Este for recorrerá todos los caracteres de atrás hacia adelante.
        elemento += i[j] #Se va agregando de caracter en caracter
      nuevaImagen.append(elemento) #Reemplaza el elemento, pero volteado 
    return Picture(nuevaImagen)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    return Picture(None)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    return Picture(None)

  def up(self, p):
    return Picture(None)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

