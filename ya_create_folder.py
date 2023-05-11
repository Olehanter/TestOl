
import os
import requests
import json
from setting import TOKEN

class Yandex:
    host = 'https://cloud-api.yandex.net/'
    url = "/v1/disk/resources/"

    def __init__(self, token):
        self.token = token
        self.folder_name = 'Photo'

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'}

    def create_folders(self, folder_name):
        uri = 'v1/disk/resources/'
        url = self.host + uri
        headers = self.get_headers()
        # count_folder += 1
        self.folder_name = folder_name
        params = {'path': f'/{self.folder_name}'}
        response = requests.put(url, headers=headers, params=params)
        # print(response.json())
        return response.status_code


ya = Yandex(TOKEN)

if __name__ == '__main__':
    print(ya.create_folders(input('Folder name? :')))
