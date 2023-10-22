#import requests package
import requests

url = "https://api.krakenflex.systems/interview-tests-mock-api/v1"
enpoint_outages = f"{url}/outages"
headers = {"x-api-key": "EltgJ5G8m44IzwE6UN2Y4B4NjPW77Zk6FJK3lL23"}

#define get function 

def invoke_get(endpoint):
    response = requests.get(f"{url}/{endpoint}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Request failed with status code:", response.status_code)

#define post function
def invoke_post(endpoint,data):
    response = requests.post(f"{url}/{endpoint}", headers=headers, json=data)
    if response.status_code == 200:
        print("Request was successful")
    else:
        print("Request failed with status code:", response.status_code)

#call the function to get the data from outages and site_info endpoint
outages = invoke_get("outages")
info= invoke_get("site-info/norwich-pear-tree")

#print(outages)
print("---------------------------------------------------------------------------------------")

#print(info)


#get the device info
devices = info["devices"]
#print(f"this is the list of {devices}")

#print("---------------------------------------------------------------------------------------")

#set an empty list where to store the devices id 
device_id_info = []

for devices_index in devices:
    device_id_info.append(devices_index["id"])
print(f'this is the device_id list {device_id_info}')
print("---------------------------------------------------------------------------------------")

#create two lists where store the outages filtered based on the device id and the time

outages_response = requests.get(enpoint_outages, headers=headers)
new_outages = []
old_outages = []
 

#iterate through the outages list to get only the outages happened after 2022
if outages_response.status_code == 200:
    outages = outages_response.json()
    for outage_index in outages:
        begin = outage_index["begin"]
        site_id = outage_index["id"]
        year = begin[:4]
        # store the old outages < `2022-01-01T00:00:00.000Z` in the olf_outages list and the new ones in the new_outages
        if int(year) < 2022 or site_id not in device_id_info:
            old_outages.append(outage_index)
        else:
            new_outages.append(outage_index)
else:
    print("Request failed with status code:", outages_response.status_code)

print("-------------------------------------------------------------------------------------------------------------------------")

#print(f"new outages are{new_outages}")
#print("-------------------------------------------------------------------------------------------------------------------------")


#add a new key value for every object on the outages list based on the common id in the device list
for current_outage in new_outages:
    outage_id = current_outage["id"] 
    #print(outages_id)
    for current_device in devices:
     #  print(device_id["id"])
        info_id = current_device["id"]
        if info_id == outage_id:
            current_outage["name"] = current_device["name"]
    
print(f"this is an updated outages list with the name:  {new_outages}")


print("-------------------------------------------------------------------------------------------------------------------------")
#call the invoke post function to post the new outages list 

post=invoke_post("site-outages/norwich-pear-tree",new_outages)
print(post)



