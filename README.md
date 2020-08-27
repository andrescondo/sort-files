# Sort files

#### Ordenamiento de archivos según su extensión

## Requerimientos
Se necesita que en el computador tenga **Python** en la version 3.x [Descarga Python3.x](https://www.python.org/downloads/)

*De preferencia python 3.6 ó superior*


## Funcionamiento

El programa permite discriminar los archivos de diferentes formatos, desde documentos de texto ('.txt'), hasta archivos de videos ('.mp4'). Se encarga de crear una carpeta diferente por tipo de extensión y mueve los archivos a las carpetas correspondiente.

El programa al recorrer el directorio actual, y va verificando fichero por fichero, verificando su extensión, y de no existir un directorio con ese nombre, lo crea y avanza con el siguiente. El programa por defecto ignora los directorios que ya fueron creadas, y el mismo archivo python (.py), ya que el moverlo podría causar algún problema en el funcionamiento.

Una vez creado todos los directorios por extensión existente, procede a moverlo a su carpeta mostrando en pantalla que archivo a sido movido de su posición original. Ya realizado este proceso el programa se cierra.


## Correr el programa

Dependiendo de tu sistema operativo (SO). El comando puede variar, pero el funcionamiento será el mismo. Acontinuación algunos de las posibles formas de hacer correr el programa.

**Diferentes formas**
```
py index.py
```
ó
```
python index.py
```
ó
```
python3 index.py
```

## Del autor

*Espero que el programa te ayude, ya sea desde organizar los archivos de tu ordenador, hasta poder crear algo más grande usando mi proyecto como base o apoyo.*


## Este proyecto esta bajo la licencia (MIT) 

### mira el archivo [LICENSE](LICENSE) para más detalles
