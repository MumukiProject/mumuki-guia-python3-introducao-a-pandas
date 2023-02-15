Como você deve ter notado, os valores podem ser repetidos em uma coluna. Precisamente por isso que o `pandas`  permite obter uma lista dos valores sem repetir ao utilizar a operação `unique`

```python
tabela[nome_coluna].unique()
```

Por exemplo:

```python
ムlivrarias["update_year"].unique()
array([2018, 2020])
```

Como vemos, `unique` retorna esse conjunto de valores únicos na forma de um `array`, que para todos os propósitos práticos podemos pensar como algo muito, muito parecido com uma lista. Se ainda assim queremos transformá-lo em `list` 🔄, podemos fazer: 

```python
ムlist(livrarias["update_year"].unique())
[2018, 2020]
```

Mas normalmente não é necessário, já que os `array`s também são sequências com as quais você pode fazer quase todas as mesmas operações que com `list`s.


> Vamos testar o que vimos!  De **quantas** cidades (diferentes) temos informação neste lote de dados?
