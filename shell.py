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
          Type (str): Do not change
          name (handle_echo): Do not change
    """
    def handle_echo(self, inp):
        print(inp)
    
    """
    Function Information
          Outputs (string): commands 
          FunctionName list_commands
          Parameters (None): Do not change 
          name (list_commands): Do not change
    """
    def list_commands(self):
        for command in self.commands:
            print(command)
            
    """
    FunctionInformation
     Outputs (no type): every file and folder in the current directory
     name listcontent
    """
    def listcontent(self):
        print(os.listdir())

    """
    FunctionInformation
     name (handle_exit): Do not change
     Outputs Exitting.
     isRunning (Do not change): False
    """
    def handle_exit(self):
        print("Exiting..")
        self.isRunning = False
        
    """
  
    FunctionInformation
          name (handle_input): Do not change  
          Parameter: inp 
          Returns: inp as a string input stripped from any white space 
          Type: string

    """
    def handle_input(self, inp):
        return input(str(inp.strip(" ")))
        
    """


    FunctionInformation:
          name (validate_input): Do not change name 
          type (str): Do not change type         
          info (This boring function here takes in a paremeter called command and checks if it is a valid command): The information of the function
          parameter (str): command
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

    

<<<<<<< HEAD
     """
     Convert the parameter to a lowercase
     """
     @staticmethod 
     def to_lower(inp):
          return inp.lower()
     
     """ 
     Handle exiting
     """
     @staticmethod
     def handle_exit():
          global running
          leave = input("Exit? ")
          if executor.to_lower(leave) == "y": 
               print("Exiting...")
               running = False

     """
     Handle input by normalizing it and getting it
     """
     @staticmethod
     def handle_input(inp):
          return executor.normalize_input(input(inp))

     """
     Output all of the commands from the commands dictionary
     """
     @staticmethod
     def output_commands():
          for i in commands:
               print(i)
     """
     List folders in the current directory
     """
     def list_dir():
          for i in os.listdir():
               if os.path.isdir(i):
                    print(i)
               else:
                    continue

     """
     Make the parameter a capital 
     """
     @staticmethod
     def capitalize(value):
          return value.capitalize()

     @staticmethod
     def list_file():
          for i in os.listdir():
               if os.path.isfile(i):
                    print(i)
               else:
                    continue

     def clear_screen():
          os.system("clear")

     def os_mode():
          global osMode
          if osMode == True:
               osMode = False
          else:
               osMode = True

     def remove():
          item = executor.handle_input("Enter the item location > ")
          if os.path.exists(item):
               if os.path.isdir(item):
                    os.removedirs(item)
               else:
                    os.remove(item)
          else:
               print(f"{item.capitalize()} does not exist!")
     def list_use():
          command = executor.handle_input("Enter a command > ")
          if command.lower() in does:
               print(does.get(command.lower()))
          else:
               print(f"{command.capitalize()} does not exist!")

     def exists():
          item = executor.handle_input("Enter > ")
          if os.path.exists(item):
               print("That exists!")
          else:
               print("That does not exist!")

     def execute_interpreter():
          file = executor.normalize_input(executor.handle_input("Enter a repository > "))
          if os.path.exists(file):
               os.system(f"python3 {file}")
          else:
               os.system("python3")
     
     def set_admin():
          global admin
          if admin == False:
               os.system("sudo -s")
               print("Admin mode entered")
               admin = True 
          else:
               os.system("exit")
               print("Admin mode exited!")
               admin = False

commands = {  
     "exit": executor.handle_exit,
     "help": executor.output_commands,
     "listdir": executor.list_dir,
     "listfile": executor.list_file,
     "clear":  executor.clear_screen,
     "osmode": executor.os_mode,
     "delete": executor.remove,
     "listuse": executor.list_use,
     "exists": executor.exists,
     "python": executor.execute_interpreter,
     "admin": executor.set_admin,
}

does = {
     "exit": "This command exits the terminal",
     "osmode": "This command allows you to use the shell of your OS",
     "listfile": "This command lists all of the files in the current directory",
     "listdir": "This command lists all of the directories in the current location",
     "clear": "This command clears the screen",
     "exists": "This command checks if a file or directory exists",
     "listuse": "This command lists the usages of the inputted command",
}

if __name__ == '__main__':
  while running: 
     try:
          command = executor.handle_input("> ")
          if commands.get(command):
              commands[command]()
          else:
               if osMode == True:
                    os.system(command)
               else:
                    print(f"{executor.capitalize(command)} is not a valid command")
                    print("Type `help` to see the available commands")
     except KeyboardInterrupt:
          executor.handle_exit()
=======
>>>>>>> 8a9f76c25c112e40a2560337c2597667e0a0a4d4