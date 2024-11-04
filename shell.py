import os
running = True 
osMode = False 
admin = False 

class executor:
     
     """
     Strip out any spacing and make the input lowercase
     """
     @staticmethod 
     def normalize_input(text):
          return executor.to_lower(executor.strip(text, " "))

     """
     Strip out the text
     """
     @staticmethod
     def strip(text, value):
          return str(text).strip(value)
     
     """
     Convert something to a string
     """
     @staticmethod
     def to_string(text):
          return str(text)

     """
     Convert num into a float
     """
     @staticmethod
     def to_float(num):
          return float(num)
     
     """
     Convert the parameter to an integer
     """
     @staticmethod
     def to_int(num):
          return int(num)

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