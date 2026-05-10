from shlex import split
from commands.help import help_command
from tasks.model import Task
from commands.add import add_command
from storage.file import save_tasks, load_tasks


def main():
    file_path = "task_tracker/tasks.json"
    tasks, next_id = load_tasks("path")
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
                    next_id = add_command(tasks, args, next_id)
                case "remove":
                    pass
                case "edit":
                    pass
                case "tags":
                    pass
                case "exit":
                    save_tasks(file_path, tasks)
                    break
                case _:
                    print("Неизвестная команда")
        except KeyboardInterrupt:
            save_tasks(file_path, tasks)
            print("\nЗавершение работы...")
            break
        except Exception as e:
            save_tasks(file_path, tasks)
            print(f"[ERROR]: {e}")


main()
