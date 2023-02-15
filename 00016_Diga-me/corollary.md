Conseguimos tirar muitas conclusões!😁

Vamos passar a limpo o que acabamos de executar. `value_counts` retorna uma coluna (`Series`) com o número de ocorrências de cada valor da coluna que passamos como argumento:

```python
ムpd.value_counts(livrarias["prov_name"])
Ciudad Autónoma de Buenos Aires                          608
Buenos Aires                                             386
Córdoba                                                  163
Santa Fe                                                 116
Mendoza                                                   46
Entre Ríos                                                32
Chaco                                                     31
Neuquén                                                   26
Río Negro                                                 24
Tucumán                                                   23
Misiones                                                  23
Salta                                                     21
Chubut                                                    19
Corrientes                                                17
Santa Cruz                                                14
San Juan                                                  13
Jujuy                                                     13
La Pampa                                                  13
San Luis                                                  11
Santiago del Estero                                        8
La Rioja                                                   6
Tierra del Fuego, Antártida e Islas del Atlántico Sur      4
Formosa                                                    3
Catamarca                                                  3
Name: prov_name, dtype: int64
```

Não só isso, mas também retorna esses valores organizados em ordem decrescente. `value_counts` é suuuuper útil! ♥️
