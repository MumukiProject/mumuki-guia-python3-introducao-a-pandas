Isso é uma bagunça! :rage: Mas temos boas notícias: podemos ordenar nossos `DataFrame`s pela coluna que queremos. E não apenas isso: podemos fazê-lo de trás para a frente!

`sort_values` é uma operação que  permite ordenar nossas tabelas a partir de uma coluna fazendo `tabela.sort_values(nome_coluna)`. Ao contrário do que o nome pode sugerir, **não modifica nossa tabela original** :bangbang:, mas retorna uma nova.

Por padrão, fará de forma crescente :arrow_up:. Por exemplo, se a coluna escolhida for numérica,  ordenará do menor para o maior, mas se for de strings, será em ordem alfabética. Se em vez disso queremos que a organização seja decrescente :arrow_down: devemos fazer `tabela.sort_values(nome_coluna, ascending=False)`.

> Vamos tentar! Escreva as seguintes expressões em várias células:
>
> * `cinemas.sort_values("city")`
> * `cinemas.sort_values("city", ascending=False)`
> * `cinemas.sort_values("screens")`
> * `cinemas.sort_values("screens", ascending=False)`
>
> Além disso, preste atenção ao que acontece com a _primeira coluna_, o que acontece com ela?
