#!/usr/bin/python3

#This is for exiting the console

import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class provides a command-line interface for interacting with the HBNB program.
    """

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        Usage: quit
        """
        return True

    do_EOF = do_quit

    def emptyline(self):
        """
        Do nothing on empty input line.
        """
        pass

if __name__ == '__main__':
    """
    Entry point of the script.
    """
    HBNBCommand().cmdloop()
