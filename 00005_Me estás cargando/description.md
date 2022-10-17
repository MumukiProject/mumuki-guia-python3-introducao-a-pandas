Ahora que importamos la biblioteca `pandas`, el siguiente paso es conseguir un lote de datos, como por ejemplo, [un listado de cines que hay que Argentina](https://docs.google.com/spreadsheets/d/e/2PACX-1vRSa9oM9fC-QlT7VOeGhZQtrWnlNSTsk3U8DWGTOXUWtPH6u9o5O5eZ0kTg8mFTwAn9vMdGRK7o2SPB/pub?gid=969960562&single=true&output=csv),

Una vez que hayamos encontrado la dirección, deberemos copiar su enlace en el portapapeles 📋, para no tener que escribir la dirección a mano, 💡 Tip: si la encontrás navegando en Internet, normalmente podés copiar ese enlace usando el botón secundario del _mouse_ 🖱️.

Y ahora sí, podremos finalmente cargarla en un `DataFrame` llamado `cines` utilizando la función `pd.read_csv`:

```python
import pandas as pd

cines = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRSa9oM9fC-QlT7VOeGhZQtrWnlNSTsk3U8DWGTOXUWtPH6u9o5O5eZ0kTg8mFTwAn9vMdGRK7o2SPB/pub?gid=969960562&single=true&output=csv")
cines
```

> ¡Hora de ensuciarse las manos! 
> 
> 1. Creá un _cuaderno interactivo_ en Colab o Jupyter (si no lo hiciste ya)
> 2. Agregá una celda de código
> 3. Pegá el código anterior en una nueva celda
> 4. Y por último, ejecutá la celda. 
>
> ¿Qué sucede? 
