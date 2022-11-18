# Formato del Juego

```
#INICIO|Introducción
*ACCiON_1|Opciones/Acciones
*ACCiON_2|Opciones/Acciones
.
.
.
*ACCiON_X|Opciones/Acciones

#ACCiON_1|Narración/Dialogo
*ACCiON_N|Opciones/Acciones

#ACCiON_2|Narración/Dialogo
ACCiON_T|Opciones/Acciones
.
.
.
#ACCiON_X|Narración/Dialogo
ACCiON_H|Opciones/Acciones
```

# Reglas de escritura
+ El `#INICIO` es el único texto no modificable, mientras todas las `ACCION_` son modificables a un valor más cómodo.
+ Tener en cuenta que tiene un **formato Clave-Valor**, por lo que **no es recomendable repetir los nombres de la acciones** a menos que realmente quiera regresar a una acción anterior.
+ Puede anidar tantas acciones como quiera siempre y cuando respete la regla anterior.
+ Para **añadir** o **quitar vida** al personaje, luego de cada `Narración/Dialogo` correspondiente, debe **agregarle** a continuación `|10`. En este caso se le añadirían 10 punto de vida
+ Tener en cuenta que manipular la vida del jugador es completamente **opcional** y si no desea manipularla **no tiene que hacer** `|0`, si no lo agrega el juego interpretará que no ha habido cambios en su salud
+ Si en algún punto de la historia quiere darle un **Game Over definitivo** al jugador al realizar una acción incorrecta, entonces tiene que **quitarle toda la vida** luego de la narración y **sin** necesidad de añadirle más **acciones anidadas**.
	+ > Ej: `#ACCiON_X|Narración/Dialogo|-1000`