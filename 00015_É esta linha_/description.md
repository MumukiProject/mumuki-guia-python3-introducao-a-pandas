Já vimos como acessar uma coluna pelo nome, mas e se quisermos acessar uma determinada linha? Para fazer isso temos `iloc`! Por exemplo, se quiséssemos obter a quinta linha do nosso dataset, deveríamos fazer:

```python
ム livrarias.iloc[4] # sim, com colchetes
city_id                                2000010
prov_id                                      2
dep_id                                    2000
obs                                        NaN
category                             Livrarias
prov_name      Ciudad Autónoma de Buenos Aires
dep_name       Ciudad Autónoma de Buenos Aires
city_name      Ciudad Autonoma de Buenos Aires
(...)
sector                                 Privado
update_year                               2018
Name: 4, dtype: object
```

Como vemos, `iloc[]` retornará um `Series`, que agora representa uma linha em vez de uma coluna. E por que 4 se é a **quinta** linha? Porque assim como as listas, as linhas começam da posição 0.

E eles não se parecem apenas nisso! Usando `iloc` também podemos obter segmentos usando a sintaxe de _slices_, que agora retornará um `DataFrame`:


```python
ム livrarias.iloc[5:8]
```

||city_id|prov_id|dep_id|obs|category|prov_name|(...)|
|---|---|---|---|---|---|---|---|
|5|2000010|2|2000||Librerias|Ciudad Autónoma de Buenos Aires|(...)|
|6|2000010|2|2000||Librerias|Ciudad Autónoma de Buenos Aires|(...)|
|7|2000010|2|2000||Librerias|Ciudad Autónoma de Buenos Aires|(...)|

> Vejamos se ficou claro! Em uma nova célula do seu caderno, atribua as seguintes variáveis:

> 
> * `primeira_livraria`: um `Series` com a primeira linha de `livrarias`
> * `segunda_e_terceira_livraria`: um `DataFrame` com as correspondentes linhas de `livraria`
> * `ultima_livraria`: similar a `primeira_livraria`, mas neste caso com a última.
