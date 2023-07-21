# Talana Kombat

## Descripción
este proyecto es una prueba tecnica de talana llamada Talana Kombat JRPG es un emocionante juego de combate en el que dos personajes se enfrentan en un duelo mortal. 
Cada luchador puede ejecutar poderosos golpes especiales mediante combinaciones de movimientos y botones de golpe.

## Pre-requisitos

-   Docker 19.03^

## Instalación 

1. Clonar el repositorio
```
git clone https://github.com/FernandoNoguera/TalanaKombat
```

2. Una vez dentro del directorio del proyecto posicionarse en la rama _develop_
   (o la rama donde necesites trabajar)
```
git checkout develop
```

4. Usar con docker o python

Docker:
```
docker build --tag talana . && docker run -it talana
```

o python:
```
python main.py
```

Esto va a iniciar el script, el cual va a ejecutar los 3 ejemplos y luego va a solicitar un json el cual puedes aplicar con el siguiente formato:
```
{"player1":{"movimientos":["D","DSD","S","DSD","SD"],"golpes":["K","P","","K","P"]},"player2": {"movimientos":["SA","SA","SA","ASA","SA"],"golpes":["K","","K","P","P"]}}
```

y la respuesta esperada sería:
```
Tonyn Stallone se mueve hacia  derecha
Arnaldor Shuatseneguer usa Remuyuken
Tonyn Stallone usa Taladoken
Arnaldor Shuatseneguer se mueve hacia  diagonal superior izquierda
Tonyn Stallone se mueve hacia  abajo
Arnaldor Shuatseneguer usa Remuyuken
Arnaldor Shuatseneguer gana la pelea.
```