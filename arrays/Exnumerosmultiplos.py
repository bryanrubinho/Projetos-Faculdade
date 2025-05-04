#6) Elaborar um algoritmo que o usuário tenha que digitar 10 números inteiros. No final, o programa
#deve exibir quantos números são múltiplos de 3, quantos números são menores que 45 e maiores
#que 55, e qual é o menor número entre eles.

num=[]
entre=0
multiplo=0
menor= None
#faz a repeticao e a contagem de 10 vezes solicitar o nome
for x in range (1, 11):
    num= int(input("Insira um numero:\n"))
    #verifica se e multiplo
    if num % 3 ==0 :
        multiplo += 1
    #verifica se e menor ou maior q os valores desejados
    if (num < 45) or (num >55):
        entre += 1
    #verifica o menor numero
    if menor is None or num < menor:
        menor = num
#exibe os resultados
print("\nQuantidade de múltiplos de 3:", multiplo)
print("Quantidade de números fora do intervalo 45 a 55:", entre)
print("Menor número digitado:", menor)

