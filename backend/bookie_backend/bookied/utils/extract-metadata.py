import hashlib
import requests
from bs4 import BeautifulSoup
from typing import Optional
from io import BytesIO
import urllib


def extract_metadata(url) -> Optional[dict]:
    # if url is None:
    #     return

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        title = soup.find("title")
        description = soup.find("meta", property="og:description")
        # Get base url
        base_url = urllib.parse.urlparse(url).hostname
        req = requests.get(f"https://favicongrabber.com/api/grab/{base_url}")
        icons = req.json()["icons"]
        for icon in icons:
            if icon["src"].endswith(".ico"):
                fav_url = icon["src"]
                break

        if fav_url:
            favicon = requests.get(fav_url).content

        return {
            "title": title.string if title else None,
            "description": description["content"] if description else None,
            "favicon": favicon if favicon else None,
            "favicon_hash": md5(favicon),
            "url": url,
        }
    except Exception as e:
        print(e)
        return None


def md5(content) -> Optional[str]:
    if content is None:
        return
    content = BytesIO(content)
    md5 = hashlib.md5()
    md5.update(content.read())
    return md5.hexdigest()


if __name__ == "__main__":
    meta = extract_metadata("https://www.youtube.com/watch?v=9bZkp7q19f0")
    from pathlib import Path

    # save favicon
    favicon = meta["favicon"]
    if favicon:
        print(md5(favicon))
