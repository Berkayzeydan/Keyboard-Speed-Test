import requests

def get_words():
    url = "https://random-word-api.herokuapp.com/word"
    params = {"number": 70}

    words = requests.get(url, params=params).json()
    return words

def get_highscore():
    with open("highscore.txt", "r") as file:
        try:
            hs = int(file.read())
        except (FileNotFoundError, ValueError):
            hs = 0
        return hs

def set_higscore(new):
    with open("highscore.txt", "w") as file:
        file.write(f"{new}")
