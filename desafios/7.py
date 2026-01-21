"""
O clube de atletismo Alura Runners organizou uma corrida e divulgou a lista com a classificação final dos participantes. Mas, um erro foi identificado: um dos nomes está incorreto. O organizador precisa de um programa que permita localizar o nome errado e substituí-lo pelo correto.

Como você escreveria um programa que solicite o nome errado, o nome correto e atualize a lista exibindo a nova classificação ao final?

Exemplo de Entrada:

    Digite o nome incorreto: Carlos
    Digite o nome correto: João

Saída esperada:

    O nome Carlos foi substituído por João.
    Lista atualizada: ['Ana', 'João', 'Pedro']
"""

candidatos = ["Ana", "Carlos", "Pedro"]

nome_incorreto = input("Digite o nome incorreto: ")

if nome_incorreto in candidatos:
    nome_correto = input("Digite o nome correto: ")
    posicao = candidatos.index(nome_incorreto)
    candidatos.remove(nome_incorreto)
    candidatos.insert(posicao, nome_correto)
    print(f"O nome {nome_incorreto} foi substituido por {nome_correto}.")
    print("Lista atualizada: ", candidatos)
else:
    print("Nome não encontrado")