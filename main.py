import cmd
import json

class MyCLI(cmd.Cmd):
    prompt = '>> '
    intro = 'Welcome to MyCLI. Type "help" for available commands.'

    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, World!")

   def do_create_task(self, line):
       task_name = input("Name your task", )

    def do_quit(self, line):
        """Exit the CLI."""
        return True

if __name__ == '__main__':
    MyCLI().cmdloop()
