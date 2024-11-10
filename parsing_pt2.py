#! /usr/bin/python3
from utils.parsed import json_data

# Filtering Data

data = json_data()


# List only the system administrators working the night shift.
def sysadmins_night():
    for admin in data['data_center']['sysadmins']:
        if admin['shift'] == 'Night':
            print(f"{admin['name']} is the sys admin that works night shifts in the Data Center.")

    


# Filter out and display details of websites that are currently active.
def active_website_details():
    for website in data['websites']:
        if website['status'] == 'Active':
            print(f"The domain: {website['domain']} is active and the following is the servers's information: ")
            print("=" * 80)
            print(f"IP Address: {website['server']['ip_address']}")
            print(f"Location: {website['server']['location']}")
            print(f"Operating System: {website['server']['os']}")
            print(f"Web Server: {website['server']['web_server']}")
            print(f"SSL Certificate expires: {website['server']['ssl_cert_expiration'][:10]}")
            print("=" * 80)


# Retrieve and display only those network interfaces on each device that are up.
def up_interfaces():
    for device in data['data_center']['network_devices']:
        if device['device_id'] == 'SW1' or 'R1':
            for interface in device['interfaces']:
                if interface['status'] == 'up':
                    print(f"The following interface on {device['device_id']} is in an up state: ")
                    print(f"{interface['interface_id']}")


if __name__ == '__main__':
    sysadmins_night()
    print()
    active_website_details()
    print()
    up_interfaces()