<div align="center">
<table>
    <theader>
        <tr>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:50%; height:auto"/></td>
            <th>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </th>
            <td><img src="https://github.com/rescobedoq/pw2/blob/main/abet.png?raw=true" alt="ABET" style="width:50%; height:auto"/></td>
        </tr>
    </theader>
    <tbody>
        <tr><td colspan="3"><span style="font-weight:bold;">Formato</span>: Guía de Práctica de Laboratorio / Talleres / Centros de Simulación</td></tr>
        <tr><td><span style="font-weight:bold;">Aprobación</span>:  2022/03/01</td><td><span style="font-weight:bold;">Código</span>: GUIA-PRLD-001</td><td><span style="font-weight:bold;">Página</span>: 1</td></tr>
    </tbody>
</table>
</div>

<div>
<span style="font-weight:bold;">INFORME DE LABORATORIO</span><br />

<table>
<theader>
<tr><th colspan="6">INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
<tr><td>ASIGNATURA:</td><td colspan="5">Programación Web 2</td></tr>
<tr><td>TÍTULO DE LA PRÁCTICA:</td><td colspan="5">Python</td></tr>
<tr>
<td>NÚMERO DE PRÁCTICA:</td><td>04</td><td>AÑO LECTIVO:</td><td>2022 A</td><td>NRO. SEMESTRE:</td><td>III</td>
</tr>
<tr>
<td>FECHA DE PRESENTACIÓN:</td><td>5/06/2022</td><td>HORA DE PRESENTACIÓN:</td><td colspan="3"></td>
</tr>
<tr><td colspan="3">INTEGRANTE(s):
<ul>
<li>Chaisa/Fernández, Anthony Leonel - achaisa@unsa.edu.pe</li>
<li>Moroccoire/Pacompia, Anthony Marcos - amoroccoire@unsa.edu.pe</li>
<li>Diaz/Portilla, Carlo Rodrigo - cdiazpor@unsa.edu.pe</li>
<li>Ticona/Hareth, Anthony Joaquín - aticonaha@unsa.edu.pe</li>
<li>Almonte/Cuba, Axel Frank - aalmontecu@unsa.edu.pe</li>
</ul>
</td>
<td>NOTA:</td><td colspan="2"></td>
</<tr>
<tr><td colspan="6">DOCENTE(s):
<ul>
<li>Richart Smith Escobedo Quispe - rescobedoq@unsa.edu.pe</li>
</ul>
</td>
</<tr>
</tbody>
</table>

<!-- Reportes -->
## SOLUCIÓN Y RESULTADOS

---

I. SOLUCIÓN DE EJERCICIOS/PROBLEMAS <br>
* Organización del repositorio:
    ```sh
	   └───Laboratorio04
        ├───.gitignore
	    ├───README.md
        ├───chessPictures.py
        ├───colors.py
	    ├───ejercicio2g.py
	    ├───interpreter.py
	    ├───picture.py
	    └───pieces.py
    ```
* Funciones de la clase Picture:  

    * Función verticalMirror:

		Función encargada de mostrar el espejo vertical de la imagen. Implementando un bucle de tipo <code>while</code> que recorrerá desde atras hacia adelante los elementos de la lista que forma la imagen, almacenando cada caracter en una nueva lista.

    * Función horizontalMirror:
	
      Función encargada de mostrar el espejo horizontal de una imagen. Esto se consigue gracias a un bucle <code>for</code> que recorrerá en todos los elementos de la lista que forma a la imagen, de atrás hacia adelante, almacenando cada caracter en una nueva lista.

    * Función negative:

      En la función <code>negative</code> vamos a utilizar la función <code>\_invColor</code> la cual es una función de propósito interno y recibe un caracter y devuelve otro caracter que se entiende como su color inverso. Luego iteramos sobre toda la imagen invirtiendo su color.

    * Función join:

      Funcion que se encarga de colocar una figura a la derecha de otra, con la funcion <code>zip()</code> se consigue emparejar dos elementos de dos vectores, conveniente porque todas las figuras tienen las mismas dimensiones; despues, con dos iteradores se recorre la lista devuelta y se concatenan para formar un nuevo vector que junta las dos figuras como indica el ejercicio.

    * Función up:
	La funcion <code>up</code> recibe un <code>Picture</code> que lo va a posicioner encima de la figura actual por lo que se crea un arreglo el cual almcena el objeto recibido con un <code>for</code> y seguidamente se almacne el siguiente <code>Picture</code> con un  segundo <code>for</code>.

    * Función under:
	La funcion <code>under</code> recibe un <code>Picture</code> que lo va a posicioner sobre de la figura actual por lo que se crea un arreglo el cual almcena el objeto que se va a generar con un <code>if</code> que verifica que sea una figura y un <code>for</code> que va a recorre el fondo por <code>longitud</code> si el caracter es un <code>espacio</code> se agrega fondo y si <code>no es</code> se cambia el fondo por la figura 
    * Función horizontalRepeat:

      Para esta función se recibe un entero <code>n</code> el cual nos va a indicar el número de veces que vamos a repetir horizontalmente la imagen. Con ayuda de un ciclo <code>for</code> vamos a crear la imagen y repetirla horizontalmente.

    * Función verticalRepeat:

      En esta función recibimos un entero <code>n</code> y con la función <code>append</code> vamos a repetirlo verticalmente.

    * Función rotate:

      La función <code>rotate</code> se va aplicar a un objeto <code>Picture</code> con el fin de rotarlo 90° sentido horario, para resolver está función se hizon un análisis previo para saber cómo es que las posiciones debían rotar.

* Ejercicios Propuestos:
	
	Para visualizar los ejercicios, se debe ejecutar los siguientes comandos y luego copiar el comando del ejercicio que se desea visualizar..
	
     ```sh
	❯ python
	Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
	Type "help", "copyright", "credits" or "license" for more information.
	>>> from chessPictures import *
	>>> from interpreter import draw
    ```

    * Ejercicio A:
	
		<code>draw(((knight.negative()).join(knight)).up(knight.join(knight.negative())))</code>

    * Ejercicio B:
	
		<code>draw(((((knight.negative()).horizontalMirror()).join(knight.horizontalMirror()))).up(knight.join(knight.negative())))</code>
	

    * Ejercicio C:
	
		<code>draw(queen.horizontalRepeat(4))</code>

    * Ejercicio D:
	
		<code>draw(square.join(square.negative()).horizontalRepeat(4))</code>

    * Ejercicio E:
	
		<code>draw((square.negative().join(square)).horizontalRepeat(4))</code>

    * Ejercicio F:
	
		<code>draw((((square.negative().up(square)).join(square.up(square.negative()))).horizontalRepeat(4)).verticalRepeat(2))</code>

    * Ejercicio G:
	
	Para visualizar este ejercicio se debe ejecutar el archivo <code>ejercicio2g.py</code>.
---

II. SOLUCIÓN DEL CUESTIONARIO

* ¿Qué son los archivos *.pyc?
  
  Los archivos <code>\*.pyc</code> son archivos ejecutables que contiene código de bytes compilado, Python compila archivos <code>\*.py</code> y guarda su resultado del proceso en archivos <code>\*.pyc</code>, luego puede ser usado para ejecutar programas.

* ¿Para qué sirve el directorio pycache?
  
  En el directorio <code>\_\_pycache\_\_</code> contiene los archivos <code>\*.pyc</code> generados automáticamente cuando los archivos <code>\*.py</code> son compilados por Python

* ¿Cuáles son los usos y lo que representa el subguión en Python?

  En Python el subguión es una convención que significa que la variable o función va a ser para uso interno, a diferencia de Java, Python no tiene keywords como <code>private</code> o <code>public</code>.
  En el laboratorio podemos encontrar una función interna <code>\_invColor</code> que es usada por la función <code>negative</code>.
   
---

III. CONCLUSIONES
	
 - La legibilidad es la mayor característica de python, es un lenguaje fácil de comprender, por ende, fácil de programar.
 - A diferencia de Java, los Strings son más fáciles de manipular en Python, siendo de gran ayuda en la resolución del laboratorio. Podemos manipular los Strings como si fueran un arreglo de caracteres y no tenemos la necesidad de utilizar métodos como <code>substring</code> para acceder a porciones del String.
 - La flexibilidad del código evita problemas de sintaxis, hace de la creación de programas un proceso menos tardío, con simplicidad, pero con eficacia y rápido entendimiento por parte de los programadores.
    
---
    
## RETROALIMENTACIÓN GENERAL

  <pre>
                                                                          
                                                                           
  </pre>

---
    
### REFERENCIAS Y BIBLIOGRAFÍA
<ul>
    <li>https://www.w3schools.com/python/python_reference.asp</li>
    <li>https://docs.python.org/3/tutorial/</li>
</ul>
