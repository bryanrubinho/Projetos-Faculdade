#10)Escreva um algoritmo que leia o numero de indentificação, as 3 notas obtidas por um aluno
#nas 3 verificações e a média dos exercícios que fazem parte da avaliação, e calcule a média de
#aproveitamento, usando a formula: MA=(nota1+nota2*2+nota3*3+ME)/7


id= int(input("Insira a sua identificação:\n"))
n1 = float(input("Insira a nota 1:\n"))
n2 = float(input("Insira a nota 2:\n"))
n3 = float(input("Insira a nota 3:\n"))

me= n1+n2+n3/3
ma= (n1+n2*2+n3*3+me)/7

if (ma >=90 ):
    print("Seu id é:\n",id,"\n Suas notas são:\n" ,n1,n2,n3,"\n Sua média de exercício é:\n", me,"\n A média de Aproveitamento é:\n",ma, "Aprovado, Conceito: A")
elif (ma >=75) and (ma<90):
    print("Seu id é:\n",id,"\n Suas notas são:\n" ,n1,n2,n3,"\n Sua média de exercício é:\n", me,"\n A média de Aproveitamento é:\n",ma, "Aprovado, Conceito: B")
elif (ma>=60) and (ma<75):
    print("Seu id é:\n",id,"\n Suas notas são:\n" ,n1,n2,n3,"\n Sua média de exercício é:\n", me,"\n A média de Aproveitamento é:\n",ma, "Aprovado, Conceito: C")
elif(ma>=40) and (ma<60):
    print("Seu id é:\n",id,"\n Suas notas são:\n" ,n1,n2,n3,"\n Sua média de exercício é:\n", me,"\n A média de Aproveitamento é:\n",ma, "Reprovado, Conceito: D")
elif(ma<40):
    print("Seu id é:\n",id,"\n Suas notas são:\n" ,n1,n2,n3,"\n Sua média de exercício é:\n", me,"\n A média de Aproveitamento é:\n",ma, "Reprovado, Conceito: E")
    