Agora que importamos a biblioteca `pandas`, o próximo passo é obter um lote de dados, como por exemplo, [uma lista de cinemas na Argentina](https://docs.google.com/spreadsheets/d/e/2PACX-1vRSa9oM9fC-QlT7VOeGhZQtrWnlNSTsk3U8DWGTOXUWtPH6u9o5O5eZ0kTg8mFTwAn9vMdGRK7o2SPB/pub?gid=969960562&single=true&output=csv),

Depois de encontrarmos o endereço, devemos copiar o link na prancheta 📋, para não precisarmos escrever o endereço à mão, 💡 Dica: se você o encontrar enquanto navega na Internet, geralmente pode copiar esse link usando o botão secundário do _mouse_ 🖱️.

E agora sim, podemos finalmente fazer upload em um `DataFrame` chamado `cinemas` usando a função `read_csv`:

```python
import pandas as pd

cinemas = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vRSa9oM9fC-QlT7VOeGhZQtrWnlNSTsk3U8DWGTOXUWtPH6u9o5O5eZ0kTg8mFTwAn9vMdGRK7o2SPB/pub?gid=969960562&single=true&output=csv")
cinemas
```

> Hora de sujar as mãos!
>
> 1. Crie um _caderno interativo_ no Colab ou Jupyter (se ainda não fez)
> 2. Adicione uma célula de código
> 3. Cole o código anterior em uma nova célula
> 4. E, finalmente, execute a célula.
>
> O que acontece?
