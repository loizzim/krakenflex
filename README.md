# Prerequisites

Before running the code, make sure you have the following installed:

* Python 3.8.0
* Requests (info about installation can be found at https://requests.readthedocs.io/)

# Configuration
The code requires configuration for the Kraken API base URL and API key. You can set these in the Kraken class constructor:

```python
self.base_url = "https://api.krakenflex.systems/interview-tests-mock-api/v1"
self.headers = {"x-api-key": "Your-API-Key-Here"}
```

# Usage
To run the code execute: `python kraken.py`
The execution will:

1) Create an instance of the Kraken class

2) Fetch outages data from the API

3) Fetch devices information from the API

4) Extract device IDs from the devices information

5) Filter outages based on device ID and begin timestamp

6) Enrich outages with device names

7) Post the enriched outage data back to the API

To run the tests execute: `python kraken_test.py`
    
# Retry Mechanism
The code includes a retry mechanism to handle failure responses when the API returns a 500 HTTP response code. It retries the request up to three times.

# Errors
The code raises an exception if the API returns HTTP status code which is not successful (200) and different from 500. It also raises an exception if the maximum number of retries has been performed without a successful response.

# Improvements
- The API key shouldn't be committed as it is considered sensitive data. I have left it there for the purpose of this exercise.
- Log statements to keep track of the code flow.
- Improve test coverage.
