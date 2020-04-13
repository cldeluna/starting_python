#!/usr/bin/env python

# Import the netmiko module
from netmiko import Netmiko


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
    "host": "ios-xe-mgmt-latest.cisco.com",
    "username": "developer",
    "password": "C1sco12345",
    "port": 8181,
    "device_type": "cisco_wlc",
}


commands = {"asa": "show int ip br", "ios": "show ip int br", "wlc": "show interface summary"}

dev_info = cisco_wlc_info

print(f"\n\n== Establishing connection to device {dev_info['host']}")
net_connect = Netmiko(**dev_info)
print(f"\n== Connection Result: \n{net_connect}")

command = "show ip int brief"

print(f"\n== Display the device prompt:")
print(net_connect.find_prompt())

if dev_info['device_type'] == "cisco_asa":
    command = commands['asa']
elif dev_info['device_type'] == "cisco_wlc":
    command = commands['wlc']
elif dev_info['device_type'] == "cisco_ios":
    command = commands['ios']

print(f"\n== Output result of command <{command}>")
output = net_connect.send_command(command)
print(output)
print(f"\n== Disconnect from device {dev_info['host']}")

net_connect.disconnect()
print(f"\n== Disconnected\n\n")



"""
https://github.com/ktbyers/netmiko/blob/develop/netmiko/ssh_dispatcher.py
# The keys of this dictionary are the supported device_types
CLASS_MAPPER_BASE = {
    "a10": A10SSH,
    "accedian": AccedianSSH,
    "alcatel_aos": AlcatelAosSSH,
    "alcatel_sros": NokiaSrosSSH,
    "apresia_aeos": ApresiaAeosSSH,
    "arista_eos": AristaSSH,
    "aruba_os": ArubaSSH,
    "avaya_ers": ExtremeErsSSH,
    "avaya_vsp": ExtremeVspSSH,
    "brocade_fastiron": RuckusFastironSSH,
    "brocade_netiron": ExtremeNetironSSH,
    "brocade_nos": ExtremeNosSSH,
    "brocade_vdx": ExtremeNosSSH,
    "brocade_vyos": VyOSSSH,
    "checkpoint_gaia": CheckPointGaiaSSH,
    "calix_b6": CalixB6SSH,
    "ciena_saos": CienaSaosSSH,
    "cisco_asa": CiscoAsaSSH,
    "cisco_ios": CiscoIosSSH,
    "cisco_nxos": CiscoNxosSSH,
    "cisco_s300": CiscoS300SSH,
    "cisco_tp": CiscoTpTcCeSSH,
    "cisco_wlc": CiscoWlcSSH,
    "cisco_xe": CiscoIosSSH,
    "cisco_xr": CiscoXrSSH,
    "cloudgenix_ion": CloudGenixIonSSH,
    "coriant": CoriantSSH,
    "dell_dnos9": DellForce10SSH,
    "dell_force10": DellForce10SSH,
    "dell_os6": DellDNOS6SSH,
    "dell_os9": DellForce10SSH,
    "dell_os10": DellOS10SSH,
    "dell_powerconnect": DellPowerConnectSSH,
    "dell_isilon": DellIsilonSSH,
    "dlink_ds": DlinkDSSSH,
    "endace": EndaceSSH,
    "eltex": EltexSSH,
    "eltex_esr": EltexEsrSSH,
    "enterasys": EnterasysSSH,
    "extreme": ExtremeExosSSH,
    "extreme_ers": ExtremeErsSSH,
    "extreme_exos": ExtremeExosSSH,
    "extreme_netiron": ExtremeNetironSSH,
    "extreme_nos": ExtremeNosSSH,
    "extreme_slx": ExtremeSlxSSH,
    "extreme_vdx": ExtremeNosSSH,
    "extreme_vsp": ExtremeVspSSH,
    "extreme_wing": ExtremeWingSSH,
    "f5_ltm": F5TmshSSH,
    "f5_tmsh": F5TmshSSH,
    "f5_linux": F5LinuxSSH,
    "flexvnf": FlexvnfSSH,
    "fortinet": FortinetSSH,
    "generic_termserver": TerminalServerSSH,
    "hp_comware": HPComwareSSH,
    "hp_procurve": HPProcurveSSH,
    "huawei": HuaweiSSH,
    "huawei_smartax": HuaweiSmartAXSSH,
    "huawei_olt": HuaweiSmartAXSSH,
    "huawei_vrpv8": HuaweiVrpv8SSH,
    "ipinfusion_ocnos": IpInfusionOcNOSSSH,
    "juniper": JuniperSSH,
    "juniper_junos": JuniperSSH,
    "juniper_screenos": JuniperScreenOsSSH,
    "keymile": KeymileSSH,
    "keymile_nos": KeymileNOSSSH,
    "linux": LinuxSSH,
    "mikrotik_routeros": MikrotikRouterOsSSH,
    "mikrotik_switchos": MikrotikSwitchOsSSH,
    "mellanox": MellanoxMlnxosSSH,
    "mellanox_mlnxos": MellanoxMlnxosSSH,
    "mrv_lx": MrvLxSSH,
    "mrv_optiswitch": MrvOptiswitchSSH,
    "netapp_cdot": NetAppcDotSSH,
    "netscaler": NetscalerSSH,
    "nokia_sros": NokiaSrosSSH,
    "oneaccess_oneos": OneaccessOneOSSSH,
    "ovs_linux": OvsLinuxSSH,
    "paloalto_panos": PaloAltoPanosSSH,
    "pluribus": PluribusSSH,
    "quanta_mesh": QuantaMeshSSH,
    "rad_etx": RadETXSSH,
    "ruckus_fastiron": RuckusFastironSSH,
    "ruijie_os": RuijieOSSSH,
    "sophos_sfos": SophosSfosSSH,
    "ubiquiti_edge": UbiquitiEdgeSSH,
    "ubiquiti_edgeswitch": UbiquitiEdgeSSH,
    "ubiquiti_unifiswitch": UbiquitiUnifiSwitchSSH,
    "vyatta_vyos": VyOSSSH,
    "vyos": VyOSSSH,
    "watchguard_fireware": WatchguardFirewareSSH,
}
"""