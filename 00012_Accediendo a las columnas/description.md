Ya sabemos que podemos conocer las columnas de un `DataFrame` haciendo `.columns` pero ahora vamos a acceder a una columna en particular 🏛️. Para eso utilizaremos corchetes de la siguiente forma: 

```python
tabla[nombre_columna] # el nombre se pasa como string
```

Por ejemplo, para acceder a los nombres de ciudad de nuestra tabla podemos hacer `librerias["city_name"]`. 

> Probá acceder a otras columnas del `DataFrame` `librerias`, como `sector` y `update_year`. ¿Y qué pasa si intentás acceder a una columna que no existe? 

