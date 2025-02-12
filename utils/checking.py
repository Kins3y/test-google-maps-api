"""Methods to check responses"""
import json


class Checking():

    @staticmethod
    def check_status_code(response, status_code):
        """Method to check status code"""

        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Success!!! Status code = " + str(response.status_code))
        else:
            print("ERROR!!! Status code = " + str(response.status_code))

    @staticmethod
    def check_json_token(response, expected_value):
        """Method of checking required arguments"""

        token = json.loads(response.text)
        assert list(token) == expected_value
        print("All arguments are existing")

    @staticmethod
    def check_json_value(response, field_name, expected_value):
        """Method to check values of required arguments"""

        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + " is correct!")

    @staticmethod
    def check_json_search_word_in_value(response, field_name, search_word):
        """Method to check values of required arguments with specific word"""

        check = response.json()

        check_info = check.get(field_name)
        if search_word in check_info:
            print("Word " + search_word + " is found!")
        else:
            print("Word " + search_word + " not found!")
