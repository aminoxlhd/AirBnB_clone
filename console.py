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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
