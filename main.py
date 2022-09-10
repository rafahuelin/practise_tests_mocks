import requests


def len_joke():
    joke = get_joke()
    return len(joke)


def get_joke():
    url = "http://api.icndb.com/jokes/random"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        return "No jokes"
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.HTTPError as e:
        status_code = response.status_code
        if status_code in [503, 504]:
            # do something
            pass
        else:
            # do something
            pass
        return "HTTPError was raised"

    if response.status_code == 200:
        joke = response.json()["value"]["joke"]
    else:
        joke = "No jokes"

    return joke


if __name__ == "__main__":
    print(get_joke())
