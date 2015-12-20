import os
import subprocess
import threading
import time

from .player import Player


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
        try:
            while self.run:
                time.sleep(1)
                line = self.p.stdout.readline()
                while(self.run and line):
                    line = self.p.stdout.readline()
                    if(line == '@P 3\n'):
                        self.player.stop()
        except Exception as ex:
            print ('Exception on readline')
            print (ex)
            self.player.stop()

class Mp3Player(Player):

    def play(self, source):
        self.source = source
        self.p = subprocess.Popen(['mpg321', '-R', 'anyword'],
            stdin=subprocess.PIPE, stderr=subprocess.PIPE,
            stdout=subprocess.PIPE)
        if not os.path.exists(source):
            return
        self._send_command('LOAD {0}'.format(self.source))
        self.auto_detect_thread = AutoDetectThread()
        self.auto_detect_thread.attachPlayer(self)
        self.auto_detect_thread.start()
        Player.play(self, source)

    def resume(self):
        self._send_command('PAUSE')
        Player.resume(self)

    def stop(self):
        self._send_command('STOP')
        self.auto_detect_thread.stop()
        Player.stop(self)

    def pause(self):
        self._send_command('PAUSE')
        Player.pause(self)

    def shutdown(self):
        self._send_command('QUIT')
        self._recycle_pid()
        Player.shutdown(self)

    def _send_command(self, command):
        try:
            self.p.stdin.write('{0}\n'.format(command))
        except Exception as ex:
            print ('Exception on send command')
            print (ex)

    def _recycle_pid(self):
        while True:
            try:
                pid, status, _ = os.wait3(os.WNOHANG)
                if pid == 0:
                    break
            except OSError as ex:
                break
