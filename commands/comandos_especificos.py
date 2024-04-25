from bash_executor import run_bash_command
import time

def buildGateways(tag):
    comando = f"nebulactl exec build --service-tag {tag} --service cfa-ra-gateways --follow"
    run_bash_command(comando)


def deployGateways(tag, env):
    comando = f"nebulactl exec deploy --service cfa-ra-gateways --follow --service-tag {tag} --cluster jupiter --environment {env} --config-tag {tag} --jira-release {tag} --jira-project ra-gateways"
    run_bash_command(comando) 

def buildJmidas(tag):
    comando = f"nebulactl exec build --service-tag {tag} --service cfa-jmidas --follow"
    run_bash_command(comando)

def deployJmidas(tag, env):
        comando = f"nebulactl exec deploy --service cfa-jmidas --follow --service-tag {tag} --cluster jupiter --environment {env} --config-tag {tag} --jira-release {tag} --jira-project cfa-jmidas"
        run_bash_command(comando)

def buildHolmes(tag):
     comando = f"nebulactl exec build --service-tag {tag} --service cfa-holmes --follow"
     print("Comando gerado: " + comando)
     time.sleep(3)
     run_bash_command(comando)


def deployHolmes(tag, env):
     comando = f"nebula exec deploy --service cfa-holmes --service-tag {tag} --config-tag {tag} --cluster jupiter --follow --environment {env}"
     run_bash_command(comando)
