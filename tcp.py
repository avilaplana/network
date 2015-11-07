#!/usr/bin/env python
import socket
import sys
import transport

if (len(sys.argv) != 3 and len(sys.argv) != 4):
    print "Format 'ports server_name port_from [port_to]'"
    sys.exit()

port_from = int(sys.argv[2])
if (len(sys.argv)) == 3:
    port_to = port_from + 1
else:
    port_to = int(sys.argv[3])

target_server_name = sys.argv[1]
target_server_ip = socket.gethostbyname(target_server_name)
range_ports = range(port_from, port_to)
print "Scanning: %s (%s) tcp ports." % (target_server_name, target_server_ip)

for port_scanned in range_ports:
    if transport.is_tcp_open(target_server_ip, port_scanned):
        print "The port:%s is open." % (port_scanned)


