from interpreter import draw
from chessPictures import *

piece = [rock, knight, bishop, queen, king, bishop, knight, rock]
piece2 = [square, pawn]

output = None
for i in range(8):
    fila=None

    if i < 2:
        for j in range(8):
            black = piece2[0]
            if (i == 0 and j % 2 == 0) or (i == 1 and j % 2 != 0) :                
                black = piece2[0].negative()

            #superponer ficha
            if i == 0:
                black=black.under(piece[j])
            else:
                black=black.under(piece2[1])

            if j > 0:
                fila=fila.join(black)
            else :
                fila=black

    if i > 1 and i < 6:
        for j in range(8):
            black = piece2[0]
            if (((i == 2) or(i == 4)) and j % 2 == 0) or ((i == 3 or i == 5)and j % 2 != 0) :                
                black = piece2[0].negative()
            if j > 0:
                fila=fila.join(black)
            else :
                fila=black


    
    if i > 5:
        for j in range(8):
            black = piece2[0]
            if (i == 6 and j % 2 == 0) or (i == 7 and j % 2 != 0) :                
                black = piece2[0].negative()

            #superponer ficha
            if i == 7:
                black=black.under(piece[j].negative())
            else:
                black=black.under(piece2[1].negative())

            if j > 0:
                fila=fila.join(black)
            else :
                fila=black
    if i<8:
        if i > 0:
            output=fila.up(output)
        else:
            output=fila    

draw(output)   