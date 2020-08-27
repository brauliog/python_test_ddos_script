import ipaddress
import socket


def target_ip():
    """
    :return: asks for a valid ip address as input
    """
    while True:
        try:
            val = input("Enter Target IP Address: ")
            return ipaddress.ip_address(val)
        except ValueError:
            print("Not a valid IP address")


def set_port():
    """
    :return: asks for a port number as input
    """
    while True:
        try:
            port = int(input("Enter Port Number: "))
            return port
        except ValueError:
            print("Enter Valid number")


def run_attack(target, port_number):
    pass
    # # create a socket connection
    # while True:
    #     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     s.connect(target, port_number)
    #     # sending data
