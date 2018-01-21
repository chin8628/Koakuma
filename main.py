from koakuma_service import KoakumaService
import pprint
import schedule
import time
import queue

class Main:

    lastest_tweet_id = None
    queue_cmd = queue.Queue()

    def __init__(self):
        self.koakuma = KoakumaService()

    def main(self):
        print('run...')
        tweets = self.koakuma.get_koakuma_tweets()

        if len(tweets) > 0:
            for i in range(len(tweets)):
                if tweets[i]['id'] == self.lastest_tweet_id:
                    index = i - 1
                    for j in range(index, -1, -1):
                        self.queue_cmd.put(tweets[j])
                    break
                elif i == len(tweets) - 1 and tweets[i]['id'] != self.lastest_tweet_id:
                    self.queue_cmd.put(tweets[i])

        while self.queue_cmd.qsize() > 0:
            tweet = self.queue_cmd.get(block=False)
            self.koakuma.process_cmd(tweet)
            self.lastest_tweet_id = tweet['id']

    def run(self):
        schedule.every(2).seconds.do(self.main)

        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == '__main__':
    Main().run()
