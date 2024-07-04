import winreg
from library.powerShell import PowerShell
from library.parserLocalMachine import ParserMachine


class Registry:
    @staticmethod
    def write_keys(keys: list[tuple[str, int, any]]):
        for key in keys:
            Registry.write_key(key[0], key[1], key[2])

    @staticmethod
    def write_key(fullpath: str, value: str, value_type: int) -> None:
        root, path, key = ParserMachine.parse_registry_path(fullpath)

        try:
            opened_key = winreg.CreateKeyEx(root, path, 0, winreg.KEY_ALL_ACCESS)

            winreg.SetValueEx(opened_key, key, 0, value_type, value)
        except OSError:
            return

    @staticmethod
    def delete_keys(keys: list[tuple[str, int, any]]):
        for key in keys:
            Registry.delete_key(key[0])

    @staticmethod
    def delete_key(fullpath: str) -> None:
        root, path, key = ParserMachine.parse_registry_path(fullpath)

        try:
            opened_key = winreg.CreateKeyEx(root, path, 0, winreg.KEY_ALL_ACCESS)

            winreg.DeleteValue(opened_key, key)
        except OSError:
            return

    @staticmethod
    def backup() -> None:
        PowerShell.execute_command("Enable-ComputerRestore -Drive 'C:\'")
        PowerShell.execute_command("Checkpoint-Computer -Description NetColombiaOptimizer -RestorePointType MODIFY_SETTINGS")

    @staticmethod
    def restore() -> None:
        PowerShell.execute_command("Rstrui.exe")