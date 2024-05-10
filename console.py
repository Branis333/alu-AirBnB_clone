#!/usr/bin/python3

""" For quiting the console """

import cmd

class HBNBCommand(cmd.Cmd):
    """
    Command-line interface for interacting with the HBNB program.

    This class provides a command-line interface for users to interact with the HBNB program.
    It inherits from the cmd.Cmd class provided by the cmd module.
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

    This block of code is executed when the script is run as a standalone program.
    It creates an instance of the HBNBCommand class and starts the command loop.
    """
    HBNBCommand().cmdloop()

