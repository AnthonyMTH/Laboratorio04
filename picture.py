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
    return Picture(None)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    return Picture(None)

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