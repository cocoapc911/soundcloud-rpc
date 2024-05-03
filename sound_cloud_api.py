import requests
import json
from bs4 import BeautifulSoup

BASE_URL = "https://api-v2.soundcloud.com"

class Soundcloud:

    def __init__(self, o_auth, client_id):
        if len(client_id) != 32:
            raise ValueError("Client_IDの形式が間違っています。")
        self.client_id = client_id
        self.o_auth = o_auth
        json_versions = dict(requests.get("https://product-details.mozilla.org/1.0/firefox_versions.json").json())
        firefox_version = json_versions.get('LATEST_FIREFOX_VERSION')
        self.headers = {"Authorization" : o_auth, "Accept": "application/json","User-Agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{firefox_version}) Gecko/20100101 Firefox/{firefox_version}"}
        app_json = requests.get("https://soundcloud.com/versions.json")
        self.app_version = dict(app_json.json()).get('app')

    def get_now(self):

        req = requests.get(f"{BASE_URL}/me/play-history/tracks?limit=1", headers=self.headers)
        if not req.json()["collection"]:
            raise "No tracks found in play history"
        track_info = req.json()['collection'][0]['track']
        return track_info
