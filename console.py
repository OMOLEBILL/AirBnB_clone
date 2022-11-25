#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

class_dict = {"BaseModel": BaseModel}
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
            l = [str(obj) for key, obj in p.items()
                if type(obj).__name__ == arg_list[0]]
            print(l)
            

            
if __name__ == '__main__' :
    HBNBCommand().cmdloop()
