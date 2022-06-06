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
    selfReversed = []
    index = len(self.img) - 1
    while(index >= 0):
          selfReversed.append(self.img[index])
          index = index - 1
    return Picture(selfReversed)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    imagen = self.img
    nuevaImagen = []
    for i in imagen: #Recorre la cantidad de elementos de la lista
      elemento = ""
      for j in range(57, -1, -1): #58 es la cantidad de caracteres que tiene cada elemento de la lista, se pone 57 porque esta vendría a ser la última posición, -1 para que recorra hasta el primer elemento, y el otro -1 para que vaya disminuyendo. 
        #Este for recorrerá todos los caracteres de atrás hacia adelante.
        elemento += i[j] #Se va agregando de caracter en caracter
      nuevaImagen.append(elemento) #Se agrega el elemento
    return Picture(nuevaImagen)

  def negative(self):
    result = []
    for x in self.img:
      line = ''
      for y in x:
        line = line + self._invColor(y)
      result.append(line)
    return Picture(result)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    return Picture(None)

  def up(self, p):
    newIMG = [] 
    for line in p.img: 
      newIMG.append(line) 
    for line in self.img:
      newIMG.append(line)      
    return Picture(newIMG)
  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """

    newImg=[]

    ficha=p.img
    fondo=self.img
    if(ficha[0][0]!=" "):
        aux=fondo
        fondo=ficha
        ficha=aux

    for i in range(len(fondo)):
        line=fondo[i]
        newLine=""
        for j in range(len(line)):
            if (ficha[i][j]==" "):
                newLine=newLine+fondo[i][j]
            else:
                newLine=newLine+ficha[i][j]
        newImg.append(newLine)

    return Picture(newImg)


  
  def horizontalRepeat(self, n):
    result = []
    for i in self.img:
      line = ''
      for j in range(n):
        line = line + i
      result.append(line)
    return Picture(result)

  def verticalRepeat(self, n):
    result = []
    for i in range(n):
      for j in self.img:
        result.append(j)
    return Picture(result)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    result = []
    for i in range(len(self.img)):
      line = ''
      for j in range(len(self.img[i])):
        try:
          line = line + self.img[len(self.img) - j][i]
        except:
          line = line + ''
      result.append(line)
    return Picture(result)
