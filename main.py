import cmd
import os
import json
filename = "task.json"
new_id = 1

class MyCLI(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to MyCLI. Type "help" for available commands.'

    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, World!")

    def do_create_task(self, linei):
        if os.path.exists(filename):
    with open(filename, 'r') as json_file:
        try:
            existing_tasks = json.load(json_file)
        existing_ids = [task['ID'] for task in existing_tasks if task['ID'] is not None]
            if existing_ids:
                new_id = max(existing_ids) + 1
        except json.JSONDecodeError:
            existing_tasks = []
        task_name = str(input("Name your task", ))
        new_task = {
           "name": task_name,
           "staus": None,
           "ID": new_id
}
        exsisting_tasks.append(new_task)
        jsonData = json.dumps(new_task)
        jsondata = [{"id": i, **d} for i, d in enumerate(jsonData)]
        print(json.dumps(jsonData, indent=4, sort_keys=False))


    def do_quit(self, line):
        """Exit the CLI."""
        return True

if __name__ == '__main__':
    MyCLI().cmdloop()
