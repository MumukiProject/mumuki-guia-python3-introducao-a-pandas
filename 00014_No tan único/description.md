Como habrás notado, en una columna se pueden repetir valores. Justamente por eso `pandas` nos permite obtener un listado de los valores sin repetir con la operación `unique`:

```python
tabla[nombre_columna].unique()
```

Por ejemplo:

```python
ム librerias["update_year"].unique()
array([2018, 2020])
```

Como vemos, `unique` retorna ese conjunto de valores únicos en la forma de un `array`, que a los fines prácticos podemos considerarlo como algo muy, muy parecido a una lista. Si de todas formas queremos convertirlo a un `list` 🔄, podremos hacer: 

```python
ム list(librerias["update_year"].unique())
[2018, 2020]
```

Pero normalmente no será necesario, dado que los `array`s son también secuencias con las que podrás hacer casi todas las mismas operaciones que con los `list`s. 

> ¡Pongamos a prueba lo visto! ¿De **cuántas** ciudades (diferentes) tenemos información en este lote de datos?
