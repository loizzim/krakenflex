import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class Kraken:
    def __init__(self):
        self.base_url = "https://api.krakenflex.systems/interview-tests-mock-api/v1"
        self.headers = {"x-api-key": "EltgJ5G8m44IzwE6UN2Y4B4NjPW77Zk6FJK3lL23"}
        session = requests.Session()

        retries = Retry(total = 3, status_forcelist = [500])
        session.mount('https://', HTTPAdapter(max_retries=retries))
        self.mySession = session


    def main(self):
        # Get outages
        outages_response = self.invoke_get("outages")

        #retry invoke.get
        outages = self.handle_response(outages_response)
        
        # Get device information
        device_info_response = self.invoke_get("site-info/norwich-pear-tree")

        #retry invoke.get
        device_info = self.handle_response(device_info_response)

        # Extract device IDs from device info
        device_ids = self.extract_device_id(device_info)

        # Filter outages based on IDs and begin time
        filtered_data = self.filter_outages(outages, device_ids)

        # Enrich outages with names from the IDs list
        enriched_outages = self.outages_with_name(filtered_data, device_info.get("devices"))

        # Post enriched outages
        post_response = self.invoke_post("site-outages/norwich-pear-tree", enriched_outages)

        # invoke 
        self.handle_response(post_response)


    def invoke_get(self, endpoint):
        return self.mySession.get(f"{self.base_url}/{endpoint}", headers=self.headers)

    def invoke_post(self, endpoint, data):
        return self.mySession.post(f"{self.base_url}/{endpoint}", headers=self.headers, json=data)

    def handle_response(self, response):
        if response.status_code == 200:
            print("Request successful", response.url)
            return response.json()
        else:
            print("Request failed with status code:", response.status_code,"endpoint:", response.url, "message:", response.json()["message"] )
            return None

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

if __name__ == "__main__":
    Kraken().main()