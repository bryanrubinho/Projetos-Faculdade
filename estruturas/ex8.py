peso= float(input("Digite o seu peso (Kg):\n"))
altura = float(input("Digite sia altura(m):\n"))

imc = peso / (altura**2)

print("Seu imc é:" % imc)

if (imc <18.5):
    print("Condição a baixo do peso")
elif 18.5<= imc < 25:
    print("Condição peso normal")
elif 25 <= imc <30:
    print("Condição acima do peso")
else:
    print("Condição obeso")
    