from ftplib import FTP
import os,sys,json
import pathlib
from xmlrpc.client import Boolean



class VersionLevel:
    @staticmethod
    def version_now()->str:
        return '1.0.2'
    @staticmethod
    def versionServer() -> str:
        try:
            ftp = FTP('ftp.webcindario.com')
            ftp.login('netcolombiaclear','memorias23')  
            ftp.cwd('log_versiones')
            with open('versiones_cliente.json','r') as f:
                version = json.loads(f.read())
                f.close()
                ftp.quit()
                return version

        except Exception as e:
            f.close()
            return "error" 
                   

class Updates:
    @staticmethod
    def update_version()->Boolean:
        try:
            versionNow = VersionLevel.version_now()
            version = VersionLevel.versionServer()
            print(version['versiones_actual']['version']) 
            if version['versiones_actual']['version'] == versionNow:
                return False
            if version == 'error':
                print('Hay un problema con el servidor')    
            else:
                return True       
        except Exception as e:
            return False
    @staticmethod
    def download_update()-> None:
        ftp = FTP('ftp.webcindario.com')
        ftp.login('netcolombiaclear','memorias23')
        ftp.cwd('versiones')
        remoteFile=f'CleanUp_{VersionLevel.versionServer()}.json'
        remoteFileOuput=f'CleanUp_{VersionLevel.versionServer()}.exe'
        with open(remoteFileOuput,'wb') as file:
            ftp.retrbinary(f"RETR {remoteFile}",file.write)
            file.close()
        ftp.quit()    
               
            #print(str(e))    