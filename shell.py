import os
class CommandInterpreter:
    def __init__(self):
        self.commands = {"echo": self.handle_echo, "exit": self.handle_exit, "list": self.listcontent, "help": self.list_commands}
        self.isRunning = True
        self.osMode = False 
    
    """
    @param inp 
    @outputs inp
    @Type any 
    """
    def handle_echo(self, inp):
        print(inp)
    
    """
    @outputs commands 
    """
    def list_commands(self):
        for command in self.commands:
            print(command)
            
    """
    @outputs every file and folder in the current directory
    """
    def listcontent(self):
        print(os.listdir())
    
    def handle_exit(self):
        print("Exiting..")
        self.isRunning = False
        
    """
    @param inp 
    @returns inp as a string input stripped from any white space 
    @Type string
    """
    def handle_input(self, inp):
        return input(str(inp.strip(" ")))
        
    """
    This boring function here takes in a paremeter called command and checks 
    if it is a valid command
    @param commands 
    @HandlesError TypeError 
    @Type string
    """
    def validate_command(self, command):
        try:
            if self.commands.get(command):
                self.commands[command]()
            elif command.startswith("echo"):
                output = command[4::].strip()
                self.handle_echo(output)
        except TypeError:
            print("The echo command must have a parameter, dumbo!")
            
commandInterpreter = CommandInterpreter()
while commandInterpreter.isRunning:
    command = commandInterpreter.handle_input("> ").lower()
    commandInterpreter.validate_command(command)
    
    
