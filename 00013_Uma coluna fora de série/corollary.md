As três operações funcionam! 🎊 Mas há uma diferença sutil: quando usamos `head` e `tail` com `Series`, eles retornam outra 'Séries' com os valores selecionados.

É que os `DataFrame`s e as `Series` são estruturas diferentes, então pode acontecer que em algumas operações os argumentos que usamos mudem, eles retornam coisas diferentes, ou diretamente... eles não funcionam com ambas!
