#!/usr/bin/python3
"""
This module defines the console
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Represents the HBNB command interpreter for Airbnb
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        return True

    def emptyline(self):
        """Do nothing when the user presses Enter on an empty line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
