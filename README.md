# Proyecto 4

## Problema

Consiste en resolver un problema diseñando una solución mediante un algoritmo paralelizable. El problema a resolver es la síntesis de ARN que consiste en hacer una copia complementaria de un segmento de ADN. Ambos son estructuralmente diferentes, el ARN se diferencia en un azúcar, la ribosa, y en una base, el uracilo. 

![Síntesis de ARN](http://www.botanica.cnba.uba.ar/Pakete/3er/LosCompuestosOrganicos/1111/Transcripcion_archivos/image002.gif)

Para realizar esta síntesis la ARN-Polimerasa se fija en una región del ADN, desenreda una hélice que será utilizada como patrón para la síntesis del ARN, siguiendo la complementariedad de bases. Por ejemplo una secuencia de ADN 'TACGCT' pasa a ser una secuencia de ARN de la forma 'AUGCGA'. 

Luego que se completa la síntesis de ARN el ADN se cierra nuevamente y el ARN sintetizado queda libre. [1]


## Solución

Para la solución han sido implementados dos scripts en python que simulan la sintetización del ARN. Uno serial y otro distribuido utilizando mpi4py. [2]  El script distribuido corre en tres nodos, cada uno trabaja sobre un dataset diferente utilizando memoria compartida. 

La solución cuenta con dos scripts, uno para el código serial y otro para el código paralelo. Para correr los programas se deben entrar a la carpeta src y ejecutar el script.

Para el serial:
```
proyecto4/src> ./serial

```


Para el paralelo:

```
proyecto4/src> ./parallel

```
Los scripts crean la carpeta donde será almacenada la respuesta y corren el programa.

## Referencias

[1] http://www.botanica.cnba.uba.ar/Pakete/3er/LosCompuestosOrganicos/1111/Transcripcion.htm

[2] https://mpi4py.readthedocs.io/en/stable/
