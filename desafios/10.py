"""
Uma escola está organizando os dados dos alunos para criar um relatório resumido. Cada aluno tem seus dados registrados em uma única entrada, incluindo nome, idade e nota final no semestre. Esses dados devem ser exibidos separadamente para cada aluno no formato abaixo:

    Aluno: Nome
    Idade: Idade
    Nota: Nota

Ajude a escola a desenvolver um programa que registre as informações dos alunos, organize os dados e exiba um relatório detalhado com as informações separadamente.

Exemplo de Entrada:

    Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: João, 16, 8.5, Maria, 17, 9.2, Pedro, 15, 7.8

Saída esperada:

    Aluno: João
    Idade: 16
    Nota: 8.5

    Aluno: Maria
    Idade: 17
    Nota: 9.2

    Aluno: Pedro
    Idade: 15
    Nota: 7.8
"""

alunos = tuple(input("Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ").split(", "))

cadastros = [alunos]

for cadastro in cadastros:
    nome, idade, nota = cadastro
    print(f"Aluno: {nome}")
    print(f"Idade: {idade}")
    print(f"Nota: {nota}")

""" 
Correção

Neste exercício, usamos tuplas para armazenar os dados de cada aluno, como nome, idade e nota. O laço for é utilizado para desempacotar as tuplas, onde temos 3 elementos por aluno: nome, idade e nota.

Além disso, utilizamos a sintaxe range(0, len(dados), 3), onde o último parâmetro serve para avançar de 3 em 3 posições. Com isso, ele sempre pega o índice do nome de cada aluno (que está na posição 0, 3, 6, etc.). Porém, para acessar a idade e a nota de cada aluno, precisamos dos índices adjacentes ao índice do nome, ou seja, i + 1 para a idade i+2 para a nota.

"""

dados = input("Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ").split(", ")

for i in range(0, len(dados), 3):
    nome, idade, nota = dados[i], int(dados[i + 1]), float(dados[i + 2])
    print(f"Aluno: {nome}")
    print(f"Idade: {idade}")
    print(f"Nota: {nota}\n")