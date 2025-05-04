#1) Elaborar um programa que solicita varias temperaturas em graus Celsius. Para cada
#temperatura inserida, o programa deve converter para graus Fahrenheit e Kelvin e mostrar na
#tela. O programa termina quanto a temperatura inserida for menor que -5. 

c=float(input("Insira a temperatura:\n"))
while (c > -5):
    
    f= c*1.8+32
    k= c+273
    print("A temperatura em fahrenheit é:\n %d em Kelvin é:\n %d " % (f, k) )
    c=float(input("Insira a temperatura:\n"))