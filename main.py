import cmd

class MyCLI(cmd.CMD):
    prompt = "PyTask$"
    intro = "Pytask v0.0.1 Welcome! prompt 'help' for commands"

    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, World!")

    def do_quit(self, line):
        """Exit the CLI."""
        return True
