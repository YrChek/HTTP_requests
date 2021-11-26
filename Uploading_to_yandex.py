import os
import requests


class YaUploader:
    def __init__(self, token, path):
        self.token = token
        self.path = path

    def get_headers(self):
        """Прописываем заголовки"""
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'}

    def upload(self):
        """Получаем ссылку на запись и записывам файлы на Яндекс диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        my_list = os.listdir(self.path)
        for name_file in my_list:
            params = {"path": name_file, "overwrite": "true"}
            response = requests.get(upload_url, headers=headers, params=params)
            print(response.status_code)
            response = response.json()
            href = response.get("href")
            full_path = os.path.join(self.path, name_file)
            with open(full_path, 'rb') as f:
                respon = requests.put(href, files={'file': f})
            print(respon)


if __name__ == '__main__':
    my_token = 'AQAAAAAtrpb1AADLW9d3Mv1vH0IphQHB3SiW7_o'
    my_path = os.path.join('C:/', 'Users', 'NoName', 'Desktop', 'Папка для загрузки')

    uploader = YaUploader(my_token, my_path)
    uploader.upload()
