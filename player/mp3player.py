import os
from .player import Player
import subprocess
import threading
import time

# Implementation based on mpg321 remote controlled
# https://github.com/e3c/mpg321/blob/master/README.remote

class AutoDetectThread(threading.Thread):
    def attachPlayer(self, player):
        self.player = player
        self.p = player.p
    def stop(self):
        self.run = False
    def run(self):
        self.run = True
        while self.run:
            time.sleep(1)
            line = self.p.stdout.readline()
            while(self.run and line):
                line = self.p.stdout.readline()
                if(line == '@P 3\n'):
                    self.player.stop()

class Mp3Player(Player):

    def play(self, source):
        self.source = source
        self.p = subprocess.Popen(['mpg321', '-R', 'anyword'],
            stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        if not os.path.exists(source):
            return
        self.p.stdin.write('LOAD {0}\n'.format(self.source))
        self.auto_detect_thread = AutoDetectThread()
        self.auto_detect_thread.attachPlayer(self)
        self.auto_detect_thread.start()
        Player.play(self, source)

    def resume(self):
        self.p.stdin.write('PAUSE\n')
        Player.resume(self)

    def stop(self):
        self.p.stdin.write('STOP\n')
        self.auto_detect_thread.stop()
        Player.stop(self)

    def pause(self):
        self.p.stdin.write('PAUSE\n')
        Player.pause(self)

    def shutdown(self):
        self.p.stdin.write('QUIT\n')
        Player.shutdown(self)
