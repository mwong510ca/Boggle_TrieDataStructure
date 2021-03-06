"""
" Timer is the timer object for appBoggle.  It is a separate QThread
" to send the remaining time of the game to the main application.
"
" author Meisze Wong
"        www.linkedin.com/pub/macy-wong/46/550/37b/
"        github.com/mwong510ca/Boggle_TrieDataStructure
"""

# !/usr/bin/env python3

import time
from PyQt5.QtCore import pyqtSignal, QThread


class Timer(QThread):
    currentTime = pyqtSignal(str)
    timesUp = pyqtSignal()

    def __init__(self):
        super(Timer, self).__init__()
        self._isRunning = True
        self._timeRemaining = 0

    def run(self):
        if not self._isRunning:
            self._isRunning = True

        while self._isRunning and self._timeRemaining > 0:
            self.currentTime.emit("Time: " + str(self._timeRemaining/10) + "s")
            time.sleep(0.1)
            self._timeRemaining -= 1

        if self._isRunning:
            self.stop()
            self.timesUp.emit()

    def setTimer(self, minute):
        self._timeRemaining = minute * 60 * 10

    def isRunning(self):
        return self._isRunning

    def stop(self):
        self._isRunning = False
