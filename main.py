# This is the template code for the CNA337 Final Project
# Zachary Rubin, zrubin@rtc.edu
# CNA 337 Fall 2020

from Server import Server


def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Suhad")


# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    ip_address = " 18.218.223.251"
    server = Server(ip_address)
    result = server.ping()
    print(result)
    if result == 0:
        print("Server with ip [%s] is up." % ip_address)