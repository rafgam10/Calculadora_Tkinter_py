# Criando uma calculadora com Tkinter

Criar a calculadora com **Tkinter** foi um processo interessante e desafiador, envolvendo tanto a construção da interface gráfica quanto a implementação da lógica por trás das operações matemáticas.

## 1. Planejamento da Interface
A primeira coisa que fiz foi pensar no design da calculadora. Eu sabia que precisaria de botões para os números (0-9), operadores matemáticos básicos (+, -, *, /), além de botões de função como "C" (para limpar) e "=" (para calcular o resultado).  
Decidi usar o método `grid()` do Tkinter para organizar os botões em um layout de grade, semelhante ao de uma calculadora física, com as operações em uma coluna à direita.

## 2. Configurando a Janela com Tkinter
Usei o **Tkinter** para criar a janela principal e configurei o título da janela e o campo de exibição (o "display" da calculadora).  
O **widget de entrada** (`Entry`) foi configurado para mostrar os números e o resultado. Foi importante garantir que o usuário não pudesse modificar o display diretamente, então fiz com que ele fosse controlado apenas pelos botões.

## 3. Implementação dos Botões
Cada botão numérico foi associado a uma função que, ao ser clicada, adiciona o número correspondente no display.  
Para as operações matemáticas, como adição e subtração, criei funções para armazenar o número atual e a operação selecionada, e depois realizar o cálculo quando o botão "=" fosse pressionado.  
Além disso, o botão "C" limpa o display e redefine a calculadora, permitindo que o usuário comece uma nova operação.

## 4. Funções para Gerenciar as Operações
A parte crucial foi implementar as funções de **soma**, **subtração**, **multiplicação** e **divisão**.  
Cada vez que o usuário clicava em um operador, o número atual era armazenado e o próximo número aguardado.  
Ao pressionar o botão "=", a calculadora recuperava o segundo número e realizava a operação escolhida, exibindo o resultado.  
Também adicionei uma lógica para lidar com **divisão por zero**, exibindo uma mensagem de erro caso ocorresse.

## 5. Tratamento de Erros
Um ponto importante foi garantir que a calculadora funcionasse sem travar ou apresentar erros quando ocorresse uma operação inválida, como a divisão por zero.  
Usei verificações simples para garantir que esses cenários fossem tratados adequadamente.

## 6. Melhorando a Interface
Após garantir que a calculadora funcionava corretamente, fiz alguns ajustes na interface para que ela fosse mais amigável ao usuário. Ajustei o tamanho dos botões, a fonte e o layout geral, criando uma interface visualmente limpa e fácil de usar.

## 7. Testes Finais
Após terminar a implementação, fiz testes com várias operações matemáticas para garantir que a lógica estava correta e que todos os botões funcionavam conforme esperado. Ao final, o resultado foi uma calculadora totalmente funcional.

---

**Design da Calculadora:**

<p align="center">
  <img src="/img/Design da Calculadora.png" alt="Design da Calculadora Tkinter">
</p>

**Imagem da Calculadora:**

<p align="center">
  <img src="/img/Imagem da Calculadora.png" alt="Imagem da Calculadora Tkinter">
</p>