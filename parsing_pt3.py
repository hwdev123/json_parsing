#! /usr/bin/python3
from utils.parsed import json_data
from datetime import date
data = json_data()



# Modifying Data

# Change the status of an inactive website to active.
def change_website_status():
    for website in data['websites']:
        if website['status'] == 'Inactive':
            website['status'].replace('Inactive','Active')
            print(f"The following website {website['domain']}'s status has been changed to active!")

# Update the last access timestamp for a specific system administrator.
def update_sysadmin_timestamp(id: int = 1):
    for sysadmin in data['data_center']['sysadmins']:
        if sysadmin['id'] == id:
            todays_date = date.today().strftime('%Y-%m-%d')
            last_access = sysadmin['last_access'][:10]
            print(f"The Sysadmin - {sysadmin['name']}'s last_access time was updated to: {last_access.replace(last_access, todays_date)}")



# Modify the subnet mask for a given network interface.
def update_subnet_mask(device_id: str, subnet_mask: str):
    for device in data['data_center']['network_devices']:
        if device_id == 'R1':
            for subnet in device['interfaces']:
                original_subnet_mask = subnet['subnet_mask']
                print(f"The new subnet mask for: {device_id}'s interface: {subnet['interface_id']} is: {subnet['subnet_mask'].replace(original_subnet_mask, subnet_mask)}")
        else:
            for subnet in device['interfaces']:
                original_subnet_mask = subnet['subnet_mask']
                print(f"The new subnet mask for: {device_id}'s interface: {subnet['interface_id']} is: {subnet['subnet_mask'].replace(original_subnet_mask, subnet_mask)}")
        




if __name__ == '__main__':
    change_website_status()
    print('=' * 100)
    update_sysadmin_timestamp()
    print('=' * 100)
    update_subnet_mask(device_id='R1', subnet_mask='255.255.240.0')