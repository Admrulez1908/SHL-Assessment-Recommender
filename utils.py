import requests
from bs4 import BeautifulSoup

def fetch_text_from_url(url):
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join(p.get_text() for p in paragraphs)
        return text
    except Exception as e:
        print(f"Error fetching URL: {e}")
        return ""

def is_url(string):
    return string.startswith("http://") or string.startswith("https://")
