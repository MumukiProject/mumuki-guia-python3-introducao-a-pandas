Já sabemos que o que chamamos de tabela `pandas` chama-se `DataFrame`. Da mesma forma, o que chamamos de coluna `pandas` chama-se `Series`. Sim, no plural mesmo sendo uma só!

```python
ム type(livrarias["sector"])
pandas.core.series.Series
```

Isso significa que cada `DataFrame` está composto por muitas `Series`. Algo muito interessante é que há operações que funcionam com qualquer dos dois tipos de dados 😮.

> Experimente as seguintes expressões e selecione quais funcionam:
