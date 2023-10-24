import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class Kraken:
    def __init__(self):
        self.base_url = "https://api.krakenflex.systems/interview-tests-mock-api/v1"
        self.headers = {"x-api-key": "EltgJ5G8m44IzwE6UN2Y4B4NjPW77Zk6FJK3lL23"}
        
        self.session = requests.Session()
        retries = Retry(total = 3, status_forcelist = [500], backoff_factor = 1, allowed_methods=frozenset(['GET', 'POST']))
        self.session.mount('https://', HTTPAdapter(max_retries=retries))

    def main(self):
        # Get outages
        outages_response = self.invoke_get("outages")

        #retry invoke.get
        outages = self.handle_response(outages_response)
        
        # Get device information
        device_info_response = self.invoke_get("site-info/norwich-pear-tree")

        #retry invoke.get
        devices_info = self.handle_response(device_info_response)

        # Extract device IDs from device info
        device_ids = self.extract_device_ids(devices_info)

        # Filter outages based on IDs and begin time
        filtered_data = self.filter_outages(outages, device_ids)

        # Enrich outages with names from the IDs list
        enriched_outages = self.enrich_outages_with_names(filtered_data, devices_info.get("devices"))

        # Post enriched outages
        post_response = self.invoke_post("site-outages/norwich-pear-tree", enriched_outages)

        # invoke 
        self.handle_response(post_response)


    def invoke_get(self, endpoint):
        return self.session.get(f"{self.base_url}/{endpoint}", headers=self.headers)

    def invoke_post(self, endpoint, data):
        return self.session.post(f"{self.base_url}/{endpoint}", headers=self.headers, json=data)

    def handle_response(self, response):
        if response.status_code == 200:
            print(f"Request {response.request.method} to endpoint '{response.url}' was successful ({response.status_code})")
            return response.json()
        else:
            print(f"Request {response.request.method} to endpoint '{response.url}' failed with code {response.status_code} and message '{response.json()['message']}'")
            raise Exception("Interrupting execution because call to API failed")
 
    def extract_device_ids(self, site_info):
        devices = site_info["devices"]
        device_ids = []
        for devices_index in devices:
            device_ids.append(devices_index["id"])
        return device_ids

    def filter_outages(self, outages, device_ids):
        interesting_outages = []
        for outage_index in outages:
            begin = outage_index["begin"]
            site_id = outage_index["id"]
            year = begin[:4]
            if int(year) >= 2022 and site_id in device_ids:
                interesting_outages.append(outage_index)  
        return interesting_outages

    def enrich_outages_with_names(self, outages, devices):
        enriched_outages = []
        for current_outage in outages:
            outage_id = current_outage["id"]
            for current_device in devices:
                device_id = current_device["id"]
                if device_id == outage_id:
                    outage_with_name = current_outage
                    outage_with_name["name"] = current_device["name"]
                    enriched_outages.append(outage_with_name)
        return enriched_outages

if __name__ == "__main__":
    Kraken().main()