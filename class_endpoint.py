import requests

class Kraken:
    def __init__(self):
        self.base_url = "https://api.krakenflex.systems/interview-tests-mock-api/v1"
        self.headers = {"x-api-key": "EltgJ5G8m44IzwE6UN2Y4B4NjPW77Zk6FJK3lL23"} 


    def invoke_get(self, endpoint):
        outages_response = requests.get(f"{self.base_url}/{endpoint}", headers=self.headers)
        if outages_response.status_code == 200:
            return outages_response.json()
        else:
            print("Request failed with status code:", outages_response.status_code)
            return None  # Return None or raise an exception in case of failure

    def invoke_post(self, endpoint, data):
        post_response = requests.post(f"{self.base_url}/{endpoint}", headers=self.headers, json=data)
        if post_response.status_code == 200:
           print("Request was successful")
        else:
            print("Request failed with status code:", post_response.status_code)

    def extract_device_id(self, device_info):
   #  info= invoke_get("site-info/norwich-pear-tree")
        devices = device_info["devices"]
        device_ids = []
        for devices_index in devices:
            device_ids.append(devices_index["id"])
        return device_ids


    def filter_outages(self,outages, device_ids):
        new_outages = []
        for outage_index in outages:
            begin = outage_index["begin"]
            site_id = outage_index["id"]
            year = begin[:4]
        # store the old outages < `2022-01-01T00:00:00.000Z` in the olf_outages list and the new ones in the new_outages
            if int(year) >= 2022 and site_id in device_ids:
                new_outages.append(outage_index)  
        return new_outages      
                 

    def outages_with_name(self, new_outages, devices):
        enriched_outages = []
        for current_outage in new_outages:
            outage_id = current_outage["id"] 
         #print(outages_id)
            for current_device in devices:
     #  print(device_id["id"])
                info_id = current_device["id"]
                if info_id == outage_id:
                    result = current_outage
                    result["name"] = current_device["name"]
                    enriched_outages.append(result)
        return enriched_outages


        