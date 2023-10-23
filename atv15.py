# Exercício Python 15: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo. 
#DICA: PESQUISE E ENTENDA SOBRE DESIGUALDADE TRIANGULAR
reta1 = float(input("digite um comprimento: "))
reta2 = float(input("digite um comprimento: "))
reta3 = float(input("digite um comprimento: "))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print("É um triangulo")
else:
    print("Não é um triangulo")