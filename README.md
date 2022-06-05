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
   <!-- tree -->
    ```
* Funciones de la clase Picture:  

    * Función verticalMirror:

    * Función horizontalMirror:

    * Función negative:

      En la función <code>negative</code> vamos a utilizar la función <code>\_invColor</code> la cual es una función de propósito interno y recibe un caracter y devuelve otro caracter que se entiende como su color inverso. Luego iteramos sobre toda la imagen invirtiendo su color.

    * Función join:

    * Función up:

    * Función under:

    * Función horizontalRepeat:

      Para esta función se recibe un entero <code>n</code> el cual nos va a indicar el número de veces que vamos a repetir horizontalmente la imagen. Con ayuda de un ciclo <code>for</code> vamos a crear la imagen y repetirla horizontalmente.

    * Función verticalRepeat:

      En esta función recibimos un entero <code>n</code> y con la función <code>append</code> vamos a repetirlo verticalmente.

    * Función rotate:

      La función <code>rotate</code> se va aplicar a un objeto <code>Picture</code> con el fin de rotarlo 90° sentido horario, para resolver está función se hizon un análisis previo para saber como es que las posiciones debían rotar.

* Ejercicios Propuestos:

    * Ejercicio A:

    * Ejercicio B:

    * Ejercicio C:

    * Ejercicio D:

    * Ejercicio E:

    * Ejercicio F:

    * Ejercicio G:
     
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