import requests


def get_json_from_url(url):

    res = requests.get(url, verify=False)

    # czy udało się poprawnie odpytać adres url?
    if res.status_code != 200:
        return {}

    # przetworzenie odpowiedzi z NBP
    try:
        res_json = res.json()
    except Exception as e:
        return {}

    if isinstance(res_json, list):
        return res_json[0]
    elif isinstance(res_json, dict):
        return res_json
    else:
        return {}
