#!/usr/bin/python3
import cmd

#This is for exiting the console

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    def do_quit(self, arg):
        """ Quit command to exit the program"""
        return True
    do_EOF = do_quit

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
