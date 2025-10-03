import requests
from bs4 import BeautifulSoup
#by perlch
def get_last_message(channel_name: str):
    url = f"https://t.me/s/{channel_name}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/117.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    messages = soup.find_all("div", class_="tgme_widget_message_text")
    if not messages:
        return None
    
    return messages[-1].get_text("\n", strip=True)


if __name__ == "__main__":
    try:        
        last_msg = get_last_message("YOUR_CHANNEL_NAME_HERE")
        if last_msg:
            print(last_msg)
        else:
            print("none")
    except Exception as e:
        print(f"oops: {e}")
