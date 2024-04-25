import subprocess
import shlex
import time
import os

def run_bash_command(command):
    try:
        subprocess.run(shlex.split(command), check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando. \n Stack Strace: \n {e}")
        time.sleep(10)
        os.system("clear")
        