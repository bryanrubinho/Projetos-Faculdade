n1= float(input("Insira a nota 1:\n"))
n2= float(input("Insira a nota 2:\n"))
n3= float(input("Insira a nota 3:\n"))
m_f= (n1+n2+n3)/3

if m_f>6:
    print("Aprovado")
elif m_f<=5:
    print("Recuperacao") 
elif m_f<5:
    print("Reprovado")