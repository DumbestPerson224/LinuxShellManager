import os 
if __name__ == '__main__':
    file = input("Enter a file > ")
    if os.path.exists(file) and os.path.isfile(file):
        os.system(f"gcc {file} -O3 -o {file.strip(".c")}.o")
    else:
        print(f'{file.capitalize()} does not exist')