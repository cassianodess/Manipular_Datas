# Manipular_Datas
1. Suponha que necessitamos implementar um sistema que precisa manipular
datas. Faca um programa a partir dos seguintes passos para este fim:
* a) Crie uma classe chamada `MinhaData`, a qual deverá conter 3 campos inteiros
que representam o `dia`, `mês` e `ano` desta data.
* b) Defina um construtor que receba 3 valores e inicialize os 3 campos de um
objeto.
* c) Defina um 2º construtor que inicialize um objeto a partir de uma string
contendo uma data ex.: `“1/4/2013`.
* d) Crie um metodo `toString()` para esta classe que retorna uma string representando
o objeto data.
* e) Crie um método chamado `compara`, que compara a data representada pelo objeto
alvo da chamada com uma data passada como argumento para o método, o valor
retornado deve ser `0` se essas datas sao iguais, `-1` se a primeira data e anterior à
ultima, ou `+1` se a primeira e posterior à ultima.
* f) Crie uma segunda classe, chamada `DataComemorativa`, a qual representará as
diferentes datas comemorativas. Uma data comemorativa normalmente contém
um nome, se é feriado ou não, se este feriado é mundial e o dia associado.
* g) Crie uma terceira classe chamada `DatasComemorativas`, a qual deverá conter
uma coleção que armazenará todas as datas comemorativas existentes.
* h) Implemente nesta terceira classe o método `adiciona()`, que insere uma data
comemorativa à lista.
* i) Implemente nesta mesma classe o método `remove(nome)`, que remove da lista a
data comemorativa que possui o parâmetro nome fornecido.
* j) Implemente um método chamado `horasNaoTrabalhadas()`, o qual deve retornar a
quantidade de horas não trabalhadas. Para tal, deve-se contar a quantidade de
datas comemorativas que são feriados e multiplicá-la por 8 (oito) que é a carga
horária diária usual de trabalho.
* k) Teste as classes criadas da seguinte forma:
  * i) No metodo `main()`, crie 1 data que represente a data `atual` e outra que represente o `Natal` deste ano;
  * ii) Chame o método de comparação das datas e imprima seu valor;
  * iii) Adicione o objeto `Natal` à coleção `DatasComemorativas` e chame o método `horasNaoTrabalhadas()`.
