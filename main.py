#! /usr/bin/env python
# coding=utf-8
import time
from funcoes import *

if __name__ == '__main__':

    while True:

        print(att_data())

        if esta_na_hora_frase() == True:
            text = trecho()
            mimir = random.randint(120, 2400)
            time.sleep(mimir)
            while len(text) > 275:
                text = trecho()
            print(text)
            api = api()
            tweet(api, text)
        elif esta_na_hora_isso_aquilo() == True:
            text = isso_aquilo()
            while len(text) > 275:
                text = isso_aquilo()
            print(text)
            api = api()
            tweet(api, text)
        elif esta_na_hora_stop() == True:
            text = stopots()
            while len(text) > 275:
                text = stopots()
            print(text)
            api = api()
            tweet(api, text)
        else:
            print('Tá na hora de mimir')

        time.sleep(60)

