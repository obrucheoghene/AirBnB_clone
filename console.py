#!/usr/bin/python3
"""
This module defines the console
"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Represents the HBNB command interpreter for Airbnb
    """
    prompt = "(hbnb) "
    __classes = ["BaseModel"]

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF signal to exit the program"""
        return True

    def emptyline(self):
        """
        Do nothing when the user presses Enter on an empty line
        """
        pass

    def do_create(self, args):
        """
        Creates a new instance of Model
        Usage: create <class name>
        """
        if args == "":
            print("** class name missing **")
            return
        elif args not in self.__classes:
            print("** class doesn't exist **")
            return
        obj = eval(args)()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """
        Prints the string representation
        of an instance
        Usage: show <class name> <id>
        """
        if args == "":
            print("** class name missing **")
            return
        params = args.split()
        if params[0] not in self.__classes:
            print("** class doesn't exist **")
            return
        elif len(params) == 1:
            print("** instance id missing **")
            return
        else:
            saved_models = storage.all()
            for obj in saved_models.values():
                if obj.id == id:
                    print(obj)
                    return
            print("* no instance found **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
