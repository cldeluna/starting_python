#!/usr/bin/env python

# Import the netmiko module
# from netmiko import Netmiko
import netmiko


dev_info = {
    "host": "ios-xe-mgmt-latest.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "port": 8181,
    "device_type": "cisco_ios",
}


print(f"\n\n== Establishing connection to device {dev_info['host']}")
net_connect = netmiko.Netmiko(**dev_info)
print(f"\n== Connection Result: \n{net_connect}")
# If you are curious about what other methods are available on the netmiko object use dir
# print(dir(net_connect))

command = "show ip int brief"

print(f"\n== Display the device prompt:")
# notice 
print(net_connect.find_prompt())

print(f"\n== Check Enable mode:")
print(net_connect.check_enable_mode())

print(f"\n== Output result of command <{command}>")
output = net_connect.send_command(command)
print(output)
print(f"\n== Disconnect from device {dev_info['host']}")

net_connect.disconnect()
print(f"\n== Disconnected\n\n")

