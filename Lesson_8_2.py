import requests
from pprint import pprint


class YaUploader:
    def __init__(self, token: str, url='https://cloud-api.yandex.net/v1/disk/resources'):
        self.token = token
        self.url = url

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_link(self, file_upload_path):
        upload_url = self.url + '/upload'
        params = {
            'path': file_upload_path,
            'overwrite': 'True'
        }
        headers = self.get_headers()
        link = requests.get(url=upload_url, params=params, headers=headers)
        return link.json()

    def upload(self, file_upload_path, file_list):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        create_folder = requests.put(url=f'{self.url}?path={file_upload_path}', headers=self.get_headers())
        for file in file_list:
            folder_path = file_upload_path + file
            href = self._get_link(folder_path)['href']
            response = requests.put(href, data=open(file, 'rb'))
            response.raise_for_status()
            if response.status_code == 201:
                print(f'Success upload {file}')


if __name__ == '__main__':
    path_to_file = 'Netology/'
    token = ''
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    uploader = YaUploader(token=token, url=url)
    uploader.upload(path_to_file, ['Somefile.txt', 'AnotherFile.txt', 'Picture1.jpeg'])
