¡Pudimos sacar muchas conclusiones! 😁

Pasemos en limpio lo que acabamos de ejecutar. `value_counts` nos retorna una columna (`Series`) con la cantidad de ocurrencias de cada valor de la columna que le pasamos como argumento: 

```python
ム pd.value_counts(librerias["prov_name"])
Ciudad Autónoma de Buenos Aires                          608
Buenos Aires                                             386
Córdoba                                                  163
Santa Fe                                                 116
(...)
La Pampa                                                  13
San Luis                                                  11
Santiago del Estero                                        8
La Rioja                                                   6
Tierra del Fuego, Antártida e Islas del Atlántico Sur      4
Formosa                                                    3
Catamarca                                                  3
Name: prov_name, dtype: int64
```

No solo eso sino que además nos retorna esos valores ordenados de forma descendente. ¡`value_counts` es suuuuper útil! ♥️
