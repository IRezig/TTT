def run_command(command):
    """Run a command and return its output as a byte string."""
    match command:
        case ["ls", "/l"]:
            print(b"total 0\n")
        case ["pwd"]:
            print(b"/home/user\n")
        case _:
            print(b"")


def main():
    """Run the main program."""
    while True:
        command = input("Enter command: ")
        run_command(command)
