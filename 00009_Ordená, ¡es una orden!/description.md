¡Esto es un desorden! :rage: Pero traemos buenas noticias: podemos ordenar nuestros `DataFrame`s por la columna que queramos. Y no sólo eso: ¡podemos hacerlo al derecho y al revés!

`sort_values` es una operación que nos permite ordenar nuestras tablas a partir de una columna haciendo `tabla.sort_values(nombre_columna)`. Contra lo que el nombre podría dar a entender, **no modifica nuestra tabla original** :bangbang:, sino que devuelve una nueva

Por defecto lo hará de forma ascendente :arrow_up:. Por ejemplo, si la columna elegida es numérica ordenará de menor a mayor, pero si es de strings lo hará en orden alfabético.  Si en cambio queremos que el ordenamiento sea descendente :arrow_down: debemos hacer `tabla.sort_values(nombre_columna, ascending=False)`. 


> ¡Probémoslo! Escribí las siguientes expresiones en varias celdas:
>
> * `cines.sort_values("city")`
> * `cines.sort_values("city", ascending=False)`
> * `cines.sort_values("screens")`
> * `cines.sort_values("screens", ascending=False)`
>
> Además, prestá atención a lo que pasa con la _primera columna_, ¿qué sucede con ella?
