# Diseño PCAM

# Particionar

El programa particiona los datos. Los datos consisten en archivos con extensión .fa los cuales contienen la representación en caracteres de cadenas de ADN.
Existen varias tareas en el algoritmo. En primer lugar la selección de archivos, la entrada del programa es una carpeta y solamente se deben seleccionar 
los archivos de extensión .fa. Luego la separación de los archivos en líneas, los archivos consisten en una gran cantidad de líneas y cada una se analiza individualmente.


# Comunicar

Los procesos se comunican por memoria compartida. Los archivos se encuentran en la carpeta /opt/dna la cual es compartida entre los 3 procesos a utilizar.
Se prefiere el uso de memoria compartida ya que los archivos pueden llegar a ser bastante pesados.

# Aglomerar

La tarea a aglomerar es la separación de líneas. A cada proceso se le pasa un archivo completo el cual debe ser analizado línea por línea por cada proceso.

# Mapear

Para este proyecto se tiene previsto un conjunto que consiste en 3 archivos del ADN humano el cual debe ser convertido a ARN. Cada archivo se va a mapear a 
un proceso. Para utilizar el programa se requieren 3 procesos. 
