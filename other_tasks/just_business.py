import requests
import os
import json

class StarWarsApiCheck():
    """Class for checking Star Wars API"""

    BASE_URL = "https://swapi.dev/api/" # Base API url
    PEOPLE_ENDPOINT = "people/" # People's endpoint
    FILMS_ENDPOINT = "films/" # Films' edpoint

    def __init__(self):
        """Here we are saving our needs"""
        self.films_url = []
        self.all_cast = set()
        self.all_characters = set()

    def get_darth_films_information(self):
        """Method to check info about people via GET request"""

        url = StarWarsApiCheck.BASE_URL + StarWarsApiCheck.PEOPLE_ENDPOINT + "4"
        print(f'Sending GET request to {url}')
        result = requests.get(url)
        info = result.json()
        print (f'Answer: {info}')
        self.films_url = info.get('films', [])
        print (self.films_url)

    def get_cast_of_films(self):

        list_all_cast = []

        for i in self.films_url:
            result = requests.get(i)
            info = result.json()
            cast = info.get('characters')
            list_all_cast.extend(cast)
        self.all_cast = set(list_all_cast)
        print(self.all_cast)
        print(f"Overall {len(self.all_cast)} actors")


    def get_characters_from_films(self):

        list_all_characters = []

        for i in self.all_cast:
            result = requests.get(i)
            info = result.json()
            character = info.get('name')
            list_all_characters.append(character)
        self.all_characters = set(list_all_characters)
        print(self.all_characters)

    def save_characters_to_file(self):
        """Method to save character names to a file"""

        with open("Characters.txt", "w", encoding="utf-8") as file:
            for character in self.all_characters:
                file.write(character + "\n")

        print("Character names saved to Characters.txt")


start = StarWarsApiCheck()
start.get_darth_films_information()
start.get_cast_of_films()
start.get_characters_from_films()
start.save_characters_to_file()

