from bash_executor import run_bash_command


def get_input(prompt):
    return input(prompt).strip()


def buildar():
    tag = get_input("Digite a tag: ")
    service = get_input("Digite o serviço: ")

    comando = f"nebulactl exec build --service-tag {tag} --service {service} --follow"
    run_bash_command(comando)


def deployar():
    service = get_input("Digite o serviço: ")
    tag = get_input("Digite a tag: ")
    cluster = get_input("Digite o cluster: ")
    environment = get_input("Digite o environment: ")
    jiraRelease = get_input("Digite o jira release(tag): ")
    jiraProject = get_input("Digite o jira project: ")

    comando = f"nebulactl exec deploy --service {service} --follow --service-tag {tag} --cluster {cluster} --environment {environment} --config-tag {tag} --jira-release {jiraRelease} --jira-project {jiraProject}"
    run_bash_command(comando)


def criarAcg():
    
    path = get_input("Informe o caminho completo incluindo o arquivo .yml: ")
    
    comando = f"nebulactl create access-control-group --path {path}"
    run_bash_command(comando)
    

def criarDeploymentTemplate():

    path = get_input("Informe o caminho completo incluindo o arquivo .yml: ")

    comando = f"nebula create deployment-template {path}"
    run_bash_command(comando)


def listarDeploymentTemplate():
    service = get_input("Digite o serviço: ")

    comando = f"nebulactl get deployment-templates --service {service}"
    run_bash_command(comando)


def buildGateways(tag):
    comando = f"nebulactl exec build --service-tag {tag} --service cfa-ra-gateways --follow"
    run_bash_command(comando)

def buildJmidas(tag):
    comando = f"nebulactl exec build --service-tag {tag} --service cfa-jmidas --follow"
    run_bash_command(comando)

def deployJmidas(tag, env):
        comando = f"nebulactl exec deploy --service cfa-jmidas --follow --service-tag {tag} --cluster jupiter --environment {env} --config-tag {tag} --jira-release {tag} --jira-project cfa-jmidas"
        run_bash_command(comando)



def deployGateways(tag, env):
    comando = f"nebulactl exec deploy --service cfa-ra-gateways --follow --service-tag {tag} --cluster jupiter --environment {env} --config-tag {tag} --jira-release {tag} --jira-project ra-gateways"
    run_bash_command(comando)