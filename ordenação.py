def buscamenor(arr):
    # Inicializa a variável 'menor' com o primeiro elemento da lista 'arr'
    menor = arr[0]
    # Inicializa a variável 'menor_indice' com 0, o índice do primeiro elemento da lista 'arr'
    menor_indice = 0 
    # Percorre os elementos da lista 'arr' começando do segundo elemento (índice 1) por que o primeiro elemento ja é armazenado na variavel menor.
    for i in range(1, len(arr)):
        # Verifica se o elemento atual é menor do que o valor atualmente armazenado em 'menor'
        if arr[i] < menor:
            # Se o elemento atual for menor, atualiza 'menor' para o valor do elemento atual
            menor = arr[i]
            # Atualiza 'menor_indice' para o índice do elemento atual
            menor_indice = i
    # Retorna o índice do menor elemento encontrado na lista
    return menor_indice

minha_lista = [5,4,6,3,8,9,15,32]

palavras = ["banana", "laranja", "maçã", "abacaxi", "uva"]

def ordenacaoporselecao(arr):
    # Inicializa uma lista vazia para armazenar os elementos ordenados
    novoarr = []
    # Itera sobre todos os elementos da lista de entrada 'arr'
    for i in range(len(arr)):
        # Encontra o índice do menor elemento restante na lista 'arr'
        menor = buscamenor(arr)
        # Remove o menor elemento da lista 'arr' usando o método 'pop(menor)' e o adiciona à lista ordenada 'novoarr' usando o método 'append()'
        novoarr.append(arr.pop(menor))
    # Retorna a lista ordenada
    return novoarr

print (ordenacaoporselecao(palavras))

"""No Python, quando você compara strings usando operadores como <, >, <= ou >=, essas comparações são feitas usando a ordem lexicográfica, que é basicamente a ordem alfabética
 para strings.
Quando você compara duas strings usando <, Python compara os caracteres das strings uma a uma, começando pelo primeiro. Se os caracteres forem iguais, ele passa para o próximo
 par de caracteres. A primeira string é considerada "menor" se seu primeiro caractere vier antes na ordem lexicográfica, ou seja, se tiver um código ASCII menor que o primeiro 
 caractere da segunda string.
Por exemplo:
'a' < 'b' é verdadeiro, porque 'a' tem um código ASCII menor do que 'b'.
'banana' < 'laranja' é verdadeiro, porque o primeiro caractere de 'banana' (que é 'b') vem antes na ordem alfabética do que o primeiro caractere de 'laranja' (que é 'l').
Portanto, o algoritmo de ordenação por seleção usa essa comparação lexicográfica para encontrar a menor palavra em uma lista de palavras. Ele compara as palavras uma a uma,
 caractere por caractere, e encontra a palavra que vem primeiro na ordem alfabética."""

