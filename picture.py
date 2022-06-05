from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

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
    result = []
    for x in self.img:
      line = ''
      for y in x:
        line = line + self._invColor(y)
      result.append(line)
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
