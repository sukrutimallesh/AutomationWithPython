import requests


def save_webpage(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(save_path, 'wb') as file:
            file.write(response.content)

        print(f"Webpage downloaded successfully and saved to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while downloading the webpage: {e}")


if __name__ == "__main__":
    url = "https://www.formula1.com/en/latest/article.2021-car-revealed-as-fia-and-f1-present-regulations-for-the" \
          "-future.3ZkeTsu1sNCrFGP1HI9KVy.html"
    save_path = "formula1_article.html"

    save_webpage(url, save_path)
