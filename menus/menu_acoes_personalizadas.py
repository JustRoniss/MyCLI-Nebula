from commands.comandos_genericos import buildar, deployar, criarAcg, criarDeploymentTemplate
import os

def menu_acoes_personalizadas():
    os.system("clear")
    print("Menu de ações personalizadas - Nebula")
    print("1) Realizar build")
    print("2) Realizar deploy")
    print("3) Criar Deployment Template")
    print("4) Criar acg")
    print("0) Sair")
    print()

    escolha = input("Digite sua opção (1-4): ")

    if escolha == '1':
        buildar()
    elif escolha == '2':
        deployar()
    elif escolha == '3':
        criarDeploymentTemplate()  
    elif escolha == '4':
        criarAcg()
    elif escolha == '0':
        exit()
    else:
        print("Opção inválida!")