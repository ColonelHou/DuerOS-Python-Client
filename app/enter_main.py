# -*- coding: utf-8 -*-
from sdk.dueros_core import DuerOS

import sys
import logging
from framework.mic import Audio
from framework.player import Player

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

audio = Audio()
player = Player()
dueros = DuerOS(player)

audio.link(dueros)

dueros.start()
audio.start()

while True:
    try:
        try:
            input('press ENTER to talk\n')
        except SyntaxError:
            pass

        dueros.listen()
    except KeyboardInterrupt:
        break

dueros.stop()
audio.stop()
