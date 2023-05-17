#!/usr/bin/python3
"""
This module defines the console
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Represents the HBNB command interpreter for Airbnb
    """
    prompt = "(hbnb) "
    __all_classes = ["BaseModel",
                     "User",
                     "State",
                     "City",
                     "Place",
                     "Amenity",
                     "Review"]

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

    def do_update(self, args):
        """
        Updates an instance based on the class name and id
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        saved_model = storage.all()
        if args == "":
            print("** class doesn't exist **")
            return
        params = args.split()
        params_len = len(params)
        if params[0] not in self.__all_classes:
            print("** class doesn't exist **")
            return
        if params_len == 1:
            print("** instance id missing **")
            return
        if "{}.{}".format(params[0], params[1]) not in saved_model.keys():
            print("** no instance found **")
            return
        if params_len == 2:
            print("** attribute name missing **")
            return
        if params_len == 3:
            print("** value missing **")
            return
        if params_len == 4:
            obj = saved_model["{}.{}".format(params[0], params[1])]
            if params[2] in obj.__class__.__dict__.keys():
                attr_type = type(obj.__class__.__dict__[params[2]])
                obj.__dict__[params[2]] = attr_type(params[3])
            else:
                obj.__dict__[params[2]] = params[3]
        elif type(eval(params[2])) == dict:
            obj = saved_model["{}.{}".format(params[0], params[1])]
            for k, v in eval(params[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    attr_type = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = attr_type(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
