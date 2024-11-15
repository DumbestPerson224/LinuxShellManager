import os
class CommandInterpreter:
    def __init__(self):
        self.commands = {"echo": self.handle_echo, "exit": self.handle_exit, "list": self.listcontent, "help": self.list_commands}
        self.isRunning = True
        self.osMode = False 
    """
    Parameter: inp 
    Outputs: inp
    Type: any 
    """
    def handle_echo(self, inp):
        print(inp)
    
    """
    Outputs: commands 
    """
    def list_commands(self):
        for command in self.commands:
            print(command)
            
    """
    Outputs: every file and folder in the current directory
    """
    def listcontent(self):
        print(os.listdir())
    
    def handle_exit(self):
        print("Exiting..")
        self.isRunning = False
        
    """
    Parameter: inp 
    Returns: inp as a string input stripped from any white space 
    Type: string
    """
    def handle_input(self, inp):
        return input(str(inp.strip(" ")))
        
    """
    This boring function here takes in a paremeter called command and checks 
    if it is a valid command
    Parameter: commands 
    HandlesError: TypeError 
    Type: string
    ErrorHandleOutput: The {command} must have a parameter
    """
    def validate_command(self, command):
        try:
            self.commands[command]()
        except KeyError:
            if not command.startswith("echo"):
                print(f"{command.upper()} is not a valid command!")
            else:
                self.handle_echo(command[4::].strip())
        except TypeError:
            print(f"The {command} command must have a parameter.")
            
commandInterpreter = CommandInterpreter()
while commandInterpreter.isRunning:
    command = commandInterpreter.handle_input("> ").lower()
    commandInterpreter.validate_command(command)
    
    
