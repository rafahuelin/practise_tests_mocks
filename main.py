import requests


def len_joke():
    joke = get_joke()
    return len(joke)


def get_joke():
    url = "http://api.icndb.com/jokes/random"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        joke = response.json()["value"]["joke"]
        if not 400 <= response.status_code < 600:
            return joke
    except requests.exceptions.Timeout:
        joke = "No jokes"
    except requests.exceptions.ConnectionError:
        joke = "No jokes"
    else:
        joke = "No jokes"
    return joke


if __name__ == "__main__":
    print(get_joke())
