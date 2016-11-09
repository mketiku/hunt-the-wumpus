#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
'''Application enables a client to play hunt the wumpus using a socket.'''
__author__ = "Michael Ketiku"
__project__ = "HuntTheWumpusClient"
___email__ = "mketiku@gmail.com"
___status__ = "unstable-dangerous"

# Import the socket module
import socket
# Import command line arguments
from sys import argv


class HTWClient(object):
    """HTWClient deals with networking and communication with the HTWServer."""

    def __init__(self):
        """Initializes the client and create a client socket."""
        # Create a TCP/IP socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, address, port_number):
        """Keeps repeating connecting to the server and returns True if

        connected successfully.
        """
        while True:
            try:
                print("Connecting to the game server...")
                # Connection time out 15 seconds
                self.client_socket.settimeout(15)
                # Connect to the specified host and port
                self.client_socket.connect((address, int(port_number)))
                # Return True if connected successfully
                return True
            except:
                # Caught an error
                print("There was an error when trying to connect to " + str(
                    address) + "::" + str(port_number))
                self.__connect_failed__()
        return False

    def __connect_failed__(self):
        """(Private) This function will be called when the attempt to connect

        failed.
        """
        # Ask the user what to do with the error
        choice = input("[A]bort, [C]hange address and port, or [R]etry?")
        if (choice.lower() == "a"):
            exit()
        elif (choice.lower() == "c"):
            address = input("Please enter the address:")
            port_number = input("Please enter the port:")

    def s_send(self, command_type, msg):
        """Sends a message to the server with an agreed command type token

        to ensure the message is delivered safely.
        """
        # A 1 byte command_type character is put at the front of the message
        # as a communication convention
        try:
            self.client_socket.send((command_type + msg).encode())
        except:
            # If any error occurred, the connection might be lost
            self.__connection_lost()

    def s_recv(self, *args):
        """Receives a packet with specified size from the server and check

        its integrity by comparing its command type token with the expected
        one.
        """
        # size = 1024

        self.client_socket.recv(1024).decode()
        try:
            message = self.client_socket.recv(size).decode()
            return message
        except:
            # If any error occurred, the connection might be lost
            self.__connection_lost()
        return message

    def __connection_lost(self):
        """(Private) This function will be called when the connection is lost.

        """
        print("Error: connection lost.")
        try:
            # Try and send a message back to the server to notify connection
            # lost
            self.client_socket.send("q".encode())
        except:
            pass
        # Raise an error to finish
        raise Exception

    def close(self):
        """Shut down the socket and close it"""
        # Shut down the socket to prevent further sends/receives
        self.client_socket.shutdown(socket.SHUT_RDWR)
        # Close the socket
        self.client_socket.close()


# Define the main program


def main():
    # If there are more than 3 arguments
    if (len(argv) >= 3):
        # Set the address to argument 1, and port number to argument 2
        address = argv[1]
        port_number = argv[2]
    else:
        # Ask the user to input the address and port number
        address = input("Please enter the address: ")
        port_number = input("Please enter the port: ")

    client = HTWClient()
    client.connect(address, port_number)
    client.s_send("suh", "dude")
    client.s_recv()
    # client.close()
    print(client.__dict__)

    command = {}
    print(command)
    # # Initialize the client object
    # client = HTWClientGame()
    # # Connect to the server
    # client.connect(address, port_number)
    # try:
    #     # Start the game
    #     client.start_game()
    # except:
    #     print(("Game finished unexpectedly!"))
    # finally:
    #     # Close the client
    #     client.close()


if __name__ == "__main__":
    # If this script is running as a standalone program,
    # start the main program.
    main()
