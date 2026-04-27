from shlex import split
from commands.help import help_command
from commands.tasks import make_task
from helpers.args import parse_add


def main():
    print("Task менеджер. help - для справки")
    while True:
        try:
            raw = input("> ").strip().lower()
            parts = split(raw)
            cmd, args = parts[0], parts[1:]
            match cmd:
                case "help":
                    help_command()
                case "add":
                    title, priority, due, tags = parse_add(args)
                    print(make_task(1, title, priority, due, tags))
                case "remove":
                    pass
                case "edit":
                    pass
                case "tags":
                    pass
                case "exit":
                    break
                case _:
                    print("Неизвестная команда")
        except KeyboardInterrupt:
            print("\nЗавершение работы...")
            break
        except Exception as e:
            print(f"[ERROR]: {e}")


main()
