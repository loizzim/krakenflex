import unittest
from kraken import Kraken

class Test_Kraken(unittest.TestCase):
    def setUp(self):
        self.endpoint = Kraken()

    def test_filter_outages_propoperly_filters_data_based_on_ids_and_date(self):
        #  sample input data from the outages call 
        outages = [
            {'id': '20f6e664-f00e-4621-9ca4-5ec588aadeaf', 'begin': '2023-02-15T11:28:26.965Z', 'end': '2023-12-24T14:20:37.532Z'},
            {'id': '70656668-571e-49fa-be2e-099c67d136ab', 'begin': '2023-01-08T16:29:22.128Z', 'end': '2022-06-09T22:10:59.718Z'}, 
            {'id': '75e96db4-bba2-4035-8f43-df2cbd3da859', 'begin': '2023-05-11T14:35:15.359Z', 'end': '2023-12-27T11:19:19.393Z'}, 
            {'id': '86b5c819-6a6c-4978-8c51-a2d810bb9318', 'begin': '2023-01-16T07:01:50.149Z', 'end': '2022-10-03T07:46:31.410Z'}, 
            {'id': 'a79fe094-087b-4b1e-ae20-ac4bf7fa429b', 'begin': '2021-02-23T11:33:58.552Z', 'end': '2022-12-16T00:52:16.126Z'}
        ]

        device_id_info = ['20f6e664-f00e-4621-9ca4-5ec588aadeaf', '75e96db4-bba2-4035-8f43-df2cbd3da859', '20f6e664-f00e-4621-9ca4-5ec588aadeaf', '75e96db4-bba2-4035-8f43-df2cbd3da859']  
        #`2022-01-01T00:00:00.000Z`
        actual = self.endpoint.filter_outages(outages, device_id_info)

        expected = [
            {'id': '20f6e664-f00e-4621-9ca4-5ec588aadeaf', 'begin': '2023-02-15T11:28:26.965Z', 'end': '2023-12-24T14:20:37.532Z'},
            {'id': '75e96db4-bba2-4035-8f43-df2cbd3da859', 'begin': '2023-05-11T14:35:15.359Z', 'end': '2023-12-27T11:19:19.393Z'}
        ]

        # Check if the correct outages are included in the result, the outages begin > 2022 and with id in devide_id_info
        self.assertEqual(expected,actual)

    def test_filter_outages_returns_empty_list_if_device_ids_is_empty(self):

        device_id =[]
        # sample outages
        outages = [
            {'id': '20f6e664-f00e-4621-9ca4-5ec588aadeaf', 'begin': '2023-02-15T11:28:26.965Z', 'end': '2023-12-24T14:20:37.532Z'},
            {'id': '70656668-571e-49fa-be2e-099c67d136ab', 'begin': '2023-01-08T16:29:22.128Z', 'end': '2022-06-09T22:10:59.718Z'}, 
            {'id': '75e96db4-bba2-4035-8f43-df2cbd3da859', 'begin': '2023-05-11T14:35:15.359Z', 'end': '2023-12-27T11:19:19.393Z'}, 
            {'id': '86b5c819-6a6c-4978-8c51-a2d810bb9318', 'begin': '2023-01-16T07:01:50.149Z', 'end': '2022-10-03T07:46:31.410Z'}, 
            {'id': 'a79fe094-087b-4b1e-ae20-ac4bf7fa429b', 'begin': '2021-02-23T11:33:58.552Z', 'end': '2022-12-16T00:52:16.126Z'}
        ]

        actual = self.endpoint.filter_outages(outages, device_id)
        expected = []
        self.assertEqual(expected,actual)

    def test_filter_outages_returns_empty_list_if_outages_is_empty(self):
        # sample devide_ids and empyt list of outages
        device_id =['20f6e664-f00e-4621-9ca4-5ec588aadeaf', 
                    '75e96db4-bba2-4035-8f43-df2cbd3da859',
                    '20f6e664-f00e-4621-9ca4-5ec588aadeaf', 
                    '75e96db4-bba2-4035-8f43-df2cbd3da859'
                 ]
       
        outages = []

        actual = self.endpoint.filter_outages(outages, device_id)
        expected = []
        self.assertEqual(expected,actual)


    def test_extract_device_id_is_working_properly(self):
    
        #device info data sample
        device_info = {'id': 'norwich-pear-tree', 'name': 'Norwich Pear Tree', 'devices': [
            {'id': '111183e7-fb90-436b-9951-63392b36bdd2', 'name': 'Battery 1'}, 
            {'id': '86b5c819-6a6c-4978-8c51-a2d810bb9318', 'name': 'Battery 2'},
            {'id': '70656668-571e-49fa-be2e-099c67d136ab', 'name': 'Battery 3'},
            {'id': '9ed11921-1c5b-40f4-be66-adb4e2f016bd', 'name': 'Battery 4'},
            {'id': 'a79fe094-087b-4b1e-ae20-ac4bf7fa429b', 'name': 'Battery 5'}, 
            {'id': '0e4d59ba-43c7-4451-a8ac-ca628bcde417', 'name': 'Battery 6'}, 
            {'id': '20f6e664-f00e-4621-9ca4-5ec588aadeaf', 'name': 'Battery 7'}, 
            {'id': '75e96db4-bba2-4035-8f43-df2cbd3da859', 'name': 'Battery 8'}]}

        expected = ['111183e7-fb90-436b-9951-63392b36bdd2', 
                    '86b5c819-6a6c-4978-8c51-a2d810bb9318', 
                    '70656668-571e-49fa-be2e-099c67d136ab', 
                    '9ed11921-1c5b-40f4-be66-adb4e2f016bd', 
                    'a79fe094-087b-4b1e-ae20-ac4bf7fa429b', 
                    '0e4d59ba-43c7-4451-a8ac-ca628bcde417', 
                    '20f6e664-f00e-4621-9ca4-5ec588aadeaf', 
                    '75e96db4-bba2-4035-8f43-df2cbd3da859'
                    ]
        
        actual = self.endpoint.extract_device_id(device_info)
        self.assertEqual(expected,actual)

    def test_outages_with_name_adds_name_from_devices_info_to_outages_list(self):
        
        filtered_outages = [{'id': '0e4d59ba-43c7-4451-a8ac-ca628bcde417', 'begin': '2022-02-15T11:28:26.735Z', 'end': '2022-08-28T03:37:48.568Z'}, 
                            {'id': '111183e7-fb90-436b-9951-63392b36bdd2', 'begin': '2022-01-01T00:00:00.000Z', 'end': '2022-09-15T19:45:10.341Z'},
                            {'id': '111183e7-fb90-436b-9951-63392b36bdd2', 'begin': '2022-02-18T01:01:20.142Z', 'end': '2022-08-15T14:34:50.366Z'}, 
                            {'id': '20f6e664-f00e-4621-9ca4-5ec588aadeaf', 'begin': '2022-02-15T11:28:26.965Z', 'end': '2023-12-24T14:20:37.532Z'}, 
                            {'id': '70656668-571e-49fa-be2e-099c67d136ab', 'begin': '2022-04-08T16:29:22.128Z', 'end': '2022-06-09T22:10:59.718Z'}, 
                            {'id': '75e96db4-bba2-4035-8f43-df2cbd3da859', 'begin': '2023-05-11T14:35:15.359Z', 'end': '2023-12-27T11:19:19.393Z'}, 
                            {'id': '86b5c819-6a6c-4978-8c51-a2d810bb9318', 'begin': '2022-02-16T07:01:50.149Z', 'end': '2022-10-03T07:46:31.410Z'}, 
                            {'id': '86b5c819-6a6c-4978-8c51-a2d810bb9318', 'begin': '2022-05-09T04:47:25.211Z', 'end': '2022-12-02T18:37:16.039Z'},
                            {'id': '9ed11921-1c5b-40f4-be66-adb4e2f016bd', 'begin': '2022-01-12T08:11:21.333Z', 'end': '2022-12-13T07:20:57.984Z'}, 
                            {'id': 'a79fe094-087b-4b1e-ae20-ac4bf7fa429b', 'begin': '2022-02-23T11:33:58.552Z', 'end': '2022-12-16T00:52:16.126Z'}]

        # sample devices ids and names

        devices = [{'id': '111183e7-fb90-436b-9951-63392b36bdd2', 'name': 'Battery 1'}, 
                    {'id': '86b5c819-6a6c-4978-8c51-a2d810bb9318', 'name': 'Battery 2'}, 
                    {'id': '70656668-571e-49fa-be2e-099c67d136ab', 'name': 'Battery 3'}, 
                    {'id': '9ed11921-1c5b-40f4-be66-adb4e2f016bd', 'name': 'Battery 4'},
                    {'id': 'a79fe094-087b-4b1e-ae20-ac4bf7fa429b', 'name': 'Battery 5'},
                    {'id': '0e4d59ba-43c7-4451-a8ac-ca628bcde417', 'name': 'Battery 6'}, 
                    {'id': '20f6e664-f00e-4621-9ca4-5ec588aadeaf', 'name': 'Battery 7'}, 
                    {'id': '75e96db4-bba2-4035-8f43-df2cbd3da859', 'name': 'Battery 8'}
                   ]
        # expected result
        
        expected = [{'id': '0e4d59ba-43c7-4451-a8ac-ca628bcde417', 'begin': '2022-02-15T11:28:26.735Z', 'end': '2022-08-28T03:37:48.568Z', 'name': 'Battery 6'}, 
                    {'id': '111183e7-fb90-436b-9951-63392b36bdd2', 'begin': '2022-01-01T00:00:00.000Z', 'end': '2022-09-15T19:45:10.341Z', 'name': 'Battery 1'}, 
                    {'id': '111183e7-fb90-436b-9951-63392b36bdd2', 'begin': '2022-02-18T01:01:20.142Z', 'end': '2022-08-15T14:34:50.366Z', 'name': 'Battery 1'}, 
                    {'id': '20f6e664-f00e-4621-9ca4-5ec588aadeaf', 'begin': '2022-02-15T11:28:26.965Z', 'end': '2023-12-24T14:20:37.532Z', 'name': 'Battery 7'}, 
                    {'id': '70656668-571e-49fa-be2e-099c67d136ab', 'begin': '2022-04-08T16:29:22.128Z', 'end': '2022-06-09T22:10:59.718Z', 'name': 'Battery 3'}, 
                    {'id': '75e96db4-bba2-4035-8f43-df2cbd3da859', 'begin': '2023-05-11T14:35:15.359Z', 'end': '2023-12-27T11:19:19.393Z', 'name': 'Battery 8'}, 
                    {'id': '86b5c819-6a6c-4978-8c51-a2d810bb9318', 'begin': '2022-02-16T07:01:50.149Z', 'end': '2022-10-03T07:46:31.410Z', 'name': 'Battery 2'}, 
                    {'id': '86b5c819-6a6c-4978-8c51-a2d810bb9318', 'begin': '2022-05-09T04:47:25.211Z', 'end': '2022-12-02T18:37:16.039Z', 'name': 'Battery 2'}, 
                    {'id': '9ed11921-1c5b-40f4-be66-adb4e2f016bd', 'begin': '2022-01-12T08:11:21.333Z', 'end': '2022-12-13T07:20:57.984Z', 'name': 'Battery 4'}, 
                    {'id': 'a79fe094-087b-4b1e-ae20-ac4bf7fa429b', 'begin': '2022-02-23T11:33:58.552Z', 'end': '2022-12-16T00:52:16.126Z', 'name': 'Battery 5'}]
        
        actual = self.endpoint.outages_with_name(filtered_outages, devices)

        self.assertEqual(expected,actual)


if __name__ == '__main__':
    unittest.main()
