from menus.menu_principal import menu_principal
from commands.comandos_especificos import buildGateways, buildJmidas, buildHolmes,  deployGateways, deployJmidas, deployHolmes
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Automatizador de comandos do nebula")
    parser.add_argument("--build", help="informe o serviço que irá receber o build")
    parser.add_argument("--tag", help="informe a tag para ser buildada")
    parser.add_argument("--deploy", help="informe o serviço que irá receber o deploy")
    parser.add_argument("--env", help="informe o environment onde será realizado o deploy")
    return parser.parse_args()

def validate_args(args, parser):
    if (args.build or args.deploy) and not args.tag:
        parser.error("--tag é obrigatório quando --build ou --deploy são fornecidos")
    if args.deploy and not args.env:
        parser.error("--env é obrigatório quando --deploy é fornecido")

def execute_command(args):
    commands = {
        "cfa-ra-gateways": {
            "build": buildGateways,
            "deploy": deployGateways
        },
        "cfa-jmidas": {
            "build": buildJmidas,
            "deploy": deployJmidas
        },
        "cfa-holmes": {
            "build": buildHolmes,
            "deploy": deployHolmes
        },
    }

    if args.build:
        command = commands.get(args.build, {}).get("build")
        if command:
            command(args.tag)

    if args.deploy:
        command = commands.get(args.deploy, {}).get("deploy")
        if command:
            command(args.tag, args.env)

def main():
    args = parse_args()
    validate_args(args, argparse.ArgumentParser())
    
    if args.build or args.deploy:
        execute_command(args)
    else:
        menu_principal()

if __name__ == "__main__":
    main()
