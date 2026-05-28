import sys
import os
import subprocess

def main():
    # # TODO: Uncomment the code below to pass the first stage
    # sys.stdout.write("$ ")
    # pass
    while True:
        command = input("$ ")
        # if len(command) == 0:
        #     continue
        cmd = command.split()[0]
        args = command.split()[1:]
        valid_cmds = ("exit", "echo", "type")

        if cmd == "exit":
            break
        elif cmd == "echo":
            print(" ".join(args))
        elif cmd == "type": 
            if args and args[0] in valid_cmds:
                print(f'{args[0]} is a shell builtin')
            else:
                path_env = os.getenv("PATH", "")
                paths = path_env.split(os.pathsep)
                found = False
                
                for p in paths:
                    if os.path.isdir(p):
                        try:
                            for e in os.scandir(p):
                                if e.is_file() and e.name == args[0] and os.access(e, os.X_OK): 
                                    print(f'{args[0]} is {e.path}')
                                    found = True
                                    break
                        except PermissionError:
                            continue
                    if found:
                        break                        
                if not found:
                    print(f'{args[0]}: not found')           
        else:            
            cmd_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), cmd)
            if os.path.isfile(cmd_path) and os.access(cmd_path, os.X_OK):
                cmd_exe = subprocess.run([sys.executable, cmd, *args], capture_output=True, text=True, check=True)
                print(cmd_exe.stdout, end="")
                
                # print(f'{command}: command not found')


if __name__ == "__main__":
    main()
