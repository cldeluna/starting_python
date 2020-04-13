
from netmiko import Netmiko

dev_info = {"host": "ios-xe-mgmt-latest.cisco.com","username": "developer", "password": "C1sco12345", "port": 8181, "device_type": "cisco_ios"}
print(type(dev_info))
command = "show ip int brief"
net_connect = Netmiko(**dev_info)
output = net_connect.send_command(command)
net_connect.disconnect()
