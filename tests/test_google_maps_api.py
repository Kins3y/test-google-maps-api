import json

from utils.api import Google_maps_api
from utils.checking import Checking

class Test_Create_Place():
    """Class that includes tests for work with loactions"""

    def test_create_new_place(self):
        """Creating, editing and deleting new location"""

        print("POST Method")
        result_post = Google_maps_api.create_new_place() #Method to create new location
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

        print("GET Method")
        result_get = Google_maps_api.get_new_place(place_id) #Method to check created location
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')

        print ("PUT Method")
        result_put = Google_maps_api.edit_new_place(place_id) #Method to update created location
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Checking new address by GET Method")
        result_get = Google_maps_api.get_new_place(place_id) #Method to check created location
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print("DELETE Method")
        result_delete = Google_maps_api.delete_new_place(place_id)  # Method to delete created location
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')


        print("Checking that address is deleted")
        result_get = Google_maps_api.get_new_place(place_id)  # Method to check created location
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        # Checking.check_json_value(result_get, 'msg', 'Delete operation failed, looks like the data doesn't exist')
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')



        print("Testing of creating, editing and deleting new location ended successfully")