import time
import requests

from player import Mp3Player, PlayerListener
from requests.exceptions import ConnectionError


class RequestConsumer(object):

    class Mp3Listener(PlayerListener):
        def __init__(self, winstance):
            self._winstance = winstance
        def onStop(self):
            self._winstance.onStop()
            if self._winstance.is_background:
               self._winstance.start()

    def __init__(self, song_path, is_background):
        self._song_path = song_path
        self._is_background = is_background
        self._player = Mp3Player()
        self._listener = RequestConsumer.Mp3Listener(self)
        self._player.attachListener(self._listener)

    @property
    def is_background(self):
        return self._is_background

    def start(self):
        self._player.play(self._song_path)

    def shutdown(self):
        self.onStop()

    def onStop(self):
        self._player.shutdown()


class Worker(object):

    def __init__(self):
        self._consumers = []
        self._bgconsumer = None
        self._run = False

    def requestSong(self):
        """try:
            r = requests.get('http://localhost:8000/api/v1/requests/next')
            if r.status_code == 200:
                song_json = r.json()
                if 'path' in song_json:
                    RequestConsumer(song_json['path']).start()
            else:
                self.onFetchingFail()
        except ConnectionError:
            self.onFetchingFail()"""
        self.consume('/Users/astagi/w/xmasatm/audio/beer.mp3', True)
        time.sleep(3)
        self.consume('/Users/astagi/w/xmasatm/audio/cup.mp3')
        time.sleep(10)
        self.consume('/Users/astagi/w/xmasatm/audio/back.mp3', True)
        time.sleep(3)

    def consume(self, path, is_background=False):
        consumer = RequestConsumer(path, is_background)
        old_bgconsumer = None
        if is_background:
            if self._bgconsumer:
                old_bgconsumer = self._bgconsumer
            self._bgconsumer = consumer
        else:
            self._consumers.append(consumer)
        consumer.start()
        if old_bgconsumer:
            time.sleep(3)
            old_bgconsumer.shutdown()

    def onFetchingFail(self):
        time.sleep(10)
        self.requestSong()

    def start(self):
        self._run = True
        while self._run:
            self.requestSong()
            time.sleep(5)

    def stop(self):
        self._run = False
        for consumer in self._consumers:
            consumer.shutdown()


if __name__ == '__main__':
    try:
        worker = Worker()
        worker.start()
    except Exception as ex:
        print (ex)
        worker.stop()
