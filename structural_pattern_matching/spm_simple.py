def run_command(command: str) -> None:
    """Run a command and return its output as a byte string."""
    match command:
        case "ls" | "/l":
            print("total 0\n")
        case "pwd":
            print("/home/user\n")
        case _:
            print("No such command\n")


def main():
    """Run the main program."""
    while True:
        command = input("Enter command: ")
        run_command(command)


if __name__ == "__main__":
    main()
