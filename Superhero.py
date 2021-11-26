import requests


class Superhero:
    mind = {}

    def __init__(self, name, number=0, host='https://superheroapi.com/api/', url='search', token='2619421814940190'):
        self.name = name
        self.host = host
        self.url = url
        self.token = token
        self.number_on_the_list = number

    def get_data(self):
        """Получение данных с сервера"""
        full_url = f'{self.host}{self.token}/{self.url}/{self.name}'
        response = requests.get(full_url)
        print(response.status_code)
        return response

    def dictionary(self):
        """Определение интелекта"""
        intelligence = int(self.get_data().json()['results'][self.number_on_the_list]['powerstats']['intelligence'])
        if intelligence not in self.mind:
            self.mind[intelligence] = [self.name]
        else:
            self.mind[intelligence].append(self.name)
        return self.mind

    def the_smartest(self):
        """Определение самого умного"""
        key_list = list(self.mind.keys())
        key_list = sorted(key_list)
        value_list = set(self.mind[key_list[-1]])
        value = (' и ').join(value_list)
        return f'Самый умный из супергероев это {value}, с уровнем интелекта {key_list[-1]}'


hulk = Superhero('Hulk')
america = Superhero('Captain America')
thanos = Superhero('Thanos')
hulk.dictionary()
america.dictionary()
thanos.dictionary()
print(hulk.the_smartest())
