c=int(input("Insira a temperatura:\n"))

while (c > -5):
    
    f= c*1.8+32
    k= c+273
    print("A temperatura em fahrenheit é:\n %d em Kelvin é:\n %d " % (f, k) )
    c=int(input("Insira a temperatura:\n"))