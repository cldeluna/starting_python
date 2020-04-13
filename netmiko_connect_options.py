#!/usr/bin/env python

# Import the netmiko module
import netmiko

cisco_ios_info = {
    "host": "ios-xe-mgmt-latest.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "port": 8181,
    "device_type": "cisco_ios",
}

cisco_asa_info = {
    "host": "10.1.10.27",
    "username": "admin",
    "password": "cisco",
    "device_type": "cisco_asa",
}


cisco_wlc_info = {
    "host": "10.10.30.30",
    "username": "admin",
    "password": "A123m!",
    "device_type": "cisco_wlc",
}

dev_info = cisco_asa_info


command = "show ip int brief"
commands = {"asa": "show int ip br", "ios": "show ip int br", "wlc": "show interface summary"}


# Set command
print(f"\n\n== Setting command to execute for device type {dev_info['device_type']}")
if dev_info['device_type'] == "cisco_asa":
    print(f"\tSetting ASA command {commands['asa']}")
    command = commands['asa']
elif dev_info['device_type'] == "cisco_wlc":
    print(f"\tSetting WLC command {commands['wlc']}")
    command = commands['wlc']
elif dev_info['device_type'] == "cisco_ios":
    print(f"\tSetting IOS command {commands['ios']}")
    command = commands['ios']

print(f"\n\n== Establishing connection to device {dev_info['host']}")
net_connect = netmiko.Netmiko(**dev_info)
print(f"\n== Connection Result: \n{net_connect}")

print(f"\n== Display the device prompt:")
print(net_connect.find_prompt())

print(f"\n== Output result of command <{command}>")
output = net_connect.send_command(command)
print(output)
print(f"\n== Disconnect from device {dev_info['host']}")

net_connect.disconnect()
print(f"\n== Disconnected\n\n")