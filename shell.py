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
  
    def handle_echo(self, inp):      
        """
        FunctionInformation
            Does: This function handles output
            Parameter (any): inp 
            Outputs (any): inp
            Type (string): Do not change
            name (handle_echo): Do not change
        """
        print(inp)
    
    
    def list_commands(self):
        """
        Function Information
          Outputs (string): commands 
          FunctionName (Do not change): list_commands
          Parameters (None): Do not change 
        """
        for command in self.commands:
            print(command)
            
    def listcontent(self):
        """
        FunctionInformation
            Outputs (no type): every file and folder in the current directory
            Parameters (None): Do not change
            FunctionName listcontent
        """
         
        for filesAndFolders in os.listdir():
            print(filesAndFolders)

    
    def handle_exit(self):
        """
        FunctionInformation
            name (handle_exit): Do not change
            Outputs (Do not change): Exitting.
            isRunning (Do not change): False
        """
        print("Exiting..")
        self.isRunning = False
        
   
    def handle_input(self, inp):     
        """
        FunctionInformation
            name (handle_input): Do not change  
            Parameter inp 
            Returns inp as a string input stripped from any white space 
            Type (Do not change): any    
        """
        return input(str(inp.strip(" ")))
        
   
    def validate_command(self, command) -> str:
        """
        FunctionInformation:
            name (validate_input): Do not change name 
            type (str): Do not change type         
            info (This boring function here takes in a paremeter called command and checks if it is a valid command): The information of the function
            parameter (string): command
            NoValidCommand (output): (The user input in caps) is not valid
        """
        if command in self.commands and not command.startswith("echo"):
            self.commands[command]()
        elif command.startswith("echo"):
            self.commands[command[4::].strip()]
        else:
            print(f"{command.upper()} is not valid")
commandInterpreter = CommandInterpreter()
while commandInterpreter.isRunning:
    command = commandInterpreter.handle_input("> ").lower()
    commandInterpreter.validate_command(command)
