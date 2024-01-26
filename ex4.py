import random
from unittest import result

done = False

while not done:
    print("O que você deseja fazer?")
    print("1. Adivinhar o numero")
    print("2.Sair")
    
    choice = input(">")
    
    if choice == "1":
        print("=====Adivinhe um numero de 1 a 10========\n")
        number = int (input("Digite um numero de 1 a 10\n"))
        result = random.randint(1,10)
        if number == result:
            print ("Parábens. Você acertou!")
        else:
            print(f"Tente novamente. O número sorteado foi {result}")
    elif choice == "2":
        done = True
    else:
        print("Opção Inválida. Escolha uma opção entre 1 e 2")