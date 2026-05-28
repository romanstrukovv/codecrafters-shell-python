import sys


def main():
    # # TODO: Uncomment the code below to pass the first stage
    # sys.stdout.write("$ ")
    # pass
    while True:
        command = input("$ ")
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
                print(f'{args[0]}: not found')           
        else:
            print(f'{command}: command not found')


if __name__ == "__main__":
    main()
