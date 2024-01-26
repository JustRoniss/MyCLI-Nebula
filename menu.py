from commands import buildar, deployar, criarDeploymentTemplate, listarDeploymentTemplate
import os




def menu_principal():
    os.system("clear")
    print("O que quer fazer hoje?")
    print("1) Ações rápidas")
    print("2) Ações personalizadas")
    print("3) Deployment templates")
    print("4) ACG")
    print("0) Sair\n")

    escolha = input("Digite sua opção (1-4): ")


    if escolha == '1':
        print("Em desenvolvimento")
    elif escolha == '2':
        menu_acoes_personalizadas()
    elif escolha == '3':
        menu_deployment() 
    elif escolha == '4':
        print("Em desenvolvimento")   
    elif escolha == '0':
        exit()
    else:
        print("Opção inválida!")


def menu_acoes_personalizadas():
    os.system("clear")
    print("Menu de ações personalizadas - Nebula")
    print("1) Realizar build")
    print("2) Realizar deploy")
    print("3) Criar acg")
    print("0) Sair")
    print()

    escolha = input("Digite sua opção (1-4): ")

    if escolha == '1':
        buildar()
    elif escolha == '2':
        deployar()
    elif escolha == '3':
        print("Em desenvolvimento")    
    elif escolha == '0':
        exit()
    else:
        print("Opção inválida!")


def menu_acoes_rapidas():
    print("Em desenvolvimento")

def menu_deployment():
    os.system("clear")
    print("Menu de Deployment Template - Nebula")
    print("1) Listar deployment template")
    print("2) Criar deployment template")
    print("3) Apagar deployment template")
    print("4) Sair")


    escolha = input("Digite sua opção (1-3): ")

    if escolha == '1':
        listarDeploymentTemplate()
    elif escolha == '2':
        criarDeploymentTemplate()
    elif escolha == '3':
        print("Em desenvolvimento")
    elif escolha == '4':
        exit()
