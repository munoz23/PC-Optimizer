
import subprocess
import sys
from typing import Any, List

class PowerShell:
    def __enter__(self):
        return sys.stdin('hola') 
    @staticmethod
    def execute_command(command: str)-> None:
        if command is None :
            raise ValueError('El comando no puede estar vacio')
        process = subprocess.run(['powershell',command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, capture_output=False,universal_newlines=True)
        
        if process.returncode !=0:
            pass
        else:
            pass
        return process
    
    @staticmethod
    def execute_commands(commands: list)-> str:
        if commands == None or commands == '':
            raise ValueError('El comando no puede estar vacio')   
        for command in commands:
            print(command,file=sys.stdout)
            process =PowerShell.execute_commands_real_time(command=command)
            return process
    @staticmethod
    def execute_commands_real_time(command: str):
        if command == None or command == '':
            raise ValueError('El comando no puede estar vacio')
        return subprocess.Popen(command,shell=True ,stdout =subprocess.PIPE,stderr=subprocess.PIPE, universal_newlines=True)
                           
                    