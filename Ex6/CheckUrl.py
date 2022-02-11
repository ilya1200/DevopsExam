import time
import urllib.request


def check_url(url: str):
    TIMEOUT_SECONDS: int = 5

    while True:
        if not urllib.request.urlopen(url).getcode() != 200:
            raise Exception("Website is down!")
        time.sleep(TIMEOUT_SECONDS)


if __name__ == '__main__':
    url: str = ""

    with open("url.txt", 'r') as url_file:
        url = url_file.read()
    try:
        check_url(url)
    except:
        print(f"{url} is dead")

