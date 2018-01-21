from api import Api
from setting import *
from mal_service import MalService

class KoakumaService:

    api = None
    lastest_cmd = None
    mal_service = None

    def __init__(self):
        if self.api == None:
            self.api = Api()

        if self.mal_service == None:
            self.mal_service = MalService()

    def get_koakuma_tweets(self):
        """
        Args:
            response (Dict): user_timeline api's response

        Returns:
            Dict: response which has only tweet about koakuma
        """
        response = self.api.get_user_timeline()
        koakuma_only = [tweet for tweet in response if tweet['text'].split()[0] == BOT_NAME]
        return koakuma_only

    def process_cmd(self, koakuma_response):
        tweet_text = koakuma_response['text']
        cmd = tweet_text.split()[1]

        if cmd == CMD_WATCHED:
            anime = ' '.join([i for i in tweet_text.split()[2:]])

            # Debug tweet by typing ' kt [whateveryouwant]' after anime title
            # because of duplicate tweet prevention of twitter
            anime = anime.split(' kt ')[0]

            self.mal_service.watched_anime(anime)


