import os 
if __name__ == '__main__':
    file = input("Enter the file you want to compile > ")
    if os.path.exists(file) and os.path.isfile(file):
        os.system(f"nasm -f elf32 {file} -o {file.strip(".asm")}.o")