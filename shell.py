import os

"""
AuthorInformation
     name (GitHub Username): DumbestPerson224
     Repo (GitHub): https://github.com/DumbestPerson224/LinuxShellManager
"""

class CommandInterpreter:
    def __init__(self):
        
        """Map commands to the corresponding method"""
        self.commands = {"echo": self.handle_echo, "exit": self.handle_exit, "list": self.listcontent, "help": self.list_commands}

        "`isRunning` and `osMode` must only be booleans"
        self.isRunning = True
        self.osMode = False 
        
    """
    FunctionInformation
          Does: This function handles output
          Parameter (any): inp 
          Outputs (any): inp
          Type (string): Do not change
          name (handle_echo): Do not change
    """
    def handle_echo(self, inp):
        print(inp)
    
    """
    Function Information
          Outputs (string): commands 
          FunctionName (Do not change): list_commands
          Parameters (None): Do not change 
    """
    def list_commands(self):
        for command in self.commands:
            print(command)
            
    """
    FunctionInformation
          Outputs (no type): every file and folder in the current directory
          Parameters (None): Do not change
          FunctionName listcontent
    """
    def listcontent(self):
        for filesAndFolders in os.listdir():
            print(filesAndFolders)

    """
    FunctionInformation
          name (handle_exit): Do not change
          Outputs (Do not change): Exitting.
          isRunning (Do not change): False
    """
    def handle_exit(self):
        print("Exiting..")
        self.isRunning = False
        
    """
    FunctionInformation
          name (handle_input): Do not change  
          Parameter inp 
          Returns inp as a string input stripped from any white space 
          Type (Do not change): any    
    """
    def handle_input(self, inp):
        return input(str(inp.strip(" ")))
        
    """
    FunctionInformation:
          name (validate_input): Do not change name 
          type (str): Do not change type         
          info (This boring function here takes in a paremeter called command and checks if it is a valid command): The information of the function
          parameter (string): command
          KeyError (Not a valid command): The command in all capitals is not a valid command 
          TypeError (No parameter provided): The command (command in original casing) must have a parameter
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
    