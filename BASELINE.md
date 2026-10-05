# Medición de referencia

Medición realizada antes de los cambios de rendimiento:

```text
Comando: uv run main.py
Tiempo total: 3:09,12 (189,12 segundos)
Tiempo de usuario: 68,29 segundos
Tiempo de sistema: 32,14 segundos
CPU: 53 %
```

La cifra corresponde a la ejecución comunicada para establecer la referencia.

## Después de los cambios

Medición ejecutada tras reutilizar el navegador, esperar a `domcontentloaded` y
procesar hasta cuatro fichas de producto en paralelo:

```text
Comando: time uv run main.py
Tiempo total: 19,640 segundos
Tiempo de usuario: 14,25 segundos
Tiempo de sistema: 8,32 segundos
CPU: 114 %
```

La ejecución procesó 36 productos. Frente a la referencia de 189,12 segundos,
esta medición tardó 169,48 segundos menos (aproximadamente 89,6 % menos; unas
9,6 veces más rápida). Las mediciones dependen de la red y del estado de la web.
