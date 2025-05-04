p_ant= float(input("Insira o preço antigo:\n"))

if (p_ant<50):
    p_novo= p_ant * 1.05
    print("O preço antigo era R$%0.2f, após a alteração ficou R$%0.2f\n" %(p_ant, p_novo))
elif ((p_ant >= 50) and (p_ant < 100)):
    p_novo= p_ant * 1.1
    print("O preço antigo era R$%0.2f, após a alteração ficou R$%0.2f\n" %(p_ant, p_novo))
elif (p_ant>100):
    p_novo= p_ant * 1.15
    print("O preço antigo era R$%0.2f, após a alteração ficou R$%0.2f\n" %(p_ant, p_novo))
if (p_novo <80):
    classificacao = "Barato"
elif ((p_novo>= 80) and (p_novo<120)):
    classificacao = "Normal"
elif ((p_novo>=120) and (p_novo<200)):
    classificacao = "Caro"
elif ((p_novo>200)):
    classificacao="Muito caro"
    

print("Esse produto é considerado %s" %(classificacao))