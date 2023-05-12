import requests
import sys


class PropertyCLI:
    url = 'https://api.stagingeb.com/v1/properties'

    def __init__(self, token):
        self.headers = {
            "accept": "application/json",
            "X-Authorization": token
        }

    def list(self):
        response = requests.get(self.url, headers=self.headers)
        response_status = response.status_code
        if response_status == 200:
            response_json = response.json()
            content = response_json.get('content')

            for row in content:
                print(row.get('title'))
            return response.json()
        elif response_status == 401:
            print('El api key no es invalida')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        my_argument = sys.argv[1]
        cli = PropertyCLI(my_argument)
        cli.list()
    else:
        print("Debes añadir el api key\nEj. python main.py l7u502p8v46ba3ppgvj5y2aad50lb9")
