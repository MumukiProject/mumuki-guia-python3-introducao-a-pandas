Ya vimos cómo acceder a una columna por su nombre, pero ¿y si queremos acceder a una fila en particular? ¡Para hacerlo contamos con `iloc`!  Por ejemplo, si quisiéramos obtener la quinta fila de nuestro dataset deberíamos hacer:

```python
ム librerias.iloc[4] # sí, con corchetes
city_id                                2000010
prov_id                                      2
dep_id                                    2000
obs                                        NaN
category                             Librerias
prov_name      Ciudad Autónoma de Buenos Aires
dep_name       Ciudad Autónoma de Buenos Aires
city_name      Ciudad Autonoma de Buenos Aires
(...)
sector                                 Privado
update_year                               2018
Name: 4, dtype: object
```

Como vemos, `iloc[]` nos devolverá un `Series`, que ahora representa una fila en lugar de una columna. ¿Y por qué 4 si es la **quinta** fila? Porque al igual que las listas, las filas empiezan desde la posición 0. 

¡Y no se parecen sólo en eso! Usando `iloc` también podemos obtener segmentos usando la sintaxis de _slices_, que ahora nos devolverá un `DataFrame`: 

```python
ム librerias.iloc[5:8]
```

||city_id|prov_id|dep_id|obs|category|prov_name|(...)|
|---|---|---|---|---|---|---|---|
|5|2000010|2|2000||Librerias|Ciudad Autónoma de Buenos Aires|(...)|
|6|2000010|2|2000||Librerias|Ciudad Autónoma de Buenos Aires|(...)|
|7|2000010|2|2000||Librerias|Ciudad Autónoma de Buenos Aires|(...)|


> ¡Veamos si se entendió! En una nueva celda de tu cuaderno, asigná las siguientes variables: 
> 
> * `primera_libreria`: un `Series` con la primera fila de `librerias`
> * `segunda_y_tercera_libreria`: un `DataFrame` con las correspondientes filas de `libreria`
> * `ultima_libreria`: similar a `primera_libreria`, pero en este caso con la última.
