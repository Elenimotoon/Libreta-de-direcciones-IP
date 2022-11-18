# Formato del Juego

### Simple
```json
{
    "TITLE": "Insert Title",
    "MAX_HEALTH": 100,
    "LIVE_BAR_SYMBOL": none,
    "SIZE_SYMBOL": 0,
}

# Menu
# Configurable
{
    "PLAY": "Start",
    "OPTIONS": {},
    "CREDITS": none,
    "EXIT": "Exit",
}

{
    "PROLOG": "Insert Prolog",
    "CHAPTER_1": {
        "NAME": "Optional chapter name",
        "STORYTELLER": "Optional telling",
        "INTERNAL_VOICE": "Optional internal voice/thoughts",
        "PROTAGONIST_DIALOGUE", "Optional protagonist dialogue",
        "OPTIONAL_TEXT": "Additional text",
        "OPTIONS": {}
    }
}
```
### Datallado
```json
{
    "TITLE": "Insert Title",
    "MAX_HEALTH": 100,
    "LIVE_BAR_SYMBOL": "Symbol",
    "SIZE_SYMBOL": 10,
}

# Menu
# Configurable
{
    "PLAY": "Start",
    "OPTIONS": {
        "NAME": "Options",
        "DETAILS": {
            "VOLUME": "Volume",
            "TEXT_SIZE": 16
        }
    },
    "CREDITS": "Insert Credits",
    "EXIT": "Exit",
}

{
    "PROLOG": "Insert Prolog",
    "CHAPTER_1": {
        "NAME": "Optional chapter name",
        "STORYTELLER": "Optional telling",
        "INTERNAL_VOICE": "Optional internal voice/thoughts",
        "PROTAGONIST_DIALOGUE", "Optional protagonist dialogue",
        "OPTIONAL_TEXT": "Additional text",
        "OPTIONS": {
            {
                "NAME": "Option name",
                "ACTIONS": "Option description to select",
                "STORYTELLER": "Optional telling",
                "INTERNAL_VOICE": "Optional internal voice/thoughts",
                "PROTAGONIST_DIALOGUE", "Optional protagonist dialogue",
                "OPTIONAL_TEXT": "Additional text",
                "OPTIONS": {}
            }
        }
    }
}
```

# Reglas de escritura
* Para los **parámetros opcionales**, como los **textos**, si no va a agregar alguno entonces reemplaza el texto entre comillas por `none`.
* Para los parámetros **numéricos** pueden ser reemplazados por `0`, **exceptuando** `MAX_HEALTH`, cosa que si se establece a `0` aparecerá un mensaje de muerte al comienzo de cada partida, volviéndolo **injugable**.
* Para los parámetros **encerrados entre llaves** (`{}`) puede dejarlos vacíos si no los va a usar.