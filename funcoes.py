import tweepy

import os
import random

from texto import *

from datetime import date, timezone, timedelta, datetime


# horario
def att_data():
    fuso_horario = timezone(timedelta(hours=-3))
    data_e_hora_atuais = datetime.now()
    data_e_hora_sao_paulo = data_e_hora_atuais.astimezone(fuso_horario)
    data = data_e_hora_sao_paulo.strftime('%H:%M')

    return data


def api():
    auth = tweepy.OAuthHandler(os.environ['consumer_key'], os.environ['consumer_secret'])
    auth.set_access_token(os.environ['access_token'], os.environ['access_token_secret'])
    return tweepy.API(auth)


def tweet(api: tweepy.API, message: str, image_path=None):
    if image_path:
        api.update_status_with_media(message, image_path)
    else:
        api.update_status(message)
    print('Tuitado com sucesso!')


def numeros(min, max):
    i = [-1, -1, -1, -1, -1]
    x = 0
    while x < 5:
        aux = random.randint(min, max)
        if aux not in i:
            i[x] = aux
            x = x + 1
    return i


def palavras():
    s_isso = isso.split(',')
    s_aquilo = aquilo.split(',')

    plv = ''
    vc = numeros(0, 99)
    x = 0
    while x < 5:
        # print(vc[x])
        auxx = int(vc[x])
        plv = plv + '\n•' + s_isso[auxx] + ' ou ' + s_aquilo[auxx] + '?'
        x = x + 1
    return plv


def frases():
    s_trechos = trechos.split('/')
    num = random.randint(0, 26)
    plv = '\n"' + s_trechos[num] + '"'
    return plv


def categorias():
    s_adedonha = adedonha.split(',')

    plv = ''
    vc = numeros(0, 30)
    x = 0
    while x < 5:
        # print(vc[x])
        auxx = int(vc[x])
        plv = plv + '\n• 10 x  ' + s_adedonha[auxx] + '.'
        x = x + 1
    return plv


def isso_aquilo():
    # meta = str(random.random()) + str(random.random())
    texto = f"""{att_data()}: ISSO OU AQUILO 

META: 50 comentários 
  {palavras()}

uma resposta = um tweet
COMENTE USANDO AS TAGS
"""
    return texto


def stopots():
    # meta = str(random.random()) + str(random.random())
    texto = f"""{att_data()}: ADEDONHA

META: 100 comentários 
  {categorias()}

uma resposta = um tweet
COMENTE USANDO AS TAGS
"""
    return texto


def trecho():
    # meta = str(random.random()) + str(random.random())
    texto = f"""{att_data()}: Quem disse isso?:     
  {frases()}
"""
    return texto


def esta_na_hora_frase():
    data = att_data()
    if data in hora_frase:
        resp = True
    else:
        resp = False
    return resp


def esta_na_hora_stop():
    data = att_data()
    if data in hora_stop:
        resp = True
    else:
        resp = False
    return resp


def esta_na_hora_isso_aquilo():
    data = att_data()
    if data in hora_isso_aquilo:
        resp = True
    else:
        resp = False
    return resp
