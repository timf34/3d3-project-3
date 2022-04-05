import socket
import requests


def get_local_ip_address() -> str:
    """
    Get local IP address of the machine
    """
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print("Local IP address: {}".format(local_ip))
    return local_ip


def get_public_ip_address() -> str:
    """
    Get public IP address of the machine
    """
    url = "https://api.ipify.org"
    response = requests.get(url)
    public_ip = response.text
    print("Public IP address: {}".format(public_ip))
    return public_ip


def test():
    get_local_ip_address()
    x = get_public_ip_address()


if __name__ == '__main__':
    test()
    print("Done")
