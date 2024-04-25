
from menus import menu_acoes_personalizadas, menu_deploymentTemplate, menu_acg
import os

def menu_principal():
    os.system("clear")
    print("O que quer fazer hoje?")
    print("1) Ações personalizadas")
    print("2) Deployment templates")
    print("3) ACG")
    print("0) Sair\n")

    escolha = input("Digite sua opção (1-4): ")


    if escolha == '1':
        menu_acoes_personalizadas()
    elif escolha == '2':
        menu_deploymentTemplate() 
    elif escolha == '3':
        menu_acg()   
    elif escolha == '0':
        exit()
    else:
        print("Opção inválida!")







