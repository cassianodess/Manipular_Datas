# Manipular_Datas
4) Suponha que necessitamos implementar um sistema que precisa manipular
datas. Faca um programa em Java a partir dos seguintes passos para este fim:
* a) Crie uma classe chamada MinhaData, a qual devera conter 3 campos inteiros
que representam o dia, mês e ano desta data.
* b) Defina um construtor que receba 3 valores e inicialize os 3 campos de um
objeto.
* c) Defina um 2o. construtor que inicialize um objeto a partir de uma string
contendo uma data (p. ex., “1/4/2013”).
* d) Crie um metodo toString() para esta classe que retorna uma string representando
o objeto data.
* e) Crie um metodo chamado compara, que compara a data representada pelo objeto
alvo da chamada com uma data passada como argumento para o metodo; o valor
retornado deve ser 0 se essas datas sao iguais, -1 se a primeira data e anterior à
ultima, ou +1 se a primeira e posterior à ultima.
* f) Crie uma segunda classe, chamada DataComemorativa, a qual representara as
diferentes datas comemorativas. Uma data comemorativa normalmente contem
um nome, se e feriado ou nao, se este feriado e mundial e o dia associado.
* g) Crie uma terceira classe chamada DatasComemorativas, a qual devera conter
uma colecao que armazenara todas as datas comemorativas existentes.
* h) Implemente nesta terceira classe o metodo adiciona(), que insere uma data
comemorativa na lista.
* i) Implemente nesta mesma classe o metodo remove(nome), que remove da lista a
data comemorativa que possui o parâmetro nome fornecido.
* j) Implemente um metodo chamado horasNaoTrabalhadas(), o qual deve retornar a
quantidade de horas nao trabalhadas. Para tal, deve-se contar a quantidade de
datas comemorativas que sao feriados e multiplica-la por 8 (oito) que e a carga
horaria diaria usual de trabalho.
* k) Teste as classes criadas da seguinte forma: i) No metodo main(), crie 1 data que
represente a data atual e outra que represente o Natal deste ano; ii) Chame o
metodo de comparacao das datas e imprima seu valor; iii) Adicione o objeto
Natal à coleção DatasComemorativas e chame o método horasNaoTrabalhadas().
