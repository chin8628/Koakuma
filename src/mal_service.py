import spice_api as spice
from key import *

class MalService:

    creds = None

    def __init__(self):
        if self.creds == None:
            self.creds = spice.init_auth(USERNAME, PASSWORD)

    def get_user_anime_list(self):
        return spice.get_list(spice.get_medium('anime'), USERNAME, self.creds)

    def watched_anime(self, anime_title):
        response = self.get_user_anime_list()
        watching_animes = response.medium_list['watching']

        found = False
        for anime in [i for i in watching_animes]:
            if anime.title == anime_title:
                found = True
                break

        if found:
            data = spice.get_blank(spice.get_medium('anime'))
            data.episodes = int(anime.episodes) + 1
            spice.update(data, anime.id, spice.get_medium('anime'), self.creds)
