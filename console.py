#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re

class_dict = {"BaseModel": BaseModel, "User": User, "State": State,
              "City": City, "Amenity": Amenity, "Place": Place, 
               "Review": Review}


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(hbnb) '

    def emptyline(self):
        """Method called when an empty line
           is entered in response to the prompt.
        """
        pass

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

    def do_create(self, arg):
        "create a new instance of base model"
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] in class_dict:
            Class = class_dict[arg_list[0]]
            instance = Class()
            print(instance.id)
            instance.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        p = storage.all()
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in class_dict.keys():
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif f"{arg_list[0]}.{arg_list[1]}" not in p.keys():
            print("** no instance found **")
        else:
            print(p[f"{arg_list[0]}.{arg_list[1]}"])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name
        and id (save the change into the JSON file)"""
        p = storage.all()
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in class_dict.keys():
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif f"{arg_list[0]}.{arg_list[1]}" not in p.keys():
            print("** no instance found **")
        else:
            p.pop(f"{arg_list[0]}.{arg_list[1]}")
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name"""
        arg_list = arg.split()
        p = storage.all()
        if len(arg_list) == 0:
            print([str(p[key]) for key in p.keys()])
        elif len(arg_list) == 1:
            if arg_list[0] not in class_dict.keys():
                print("** class doesn't exist **")
                return
            lists = [str(v) for k, v in p.items()
                    if type(v).__name__ == arg_list[0]]
            print(lists)

    def do_update(self, arg):
        """Updates an instance based on the class name
        and id by adding or updating attribute """
        arg_list = arg.split()
        p = storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in class_dict.keys():
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif f"{arg_list[0]}.{arg_list[1]}" not in p.keys():
            print("** no instance found **")
        elif len(arg_list) == 2:
            print("** attribute name missing **")
        elif len(arg_list) == 3:
            print("** value missing **")
        else:
            cast = None
            if not re.search('^".*"$', arg_list[3]):
                if '.' in arg_list[3]:
                    cast = float
                else:
                    cast = int
            else:
                arg_list[3] = arg_list[3].replace('"', '')
            if cast:
                try:
                    arg_list[3] = cast(arg_list[3])
                except ValueError:
                    pass
            key = f"{arg_list[0]}.{arg_list[1]}"
            setattr(p[key], arg_list[2], arg_list[3])
            storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
