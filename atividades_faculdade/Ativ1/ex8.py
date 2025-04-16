#8)Elaborar um programa que dados o tamanho de um arquivo (em bits), bem como a velocidade
#da conexão (em bits por segundo), informe o tempo necessário para o download do arquivo.

#entrada
ve_bits= float(input("Insira o tamanho do arquivo em bits\n"))
ve_internet=float(input("Inserir a velocidade da internet\n"))
#processo
ve_download = ve_bits/ve_internet
#saida
print("A velocidade de download é:", ve_download, "seg")
