# MeteorChallenge

Tasks:

- Count the number of Stars

- Count the number of Meteors

- If the Meteors are falling perpendicularly to the Ground (Water level), count how many will fall on the Water

- (optional) Find the phrase that is hidden in the - dots in the sky.

  - HINT 1: 177 Characters

  - HINT 2: Most of the last tasks’ code can be reused for this one

Please, send us the result and code you used to solve the tasks above. Explain how you achieved the results in each question. Good work!!

Subject: [CHALLENGE] [METEOR] your name

## Contando o número de estrelas e meteoros

Dado uma imagem 704x704 pixels, uma varredura simples na matriz RGB resolve o problema em um tempo satisfatório. Dessa forma:
  - Os meteoros possuem um valor RGB = [255,0,0]. 
  - As estrelas possuem um valor RGB = [255,255,255].

Para uma melhor visualização foi desenhado um circulo roxo em volta dos meteoros e um vermelho em volta das estrelas.

![alt text](https://github.com/jeanhardzz/MeteorChallenge/blob/main/result.jpg?raw=true)

## Conclusão

Para realizar a contagem das estrelas e dos meteoros foram usadas operações na matriz de pixels da imagem. Para este problema não houve necessidade de elaborar operações complexas a fim de minimizar o tempo do algoritmo, uma vez que a matriz referente a imagem era relativamente pequena. Assim foi feita uma varredura simples na matriz para encontrar e contar os elementos relevantes.

- **Estrelas**: 315
- **Meteoros**: 328
- **Meteros caindo na agua**: 105

Sobre a questão opcional, onde o objetivo é encontrar a frase oculta, não foi encontrada. Deixei explicitado acima o meu raciocínio ao tentar encontra-la investigando código binário e código morse.
