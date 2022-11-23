# Base climática

Este é um respositório destinado a prática 6 da disciplina SEL0630 - Aplicações de Microprocessadores II.

## Acesso a API

Para aquisição dos dados meteriológicos foram utilizadas três bibliotecas para facilitar o acesso: *requests, json e pprint*.

A requisição dos dados foi feita a partir do comando ```get()``` da biblioteca *requests*, sendo necessário oferecer como parâmetro a *url* fornecida pela API juntamente com o ID do sensor meteriológico desejado.

Em seguida os dados foram convertidos no formato tradicional de json pelo próprio comando ```.json()```, por fim acessamos os dados que nos interessava pelos index ```['itens']``` e ```[0]```.

O comando ```pprint``` foi utilizado para apresentar os dados no console de forma simplificada.

## PiCamera

Inicialmente, inicializamos um objeto do tipo ```PiCamera``` e atribuímos a ```camera```. Isso nos dá acesso aos seguintes métodos utilizados:

- ```start_preview()``` - Comando que mostra a visão da camera em tempo real.
- ```annotate_text ()``` - Comando que permite a adição de texto a imagem da câmera.
- ```capture()``` - Comando que tira uma foto da visão da câmera e salva em determinado diretório.
- ```start_recording()``` - Comando que inicia a gravação de um vídeo e salva em determinado diretório.
- ```stop_recording()``` - Comando que encerra a gravação do vídeo.
- ```stop_preview()``` - Comando que encerra a visualização da visão da câmera.

Desse modo o utilizamos o método ```annotate_text ()``` para salvar alguns dados na imagem da câmera, como:

- Número USP dos alunos
- Local
- Umidade
- Velocidade do Vento

Por fim foi retirada uma foto por meio do comando ```capture()``` e gravado um curto vídeo de 5 segundos utilizando ```start_recording()```, ```sleep(5)```, ```stop_recording()```.
