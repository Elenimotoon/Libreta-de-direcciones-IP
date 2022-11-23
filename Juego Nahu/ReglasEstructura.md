# Formato del Juego

### Simple
```json
{
    "MAIN": {
        "TITLE": "Insert Title",
        "MAX_HEALTH": 100,
        "HEALTH_OPTIONS": {
            "NUMERIC_HEALTH": true,
            "PERCENT_HEALTH": false,
            "HEALTH_BAR": {
                "HEALTH_BAR_DISPLAY": false
            },
            "HEALTH_FORMAT": "{NUMERIC_HEALTH} HP"
        }
    },
    "MENU": {
        "PLAY": "Start",
        "OPTIONS": null,
        "CREDITS": null,
        "EXIT": "Exit"
    },
    "HISTORY": {
        "PROLOG": "Insert Prolog",
        "CHAPTERS": [
            {
                "CHAPTER_NAME": "Optional chapter name",
                "INITIAL_HEALTH": {
                    "SET_HEALTH": true,
                    "NEW_HEALTH": 100
                },
                "STORYTELLER": "Optional telling",
                "INTERNAL_VOICE": "Optional internal voice/thoughts",
                "PROTAGONIST_DIALOGUE": "Optional protagonist dialogue",
                "OPTIONAL_TEXT": "Additional text",
                "OPTIONS": [
                    {
                        "OPTION_NAME": "Option name",
                        "ACTION": "Option description to select"
                    }
                ],
                "PROTAGONIST_STATS": null
            }
        ]
    }
}
```
### Datallado
```json
{
    "MAIN": {
        "TITLE": "Insert Title",
        "MAX_HEALTH": 100,
        "HEALTH_OPTIONS": {
            "NUMERIC_HEALTH": true,
            "PERCENT_HEALTH": false,
            "HEALTH_BAR": {
                "HEALTH_BAR_DISPLAY": true,
                "LEFT_HEALTH_BAR_SYMBOL": "Left Symbol",
                "RIGHT_HEALTH_BAR_SYMBOL": "Right Symbol",
                "SIZE_SYMBOL": 10
            },
            "HEALTH_FORMAT": "{HEALTH_BAR}  {NUMERIC_HEALTH}"
        }
    },
    "MENU": {
        "PLAY": "Start",
        "OPTIONS": {
            "NAME": "Options",
            "DETAILS": {
                "VOLUME": "Volume",
                "TEXT_SIZE": 16
            }
        },
        "CREDITS": "Insert Credits",
        "EXIT": "Exit"
    },
    "HISTORY": {
        "PROLOG": "Insert Prolog",
        "CHAPTERS": [
            {
                "CHAPTER_NAME": "Optional chapter name",
                "INITIAL_HEALTH": {
                    "SET_HEALTH": true,
                    "NEW_HEALTH": 100
                },
                "STORYTELLER": "Optional telling",
                "INTERNAL_VOICE": "Optional internal voice/thoughts",
                "PROTAGONIST_DIALOGUE": "Optional protagonist dialogue",
                "OPTIONAL_TEXT": "Additional text",
                "OPTIONS": [
                    {
                        "OPTION_NAME": "Option name",
                        "ACTION": "Option description to select",
                        "STORYTELLER": "Optional telling",
                        "INTERNAL_VOICE": "Optional internal voice/thoughts",
                        "PROTAGONIST_DIALOGUE": "Optional protagonist dialogue",
                        "OPTIONAL_TEXT": "Additional text",
                        "OPTIONS": {
                            "DAMAGE": null,
                            "HEALING": null,
                            "POISON": null,
                            "BLEED_OUT": null
                        }
                    }
                ],
                "PROTAGONIST_STATS": {
                    "DAMAGE": null,
                    "HEALING": null,
                    "POISON": null,
                    "BLEED_OUT": null
                }
            }
        ]
    }
}
```

# Reglas de escritura
* Para los **parámetros opcionales**, como los **textos**, si no va a agregar alguno entonces reemplaza el texto entre comillas por `null`.
* Para los parámetros **numéricos** pueden ser reemplazados por `0`, **exceptuando** `MAX_HEALTH` y `NEW_HEALTH`, cosa que si se establecen a `0` aparecerá un mensaje de muerte al comienzo de cada partida, volviéndolo **injugable**.
* Para los parámetros **encerrados entre llaves** (`{}`) o **encerrados entre corchetes** (`[]`) lo recomendable sería reemplazarlos por `null` si no los va a usar.
* Para los casos en el que la historia necesite emplear la utilización de comillas se debería usar comillas Españolas/Latinas/Angulares (`« »`) para evitar conflictos.
## Aclaración
* `MAX_HEALTH` y `NEW_HEALTH` **NO SON LO MISMO**.
* `MAX_HEALTH` sirve para establecer el límite máximo de vida, logrando que el jugador no pueda sobrepasar la cantidad establecida. Mientras que `NEW_HEALTH` establece la vida inicial a la establecida en cada capitulo siempre y cuando se haya establecido `"SET_HEALTH": true` y establecido un valor a `NEW_HEALTH`.
* `"SET_HEALTH": false` **SOLO SIRVE SI EL PRIMER CAPITULO SE HA ESTABLECIDO UNA VIDA INICIAL**,  de lo contrario será imposible de jugar.
# Relación entre formato JSON y diccionarios en Python
![](https://www.freecodecamp.org/espanol/news/content/images/2022/06/image-6.png)
![](https://www.freecodecamp.org/espanol/news/content/images/2022/06/image-10.png)