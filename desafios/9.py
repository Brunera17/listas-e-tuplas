"""
A professora Helena quer facilitar sua rotina na hora de calcular a média das notas finais da turma. Ela sempre anota as notas dos alunos ao longo do semestre e, no final, precisa de um relatório para saber se a turma está indo bem.

Para isso, ajude a professora a criar um programa que receba as notas finais de todos os alunos e calcule a média da turma.

Exemplo de Entrada:

    Digite as notas dos alunos separadas por vírgula: 8.5, 7.0, 9.2, 6.8

Saída esperada:

    Média final da turma: 7.88
"""

notas = list(input("Digite as notas dos alunos separadas por vírgula: ").split(", "))
soma = 0

for nota in notas:
    valor = float(nota)
    soma += valor
    quantidade = notas.index(nota)+1

media = soma / quantidade
print(f"Média final da turma: {media:.2f}")

"""
Correção

Podemos fazer um programa que utiliza o método sum() para calcular a soma de todas as notas, e a função len() para determinar o total de elementos. O for é utilizado para converter os valores de entrada em números decimais, para garantir que o cálculo seja feito corretamente.
"""

notas = input("Digite as notas dos alunos separadas por vírgula: ").split(", ")
notas = [float(nota) for nota in notas]
media = sum(notas) / len(notas)
print(f"Média final da turma: {media:.2f}")