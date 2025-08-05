import cmd
import json

class MyCLI(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to MyCLI. Type "help" for available commands.'

    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, World!")

    def do_create_task(self, line):
        task_name = str(input("Name your task", ))
        new_task = { "name":task_name, "status":None, "ID":None }
        jsonData = json.dumps(new_task)
        jsondata = [{"id": i, **d} for i, d in enumerate(jsonData)]
        print(json.dumps(jsonData, indent=4, sort_keys=False))


    def do_quit(self, line):
        """Exit the CLI."""
        return True

if __name__ == '__main__':
    MyCLI().cmdloop()
