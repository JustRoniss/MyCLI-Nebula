from menu import menu_principal
from commands import buildGateways, deployGateways

import os
import argparse

def main():
    
    parser = argparse.ArgumentParser(description="Automatizador de comandos do nebula")

    parser.add_argument("--build", help="informe o serviço que irá receber o build")
    parser.add_argument("--tag", help="informe a tag para ser buildada")
    parser.add_argument("--deploy", help="informe o serviço que irá receber o deploy")
    parser.add_argument("--env", help="informe o environment onde será realizado o deploy")

    args = parser.parse_args()


    if args.build and not args.tag:
        parser.error("--tag é obrigatório quando --build é fornecido")

    elif args.deploy and not args.tag:
        parser.error("--tag é obrigatório quando --deploy é fornecido")

    elif args.deploy and not args.env:
        parser.error("--env é obrigatório quando --deploy é fornecido")



    elif (args.build or args.deploy) and args.tag:
        if args.build:
            if(args.build == "cfa-ra-gateways"):
                buildGateways(args.tag)

        if args.deploy:
            if(args.deploy == "cfa-ra-gateways"):
                deployGateways(args.tag, args.env)
        
    else:
        menu_principal()
    

if __name__ == "__main__":
    main()

    # while True:
    #     menu_principal()


