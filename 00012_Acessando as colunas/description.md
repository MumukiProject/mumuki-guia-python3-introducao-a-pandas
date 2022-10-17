Já sabemos que podemos conhecer as colunas de um `DataFrame` fazendo `.columns` mas agora vamos acessar uma determinada coluna 🏛. Para isso, usaremos colchetes da seguinte forma:

```python
tabela[nome_coluna] # o nome se encaixa como string
```

Por exemplo, para acessar os nomes de cidades em nossa tabela podemos fazer `livrarias["city_name"]`.


> Tente acessar a outras colunas do `DataFrame` `livrarias`, como `sector` e `update_year`. E o que acontece se tentar acessar uma coluna que não existe? 
