import requests

URL = 'http://shibe.online/api/shibes?count=[1]'


def __check_valid_response_code(request):
    if request.status_code == 200:
        return request.json()

    return False


def get_shibe():
    request = requests.get(URL)
    data = __check_valid_response_code(request)

    return data