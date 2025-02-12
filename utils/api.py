from utils.http_methods import Http_methods

"""Methods to test Google Maps API"""

BASE_URL = "https://rahulshettyacademy.com" # Base URL
KEY = "?key=qaclick123" # Parameter for every request

class Google_maps_api():

    """Method to create new location"""
    @staticmethod
    def create_new_place():

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
             ],
            "website": "http://google.com",
            "language": "French-IN"
        }


        post_resource = "/maps/api/place/add/json" # Resource of POST method
        post_url = BASE_URL + post_resource + KEY
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post


    @staticmethod
    def get_new_place(place_id):
        """Method to check new location"""

        get_resource = "/maps/api/place/get/json" # Resource of GET method
        get_url = BASE_URL + get_resource + KEY + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def edit_new_place(place_id):
        """Method to edit new location"""

        put_resource = "/maps/api/place/update/json" # Resource of PUT method
        put_url = BASE_URL + put_resource + KEY
        json_for_update_new_location = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }

        print(put_url)
        result_put = Http_methods.put(put_url, json_for_update_new_location)
        print(result_put.text)
        return result_put

    @staticmethod
    def delete_new_place(place_id):
        """Method to delete new location"""

        delete_resource = "/maps/api/place/delete/json" # Resource of DELETE method
        delete_url = BASE_URL + delete_resource + KEY
        json_for_delete_new_location = {
            "place_id": place_id
        }

        print(delete_url)
        result_delete = Http_methods.put(delete_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete

