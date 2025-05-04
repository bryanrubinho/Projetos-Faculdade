#18) Elaborar um programa que leia o tempo de duração de um evento em uma fábrica expressa
#em segundos e mostre-o expresso em horas, minutos e segundos.

#entrada
d = int(input("Insira o tempo de duração em segundos:\n"))
#processo
hora= d/60
h=hora/60
m= h*60
s= m*60
#saida
print("A duração do evento foi:\n", h,"horas", m,"minutos", s ,"segundos")
