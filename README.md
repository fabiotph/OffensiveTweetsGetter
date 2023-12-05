# OffensiveTweetsGetter

Esse projeto faz buscas na base do Twitter por palavras-chave ou trechos de frases e salva em um arquivo csv.

## :green_circle: Como Executar
1. Adicione seu token da api do Twitter à variável de ambiente ```TWITTER_TOKEN```

2. Edite o arquivo script.sh passando a lista com as palavras-chave e a quantidade de itens que deseja buscar, utilizando o padrão especificado abaixo:

  ```
  "'<text>' <count> <[optional] exact>" 
  
       - text: text to search
       - count: number of total results
       - exact: if "false" or "False" not search perfect match
      
  Examples:
       "'bom dia' 10": search 10 tweets with "bom dia"
       "'bom dia' 10 false": search 1o tweets with "bom" and "dia"
  ```

3. Execute o arquivo script.sh
