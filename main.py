from random import choice
import os



def competition(choiceParameter):
    os.system('cls' if os.name == 'nt' else 'clear')
    machineChoice = choice(['pedra', 'papel', 'tesoura'])
    dictChoices = {}
    if machineChoice == 'pedra':
         dictChoices['pedra'] = 1
         dictChoices['papel'] = 2
         dictChoices['tesoura'] = 0
    elif machineChoice == 'papel':
         dictChoices['pedra'] = 0
         dictChoices['papel'] = 1
         dictChoices['tesoura'] = 2
    else:
         dictChoices['pedra'] = 2
         dictChoices['papel'] = 0
         dictChoices['tesoura'] = 1
    if dictChoices[choiceParameter] > dictChoices[machineChoice]:
         print(f"Sua escolha foi {choiceParameter} e a escolha sorteada na máquina foi {machineChoice}\n")
         print("Você venceu!\n")
    elif dictChoices[choiceParameter] < dictChoices[machineChoice]:
         print(f"Sua escolha foi {choiceParameter} e a escolha sorteada na máquina foi {machineChoice}\n")
         print("Você perdeu!\n")
    else:
         print(f"Sua escolha foi {choiceParameter} e a escolha sorteada na máquina foi {machineChoice}\n")
         print("As escolhas foram iguais!\n")
         print("Empate!\n")
                          
    
finish = True

while finish:
        userChoice = input("Escolha pedra, papel ou tesoura ou digite sair para finalizar:\n")
        userChoice = userChoice.lower()
        if  userChoice == 'sair':
            os.system('cls' if os.name == 'nt' else 'clear')
            finish = False
        elif userChoice == 'pedra' or userChoice == 'papel' or userChoice == 'tesoura':
            userChoice = competition(userChoice)
        else:
             os.system('cls' if os.name == 'nt' else 'clear')
             print("Você deve escolher pedra, papel ou tesoura ou a palavra \"Sair\" para poder sair\n")
             
             
print('Fim do programa')