from commands.comandos_genericos import criarDeploymentTemplate, listarDeploymentTemplate
import os


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
