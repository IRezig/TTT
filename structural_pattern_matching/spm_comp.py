def run_command(command: str) -> None:
    match command.split():
        case ["load", filename]:
            print(f"Loading filename {filename}.")
        case ["save", filename]:
            print(f"Saving filename {filename}.")
        case ["quit" | "exit" | "bye", *rest]:
            if "--force" in rest or "-f" in rest:
                print("Forcefully quitting the program.")
            else:
                print("Quitting the program.")
            quit()
        case _:
            print(f"Unknown command '{command}'.")


# load example.py
# save example.py
# bye
# quit --force
# quit -f


def run_command_v3(command: str) -> None:
    match command.split():
        case ["load", filename]:
            print(f"Loading filename {filename}.")
        case ["save", filename]:
            print(f"Saving filename {filename}.")
        case ["quit" | "exit" | "bye", *rest] if "--force" in rest or "-f" in rest:
            print("Sending SIGTERM to all processes and quitting the program.")
            quit()
        case ["quit" | "exit" | "bye"]:
            print("Quitting the program.")
            quit()
        case _:
            print(f"Unknown command {command!r}.")



def main():
    while True:
        command = input("Enter command: ")
        run_command(command)


if __name__ == "__main__":
    main()