#!/usr/bin/python3

import cmd
from models import BaseModel, storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """EOF command to end the program"""
        return True

    def do_quit(self, arg):
        """Quite command to end the program"""
        return True
    
    def emptyline(self):
        """an empty line + ENTER will execute anything"""
        pass

    def do_create(self, arg):
        """Create command will create a new instance of the specified model."""
        if not arg:
            print("** class name missing **")
            return
        
        if not arg == 'BaseModel':
            print("** class doesn't exist **")
            return
        
        baseModel = BaseModel()
        storage.new(baseModel)
        storage.save()
        print(baseModel.id)

    def do_show(self, arg):
        """Show command will show a model based on the given ID."""
        if not arg:
            print("** class name missing **")
            return
        
        args = arg.split(" ")
        
        if len(args) != 2:
            if not args[0] == "BaseModel":
                print("** class doesn't exist **")
                return
            print("** instance id missing **")
            return
        
        className = args[0]
        id = args[1]
        for key, value in storage.all().items():
            if key == f"{className}.{id}":
                print(value)
                return
        print("** no instance found **")

    def do_destroy(self, arg):
        """Destory command will remove a model based on the given ID."""
        if not arg:
            print("** class name missing **")
            return
        
        args = arg.split(" ")
        
        if len(args) != 2:
            if not args[0] == "BaseModel":
                print("** class doesn't exist **")
                return
            print("** instance id missing **")
            return
        
        className = args[0]
        id = args[1]
        for key, value in storage.all().items():
            if key == f"{className}.{id}":
                storage.destroy(value)
                storage.save()
                return
        print("** no instance found **")


    def do_all(self, arg):
        """All command will list all the models based on a given class, if no class was given, it'll show all the models."""
        if arg:
            if not arg == 'BaseModel':
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    if value['__class__'] == arg:
                        print(value)
        else:
            for key, value in storage.all().items():
                print(value)


    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        if not arg:
            print("** class name missing **")
            return
        
        args = arg.split(" ")
        
        if len(args) == 1:
            if args[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            else:
                print("** instance id missing **")
                return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
            
        
        className = args[0]
        if className != "BaseModel":
            print("** class doesn't exist **")
            return

        id = args[1]
        attribute_name = args[2]
        attribute_value = args[3]
        for key, value in storage.all().items():
            if key == f"{className}.{id}":
                storage.update(value, attribute_name, attribute_value)
                storage.save()
                storage.reload()
                return

if __name__ == "__main__":
    HBNBCommand().cmdloop()

