import sys
import os
import subprocess

def find_in_path(cmd):
    path_env = os.getenv("PATH", "")
    paths = path_env.split(os.pathsep)
    
    for p in paths:
        if os.path.isdir(p):
            full_path = os.path.join(p, cmd)
            if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                return full_path
    return None

def main():
    last_cd_path = ""
    while True:
        command = input("$ ")
        if len(command) == 0:
            continue
        cmd = command.split()[0]
        args = command.split()[1:]
        valid_cmds = ("exit", "echo", "type", "pwd", "cd")

        if cmd == "exit":
            break
        elif cmd == "pwd":
            print(os.getcwd())
        elif cmd == "echo":
            print(" ".join(args))
        elif cmd == "cd":
            if len(args) == 0:
                continue
            if args[0] == '-':
                os.chdir(last_cd_path)                
            elif args[0] == '~':
                os.chdir(os.getenv("HOME"))
            elif os.path.isdir(args[0]):
                last_cd_path = os.getcwd()
                os.chdir(args[0])
            else:
                print(f'cd: {args[0]}: No such file or directory')
        elif cmd == "type": 
            if args and args[0] in valid_cmds:
                print(f'{args[0]} is a shell builtin')
            else:
                found_path = find_in_path(args[0])
                if found_path:
                    print(f'{args[0]} is {found_path}')
                else:
                    print(f'{args[0]}: not found')           
        else:            
            executable_path = find_in_path(cmd)
            
            if not executable_path:
                local_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), cmd)
                if os.path.isfile(local_path) and os.access(local_path, os.X_OK):
                    executable_path = local_path

            if executable_path:
                try:
                    cmd_exe = subprocess.run([cmd, *args], executable=executable_path, capture_output=True, text=True)
                    print(cmd_exe.stdout, end="")
                except OSError as e:
                    if e.errno == 8: 
                        cmd_exe = subprocess.run([sys.executable, executable_path, *args], executable=executable_path, capture_output=True, text=True)
                        print(cmd_exe.stdout, end="")
                    else:
                        raise e
            else:
                print(f'{cmd}: command not found')

if __name__ == "__main__":
    main()



