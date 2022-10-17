Como você deve ter notado, os valores podem ser repetidos em uma coluna. Precisamente por isso `pandas`  permite obter uma lista dos valores sem repetir com a operação `unique`:

```python
tabela[nome_coluna].unique()
```

Por exemplo:

```python
ム livrarias["update_year"].unique()
array([2018, 2020])
```

Como vemos, `unique` retorna esse conjunto de valores únicos na forma de um `array`, que para todos os propósitos práticos podemos pensar como algo muito, muito parecido com uma lista. Se de todas maneiras queremos transformá-lo em um `list` 🔄, poderemos fazer: 

```python
ム list(livrarias["update_year"].unique())
[2018, 2020]
```

Mas normalmente não será necessário, já que os `array`s também são seqüências com as quais você pode fazer quase todas as mesmas operações que com `list`s.

> Vamos testar o que vimos!  De **quantas** cidades (diferentes) temos informação neste lote de dados?
