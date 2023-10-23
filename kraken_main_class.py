from class_endpoint import Kraken

# initialise an instance of the class Kraken
instance = Kraken()

#call outages and get_device info  methods to get respectively the outages and devices lists

outages = instance.invoke_get("outages")
get_devices= instance.invoke_get("site-info/norwich-pear-tree")


# call the extract_device_id method to extract the ids from the device info list 
device_ids =instance.extract_device_id(get_devices)



# filter the outages list based on the begin date and if the ids is present in the devices id list 
filtered_data = instance.filter_outages(outages,device_ids)

# enrich the filtered outages list with the name object from the devices id info, based on common ids
instance.outages_with_name(filtered_data, get_devices["devices"])

# call the invoke post method to post the enriched outages list 
post = instance.invoke_post("site-outages/norwich-pear-tree",filtered_data)


