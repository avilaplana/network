__author__ = 'alvarovilaplana'
import socket

def list_ports_tcp_open(ip, ports, timeout=1):
    ports_open = []
    for port in ports:
        if is_tcp_open(ip, port, timeout):
            ports_open.append(port)

    return ports_open


def is_tcp_open(ip, port, timeout=1):
    return _is_open(ip, port, socket.SOCK_STREAM, timeout)

def _is_open(ip, port, protocol, timeout):
    sock = socket.socket(socket.AF_INET, protocol)
    sock.settimeout(timeout)
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

