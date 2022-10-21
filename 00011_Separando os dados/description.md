No início desta lição falamos que _csv_ é uma extensão de arquivos que têm seus valores separados por vírgulas. No entanto, às vezes pode acontecer que outro caractere seja usado para separar os valores, como por exemplo, ponto e vírgula:


```csv
nome;sobrenome;idade
Feli;Perez;24
Dani;Lopez;32
Juani;Vazquez;19
```

O problema é que esses casos `read_csv` não funcionará :grimacing:. Mas não entre em pânico que isso será resolvido facilmente 😌. Temos apenas que passar um parâmetro `sep` a `read_csv`!

```python
pessoas = pd.read_csv(localizacao, sep=";")
```

> Vamos deixar para trás os cinemas e mudar nosso lote de dados. A partir de agora vamos trabalhar com um arquivo de livrarias :books: em formato _tsv_, ou seja, um arquivo com valores separados por tabulações `Tab ↹ `. Faça upload em uma nova célula fazendo o seguinte…
>
> ```python
> import pandas as pd # se em uma célula anterior já fez upload com pandas,  
                                        # esta linha você pode omitir
> livrarias = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRSa9oM9fC-QlT7VOeGhZQtrWnlNSTsk3U8DWGTOXUWtPH6u9o5O5eZ0kTg8mFTwAn9vMdGRK7o2SPB/pub?gid=1473087913&single=true&output=tsv", sep="\t")
> livrarias
> ```
>
> … e nos vemos no próximo exercício 👋.
