# Prerequisites

Before running the code, make sure you have the following installed:

Python (>=3.7)
The requests library
You can install the required library using pip:

bash:
pip install requests

# Configuration
The code requires configuration for the Kraken API base URL and an API key. You can set these in the Kraken class constructor:

python
self.base_url = "https://api.krakenflex.systems/interview-tests-mock-api/v1"
self.headers = {"x-api-key": "Your-API-Key-Here"}


# Usage
To use the code, follow these steps:
Run the Kraken.py to:

1)Create an instance of the Kraken class

2)Fetch outage data from the API

3)Fetch device information from the API

4)Extract device IDs from the device information

5)Filter outages based on device IDs and begin time

6)Enrich outages with device names

6)Post the enriched outage data back to the API


python:


if __name__ == "__main__":
  Kraken().main()
    
# Retry Mechanism
The code includes a retry mechanism to handle transient errors when making API requests. It retries a request up to three times in case of a 500 status code.

# Error Handling
The code provides basic error handling for failed API requests. If a request fails, an exception is raised, and the execution is interrupted.

# Testing
The file Kraken_test.py contains unit test code to test the methods in the class Kraken

#API Endpoints
Make sure the API endpoints used in the code match your specific requirements:

outages: Endpoint for fetching outage data.
site-info/norwich-pear-tree: Endpoint for fetching device information.
site-outages/norwich-pear-tree: Endpoint for posting enriched outage data.
