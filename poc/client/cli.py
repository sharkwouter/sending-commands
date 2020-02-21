from poc.client.base import ClientBase
import subprocess


class ClientCli(ClientBase):

    def execute_command(self, command) -> bool:
        if not self.__execute_command(command.command):
            return False
        return True

    def execute_rollback(self, command) -> bool:
        return self.__execute_command(command.rollback)

    def __execute_command(self, command):
        print(command)
        if not command[0]:
            return True
        try:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            process.wait()
            if process.returncode == 0:
                return True
        except (FileNotFoundError, PermissionError) as exc:
            print(exc)
        except Exception as exc:
            print("Uncaught exception: {}".format(exc))
        return False
