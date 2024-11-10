#! /usr/bin/python3
from utils.parsed import json_data
    
json_data: dict = json_data()

data_center, websites = json_data

# Basic Parsing and Traversal
def main():
# Print IPs of network devices
    print(f"These are the network devices in {data_center}'s IP Addresses: ")
    print('=' * 80)
    for data in json_data['data_center']['network_devices']:
        if data['device_id'] == 'SW1':
            print(f"SW1 MGMT IP: {data['device_id']}: {data['ip_address']}")
            print("=" * 80)

        elif  data['device_id'] == 'R1':
            print(f"R1 MGMT IP: {data['ip_address']}")
            for interfaces in data['interfaces']:
                if data['device_id'] == 'R1':
                    print(f"R1: {interfaces['interface_id']}: {interfaces['ip_address']} Mask: {interfaces['subnet_mask']}")

if __name__ == '__main__':
    main()

