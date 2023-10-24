# Kraken 
Krakenflex back end exercise

## Install the request library

bash
:pip3 install requests (for python 3.xx)
pip install requests (for previous python versions)

## Files

kraken_main.py contains the main code to run for this project 
class_endpoint.py contains main code organised in classes
kraken_main_class.py contains code t be executed
test.py contains unit tests

## Usage

to post to `/site-outages/norwich-pear-tree` all outages from the `GET /outages` endpoint that began after`2022-01-01T00:00:00.000Z` and with an ID in the list of devices in `GET /site-info/norwich-pear-tree` run kraken_main.py file which imports classes from class_endpoint.py

to test the code run test.py
