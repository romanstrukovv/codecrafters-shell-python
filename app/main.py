import sys


def main():
    # # TODO: Uncomment the code below to pass the first stage
    # sys.stdout.write("$ ")
    # pass
    while True:
        command = input("$ ")
        cmd = command.split()[0]
        args = command.split()[1:]
        if cmd == "exit":
            break
        elif cmd == "echo":
            print(" ".join(args))
        else:
            print(f'{command}: command not found')


if __name__ == "__main__":
    main()
