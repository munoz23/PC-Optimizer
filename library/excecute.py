from library.powerShell import PowerShell
import os,shutil,json
from getpass import getuser
from library.windowsLocalMachine import Registry


class Commands:
    @staticmethod
    def listCommands()-> list:
        ls = [{ 
                'network optimizer':["Set-NetTCPSetting -SettingName internet -AutoTuningLevelLocal normal","Set-NetTCPSetting -SettingName internet -ScalingHeuristics disabled","netsh int tcp set supplemental internet congestionprovider=CUBIC","Set-NetOffloadGlobalSetting -ReceiveSegmentCoalescing disabled","Set-NetOffloadGlobalSetting -ReceiveSideScaling enabled","Disable-NetAdapterLso -Name *","Enable-NetAdapterChecksumOffload -Name *","Set-NetTCPSetting -SettingName internet -EcnCapability disabled","Set-NetOffloadGlobalSetting -Chimney disabled","Set-NetTCPSetting -SettingName internet -Timestamps disabled","Set-NetTCPSetting -SettingName internet -MaxSynRetransmissions 2","Set-NetTCPSetting -SettingName internet -NonSackRttResiliency disabled","Set-NetTCPSetting -SettingName internet -InitialRto 2000","Set-NetTCPSetting -SettingName internet -MinRto 300","netsh interface ipv4 set subinterface \"Ethernet\" mtu=1500 store=persistent","netsh interface ipv6 set subinterface \"Ethernet\" mtu=1500 store=persistent","netsh interface ipv4 set subinterface \"Wi-Fi\" mtu=1500 store=persistent","netsh interface ipv6 set subinterface \"Wi-Fi\" mtu=1500 store=persistent"]
            },
            {
                'windows activation':["slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX","slmgr.vbs /skms kms8.msguides.com","slmgr.vbs /ato"]
            },
            {
                'Windows Optimizer':["powercfg /s 381b4222-f694-41f0-9685-ff5bb260df2e","powercfg /d 010fd358-aaf5-4687-a504-26218b58eab8","powercfg /duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61 010fd358-aaf5-4687-a504-26218b58eab8","powercfg /changename 010fd358-aaf5-4687-a504-26218b58eab8 'Optimized Ultimate Performance'","powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 54533251-82be-4824-96c1-47b60b740d00 893dee8e-2bef-41e0-89c6-b55d0929964c 0","powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 54533251-82be-4824-96c1-47b60b740d00 893dee8e-2bef-41e0-89c6-b55d0929964c 0","powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 7516b95f-f776-4464-8c53-06167f40cc99 3c0bc021-c8a8-4e07-a973-6b14cbcb2b7e 900","powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 7516b95f-f776-4464-8c53-06167f40cc99 3c0bc021-c8a8-4e07-a973-6b14cbcb2b7e 600","powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 238c9fa8-0aad-41ed-83f4-97be242c8f20 29f6c1db-86da-48c5-9fdb-f2b67b1f44da 1800","powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 238c9fa8-0aad-41ed-83f4-97be242c8f20 29f6c1db-86da-48c5-9fdb-f2b67b1f44da 900","powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 238c9fa8-0aad-41ed-83f4-97be242c8f20 94ac6d29-73ce-41a6-809f-6363ba21b47e 0","powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 238c9fa8-0aad-41ed-83f4-97be242c8f20 94ac6d29-73ce-41a6-809f-6363ba21b47e 0","powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 19cbb8fa-5279-450e-9fac-8a3d5fedd0c1 12bbebe6-58d6-4636-95bb-3217ef867c1a 0","powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 19cbb8fa-5279-450e-9fac-8a3d5fedd0c1 12bbebe6-58d6-4636-95bb-3217ef867c1a 3","powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 1","powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 2a737441-1930-4402-8d77-b2bebba308a3 48e6b7a6-50f5-4782-a5d4-53bb8f07e226 1","powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 501a4d13-42af-4429-9fd1-a8218c268e20 ee12f906-d277-404b-b6da-e5fa1a576df5 0","powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 501a4d13-42af-4429-9fd1-a8218c268e20 ee12f906-d277-404b-b6da-e5fa1a576df5 2","powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 9596fb26-9850-41fd-ac3e-f7c3c00afd4b 10778347-1370-4ee0-8bbd-33bdacaade49 1","powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 9596fb26-9850-41fd-ac3e-f7c3c00afd4b 10778347-1370-4ee0-8bbd-33bdacaade49 0","powercfg /setacvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 9596fb26-9850-41fd-ac3e-f7c3c00afd4b 34c7b99f-9a6d-4b3c-8dc7-b6693b78cef4 0","powercfg /setdcvalueindex 010fd358-aaf5-4687-a504-26218b58eab8 9596fb26-9850-41fd-ac3e-f7c3c00afd4b 34c7b99f-9a6d-4b3c-8dc7-b6693b78cef4 2","powercfg /s 010fd358-aaf5-4687-a504-26218b58eab8","powercfg /hibernate off","Disable-MMAgent -MemoryCompression","bcdedit /set disabledynamictick yes","bcdedit /set useplatformclock no"]
            },
            {
                'disabled updates':[["HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU\\AutoInstallMinorUpdates",0,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU\\NoAutoUpdate",1,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\WindowsStore\\AutoDownload",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\SetAutoRestartNotificationDisable",1,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\Maps\\AutoDownloadAndUpdateMapData",0,4]]
            },
            {
                'disabled telemetrys windows':[["HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection\\AllowTelemetry",0,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\TabletPC\\PreventHandwritingDataSharing",1,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\Psched\\NonBestEffortLimit",0,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\DiagTrack\\Start",4,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\dmwappushservice\\Start",4,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\diagsvc\\Start",4,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\diagnosticshub.standardcollector.service\\Start",4,4]]
            },
            {
                'cleanup':[["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Active Setup Temp Folders\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\BranchCache\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\D3D Shader Cache\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Delivery Optimization Files\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Diagnostic Data Viewer database files\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Downloaded Program Files\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Feedback Hub Archive log files\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Internet Cache Files\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Language Pack\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Old ChkDsk Files\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\RetailDemo Offline Content\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Setup Log Files\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\System error memory dump files\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\System error minidump files\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Temporary Files\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Temporary Setup Files\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Thumbnail Cache\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Update Cleanup\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\User file versions\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Windows Defender\\StateFlags0000",2,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VolumeCaches\\Windows Error Reporting Files\\StateFlags0000",2,4]]
            },
            {
                'windows registry optimization':[["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\AxInstSV\\Start",4,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\AppMgmt\\Start",4,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\CertPropSvc\\Start",4,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\PeerDistSvc\\Start",4,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\SCPolicySvc\\Start",4,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\SNMPTRAP\\Start",4,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\WebClient\\Start",4,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\WinRM\\Start",4,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\WerSvc\\Start",4,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\PNRPsvc\\Start",4,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\p2psvc\\Start",4,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\p2pimsvc\\Start",4,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\SysMain\\DelayedAutoStart",1,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\ServiceProvider\\LocalPriority",4,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\ServiceProvider\\HostsPriority",5,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\ServiceProvider\\DnsPriority",6,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\ServiceProvider\\NetbtPriority",7,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\QoS\\Do not use NLA","1",1],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\LanmanServer\\Parameters\\Size",3,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\MaxUserPort",65534,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\TcpTimedWaitDelay",30,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters\\DefaultTTL",64,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerThrottling\\PowerThrottlingOff",1,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\FileSystem\\NtfsDisable8dot3NameCreation",1,4],["HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\LargeSystemCache",1,4],["HKEY_CURRENT_USER\\Control Panel\\Desktop\\HungAppTimeout","4000",1],["HKEY_CURRENT_USER\\Control Panel\\Desktop\\WaitToKillAppTimeout","5000",1],["HKEY_CURRENT_USER\\Control Panel\\Desktop\\MenuShowDelay","0",1],["HKEY_CURRENT_USER\\Control Panel\\Desktop\\ForegroundLockTimeout",200000,4],["HKEY_CURRENT_USER\\Control Panel\\Desktop\\AutoEndTasks","1",1],["HKEY_CURRENT_USER\\Control Panel\\Mouse\\MouseHoverTime","100",1],["HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\BackgroundAccessApplications\\GlobalUserDisabled",1,4],["HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\DesktopProcess",1,4],["HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\GameDVR\\AppCaptureEnabled",0,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Dfrg\\BootOptimizeFunction\\Enable","Y",1],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Max Cached Icons",2000,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\NetworkThrottlingIndex",4294967295,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\SystemResponsiveness",0,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games\\Affinity",0,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games\\Background Only","False",1],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games\\Clock Rate",10000,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games\\GPU Priority",8,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games\\Priority",6,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games\\Scheduling Category","High",1],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Multimedia\\SystemProfile\\Tasks\\Games\\SFIO Priority","High",1],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_MAXCONNECTIONSPERSERVER\\explorer.exe",10,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Internet Explorer\\Main\\FeatureControl\\FEATURE_MAXCONNECTIONSPER1_0SERVER\\explorer.exe",10,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\Psched\\NonBestEffortLimit",0,4],["HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows\\Psched\\TimerResolution",0,4],["HKEY_CURRENT_USER\\System\\GameConfigStore\\GameDVR_Enabled",0,4],["HKEY_CURRENT_USER\\System\\GameConfigStore\\GameDVR_FSEBehavior",2,4]]
            },
            {
                'windows Defrag':["defrag C: /U /V "]
            }
            ]
        return ls    



class Option:
    @staticmethod
    def delect_file_or_folder(type,root) -> None:
        try:
            if type == 'file':
                os.remove(root)
            elif type == 'folder':
                shutil.rmtree(root)
        except OSError as e:
            pass
    @staticmethod
    def optimizer_network() -> None:
        commands =Commands()
        ls =commands.listCommands()

        print('* Optimizando network')
        try:
            with PowerShell.execute_commands(ls[0]['network optimizer']) as f:
                while f.poll() is None:
                    line = f.stdout().readline().encode('utf8')
                    print("desde excute:"+f.decode('utf-8'))
        except Exception as e:
            print(e)            
        print('- Proceso terminado')

    @staticmethod
    def windows_optimizer()-> None:
        try:
            commands = Commands()
            wp = commands.listCommands()
            print('Limpiando Registros')

            Registry.write_keys(wp[6]['windows registry optimization'])
        
        
            print('Limpiando Disco')
            PowerShell.execute_commands(wp[2]['Windows Optimizer'])
            print('Desea desfragmentar el Disco? (si o no)')
            response = str(input('*-Ingrese si o no: '))
            if response.lower() == 'si':
                print('*-Defragmentando Disco')
                print('*-Por Favor No Apague su equipo hasta que termine le proceso gracias')
                PowerShell.execute_commands_real_time(['defrag C: /U /V '])   
            print('*-Proceso finalizado')
        except Exception as e:
            print(e)
            input()  
    @staticmethod
    def desabilite_telemetry() -> None:
        commands = Commands()
        dt = commands.listCommands()
        print('*-Desactivando la Telemetria de Windows')
        Registry.write_keys(dt[4]['disabled telemetrys windows'])
        print('*-Las telemetrias se desactivaron correctamente')
    @staticmethod
    def disabled_updates() -> None:
        commands = Commands()
        ls = commands.listCommands()
        print('Desabilitando Actualizacion de Windows')
        Registry.write_keys(ls[3]['disabled updates'])
    @staticmethod
    def active_windows() -> None:
        commands = Commands()
        aw = commands.listCommands()
        print('Activando Windows')
        PowerShell.execute_commands(aw[1]['windows activation'])
        print('Windows Activado, necesita de reinciar su equipo')
    @staticmethod
    def delect_files_trash() -> None:
        try:
            root_list =["C:/Windows/Temp","C:/Users/"+getuser()+"/AppData/Local/Temp","'C:/Windows/prefetch"]
            for ruta in root_list:
                for root, dirs, files in os.walk(ruta,topdown=False):
                    for name in files:
                        if os.path.exists(ruta+'\\'+name):
                            Option.delect_file_or_folder(type='file',root=ruta+'/'+name)
                            print('Archivos Limpiados:'+name)
                            
                    for folder in dirs:
                        if os.path.exists(ruta+'\\'+folder):
                            Option.delect_file_or_folder(type='folder',root=ruta+'/'+name)
                            print('Carpetas Limpiadas:'+folder)
        except Exception as e:
            print(e)
                      
        




        


