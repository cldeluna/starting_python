#!/usr/bin/env python

# Import the netmiko module
import netmiko
import json
import argparse


def connect_to_dev(dev_dict):
# Safely attempt to connect to a device and gracefully exit.
    try:
        connection_object = netmiko.Netmiko(**dev_dict)

    except Exception as e:
        print(f"ERROR. Could not establish connection to {dev_dict['host']}!\nException: {e}\nAborting Program!")
        exit()

    return connection_object

def save_devices_to_json(filename="devices.json"):

    devices = {}
    cisco_ios_info = {
        "host": "ios-xe-mgmt-latest.cisco.com",
        "username": "developer",
        "password": "C1sco12345",
        "port": 8181,
        "device_type": "cisco_ios",
    }

    cisco_ios_info2 = {
        "host": "ios-xe-mgmt.cisco.com",
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
        "host": "10.10.30.31",
        "username": "admin",
        "password": "A123m!",
        "device_type": "cisco_wlc",
    }


    devices.update({'ios': [cisco_ios_info]})
    # print(devices)
    value_list = devices['ios']
    # print(value_list)
    value_list.append(cisco_ios_info2)
    # print(value_list)
    devices.update({'ios': value_list})
    devices.update({'wlc':[cisco_wlc_info]})
    devices.update({'asa':[cisco_asa_info]})

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(devices, f, ensure_ascii=False, indent=4)

    print(f"Saved device data into file {filename}")


def load_devices_from_json(filename="devices.json"):
# Safely attempt to load device data from a json file
    try:
        with open(filename) as json_file:
            data = json.load(json_file)

    except Exception as e:
        print(f"ERROR. Could not open devices file {filename}!\nException: {e}\nAborting Program!")
        exit()
    return data

def execute_cmd(dev,cmd):

    print(f"\n\n== Establishing connection to device {dev['host']}")
    net_connect = connect_to_dev(dev)
    print(f"\n== Connection Result: \n{net_connect}")

    print(f"\n== Display the device prompt:")
    print(net_connect.find_prompt())

    print(f"\n== Output result of command <{cmd}>")
    output = net_connect.send_command(cmd)
    print(output)
    print(f"\n== Disconnect from device {dev['host']}")

    net_connect.disconnect()
    print(f"\n== Disconnected\n\n")

    return output

def main():
    # Function to save devices information to a JSON file
    save_devices_to_json()

    # Function to load devices information from a JSON file
    devs_dict = load_devices_from_json()

    # pick out the device type (based on command line arguments)
    dev_info_list_of_dicts = devs_dict[arguments.device_type]

    for item in dev_info_list_of_dicts:
        print(item)

    commands = {"asa": "show int ip br", "ios": "show ip int br", "wlc": "show interface summary"}

    # Set command
    print(f"\n\n== Setting command to execute for device type {arguments.device_type}")
    if arguments.device_type == "asa":
        print(f"\tSetting ASA command {commands['asa']}")
        command = commands['asa']
    elif arguments.device_type == "wlc":
        print(f"\tSetting WLC command {commands['wlc']}")
        command = commands['wlc']
    elif arguments.device_type == "ios":
        print(f"\tSetting IOS command {commands['ios']}")
        command = commands['ios']

    cmd_output = {}
    for a_device_dict in dev_info_list_of_dicts:
        cmd_output.update({a_device_dict['host']: execute_cmd(a_device_dict, command)})


    print(f"\n\n******** Consolidated Output for {len(cmd_output)} device(s) **********\n")
    for key in cmd_output.keys():
        print(f"\nKey: {key}\nResponse:\n{cmd_output[key]}")

   

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Connect to Network Device')

    parser.add_argument('-d', '--device_type', action="store", default='ios')

    arguments = parser.parse_args()

    main()