#!/usr/bin/python3
import cmd


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '
    print("\n")

    def emptyline(self):
        """Method called when an empty line
           is entered in response to the prompt.
        """
        prompt = '(hbnb) '/n

    def do_EOF(self, line):
        """indicates the end of a file"""
        return True

    def do_quit(self, line):
        """this method exits the program"""
        return True

    def help_quit(self):
        """Method prints the quit command
        """
        print("Quit command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
