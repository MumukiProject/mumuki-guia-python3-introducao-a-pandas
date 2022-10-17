Ya sabemos que a lo que llamamos tabla `pandas` lo llama `DataFrame`. De la misma forma, lo que llamamos columna `pandas` lo llama `Series`. ¡Sí, en plural aunque sea una! 

```python
ム type(librerias["sector"])
pandas.core.series.Series
```

Esto significa que cada `DataFrame` está compuesto por muchas `Series`. Algo muy interesante es que hay operaciones que funcionan con cualquiera de los dos tipos de datos 😮. 

> Probá las siguientes expresiones y seleccioná cuáles funcionan:
