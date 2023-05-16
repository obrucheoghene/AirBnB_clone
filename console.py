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
    __all_classes = ["BaseModel"]

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
        elif args not in self.__all_classes:
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
        saved_model = storage.all()
        if args == "":
            print("** class name missing **")
            return
        params = args.split()
        if params[0] not in self.__all_classes:
            print("** class doesn't exist **")
            return
        elif len(params) == 1:
            print("** instance id missing **")
            return
        elif "{}.{}".format(params[0], params[1]) not in saved_model.keys():
            print("** no instance found **")
        else:
            print(saved_model["{}.{}".format(params[0], params[1])])

    def do_all(self, args):
        """
        Prints all string representation
        of all instances or the specified one only
        Usage: all <class name> | all
        """
        all_instances = storage.all().values()
        if args == "":
            print([str(obj) for obj in all_instances])
            return
        params = args.split()
        class_name = params[0]
        if class_name not in self.__all_classes:
            print("** class doesn't exist **")
        else:
            print([str(obj) for obj in all_instances
                   if class_name == obj.__class__.__name__])

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id
        Usage: destroy BaseModel 1234-1234-1234
        """
        saved_model = storage.all()
        if args == "":
            print("** class name missing **")
            return
        params = args.split()
        if params[0] not in self.__all_classes:
            print("** class doesn't exist **")
            return
        elif len(params) == 1:
            print("** instance id missing **")
            return
        elif "{}.{}".format(params[0], params[1]) not in saved_model.keys():
            print("** no instance found **")
        else:
            del saved_model["{}.{}".format(params[0], params[1])]
            storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
