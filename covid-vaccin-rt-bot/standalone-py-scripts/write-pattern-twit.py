import pandas as pd
from infographic_trend_squares import *
import requests
import math
import io


## Download dataframe
url = "https://www.data.gouv.fr/fr/datasets/r/f335f9ea-86e3-4ffa-9684-93c009d5e617" # URL stable
myfile = requests.get(url)
open('../data/table-indicateurs-open-data-france.csv', 'wb').write(myfile.content)


## Load overall dataframe
df = pd.read_csv('../data/table-indicateurs-open-data-france.csv')


## Overall parameters to construct the infographic
days_toCompute = 10
moving_squares = 4  # seems to be the more elegant infographic pattern


#-----------------------------------------------------------------------------------------------------------------------
# Tension hospitalière sur la capacité en réanimation

## Parameters to construct the infographic
empty_pattern = "⬛"
filled_pattern = "💟"
down_pattern = "📉"
up_pattern = "📈"


## Get only the required values from data
rate_days = df.loc[df.shape[0] - days_toCompute: df.shape[0] + 1,
             "TO"]

## Turn propotions into %
rate_days = rate_days.apply(lambda x: x*100)


## Create infographic bloc
infographic_hosOccRate = info_bloc(rate_days,
                               moving_squares,
                               empty_pattern,
                               filled_pattern)


## Adding some top lines to emphasize the infographic
title_line = "Tension hospitalière sur la capacité en réanimation"

orange = '🟠'
red = '🔴'
green = '🟢'

trend_res = up_pattern if rate_days.iloc[-1] > rate_days.iloc[-2] else down_pattern
color_res = red if rate_days.iloc[-1] > 60 else (green if rate_days.iloc[-1] < 30 else orange)

sign_res = "+" if trend_res ==  up_pattern else "-"
new_hos = abs(rate_days.iloc[-1] - rate_days.iloc[-2])

today_line = f"{df.loc[df.shape[0]-1, 'date']}: {color_res} {round(rate_days.iloc[-1], 2)}% {trend_res}"

lstDays_line = f"{days_toCompute} derniers jours: Min {round(min(rate_days),2)}% Max {round(max(rate_days),2)}%"

lgdSqr_line = f"{filled_pattern}≈ +{round((max(rate_days) - min(rate_days))/moving_squares,2)}%"


## Wrap-up
infographic_hosOccRate = title_line + '\n\n' +\
                         today_line + '\n\n' +\
                         lstDays_line + '\n' +\
                         lgdSqr_line + '\n\n' +\
                         infographic_hosOccRate

## Following up tweet with sources

rt_expl = "Proportion de patients atteints de COVID-19 actuellement en réanimation, en soins intensifs, " \
          "ou en unité de surveillance continue rapportée au total des lits en capacité initiale, c’est-à-dire " \
          "avant d’augmenter les capacités de lits de réanimation dans un hôpital"

rt_exactNmb = f"Différence exacte depuis 24h: {sign_res}{round(new_hos,2)}%"

rt_sources = f"Sources et données: @SantePubliqueFr @datagouvfr" \
             f"\nhttps://www.data.gouv.fr/fr/datasets/synthese-des-indicateurs-de-suivi-de-lepidemie-covid-19/#_" \
             f"\nhttps://www.data.gouv.fr/fr/datasets/indicateurs-de-suivi-de-lepidemie-de-covid-19/#_"

rt_hosOccRate = rt_expl + '\n' + rt_exactNmb + '\n' + rt_sources


#-----------------------------------------------------------------------------------------------------------------------
# Nombre de patients actuellement hospitalisés pour COVID-19


## Parameters to construct the infographic
empty_pattern = "⬛"
filled_pattern = "🥼"
down_pattern = "📉"
up_pattern = "📈"


## Get only the required values from data
rate_days = df.loc[df.shape[0] - days_toCompute: df.shape[0] + 1,
             "hosp"].astype(int)


## Create infographic bloc
infographic_hosPpl = info_bloc(rate_days,
                               moving_squares,
                               empty_pattern,
                               filled_pattern)


## Adding some top lines to emphasize the infographic
title_line = "Patients hospitalisés pour COVID-19"

trend_res = up_pattern if rate_days.iloc[-1] > rate_days.iloc[-2] else down_pattern
sign_res = "+" if trend_res == up_pattern else "-"
new_hos = abs(rate_days.iloc[-1] - rate_days.iloc[-2])
today_line = f"{df.loc[df.shape[0]-1, 'date']}: {rate_days.iloc[-1]} {trend_res}"

lstDays_line = f"{days_toCompute} derniers jours: Min {min(rate_days)} Max {max(rate_days)}"

lgdSqr_line = f"{filled_pattern}≈ +{math.floor((max(rate_days)-min(rate_days))/moving_squares)}"


## Wrap-up
infographic_hosPpl = title_line + '\n\n' +\
                         today_line + '\n\n' +\
                         lstDays_line + '\n' +\
                         lgdSqr_line + '\n\n' +\
                         infographic_hosPpl


## Following up tweet with sources

rt_expl = ""

rt_exactNmb = f"Différence exacte depuis 24h: {sign_res}{new_hos}"

rt_sources = f"Sources et données: @SantePubliqueFr @datagouvfr" \
             f"\nhttps://www.data.gouv.fr/fr/datasets/synthese-des-indicateurs-de-suivi-de-lepidemie-covid-19/#_"

rt_hosPpl = rt_exactNmb + '\n' + rt_sources


#-----------------------------------------------------------------------------------------------------------------------
# Nouveaux patients décédés à l’hôpital au cours des dernières 24h pour cause de COVID-19


## Parameters to construct the infographic
empty_pattern = "⬛"
filled_pattern = "⚰"
down_pattern = "📉"
up_pattern = "📈"


## Get only the required values from data
rate_days = df.loc[df.shape[0] - days_toCompute: df.shape[0] + 1,
             "incid_dchosp"].astype(int)


## Create infographic bloc
infographic_dcHos = info_bloc(rate_days,
                              moving_squares,
                              empty_pattern,
                              filled_pattern)


## Adding some top lines to emphasize the infographic
title_line = "Décès à l’hôpital pour COVID-19 (hors EHPAD/ESMS)"

trend_res = up_pattern if rate_days.iloc[-1] > rate_days.iloc[-2] else down_pattern

sign_res = "+" if trend_res == up_pattern else "-"
new_hos = abs(rate_days.iloc[-1] - rate_days.iloc[-2])

today_line = f"{df.loc[df.shape[0]-1, 'date']}: {rate_days.iloc[-1]} {trend_res}"

lstDays_line = f"{days_toCompute} derniers jours: Min {min(rate_days)} Max {max(rate_days)}"

lgdSqr_line = f"{filled_pattern}: +{math.floor((max(rate_days) - min(rate_days))/moving_squares)}"


## Wrap-up
infographic_dcHos = title_line + '\n\n' +\
                         today_line + '\n\n' +\
                         lstDays_line + '\n' +\
                         lgdSqr_line + '\n\n' +\
                         infographic_dcHos


## Following up tweet with sources

rt_expl = ""

rt_exactNmb = f"Différence exacte depuis 24h: {sign_res}{new_hos}"

rt_sources = f"Sources et données: @SantePubliqueFr @datagouvfr" \
             f"\nhttps://www.data.gouv.fr/fr/datasets/synthese-des-indicateurs-de-suivi-de-lepidemie-covid-19/#_"

rt_dcHos = rt_exactNmb + '\n' + rt_sources


twit_txtfile = infographic_hosOccRate + '\n' + rt_hosOccRate + '\n' +\
               infographic_hosPpl + '\n' + rt_hosPpl + '\n' + \
               infographic_dcHos + '\n' + rt_dcHos


with io.open('tweets.txt', 'w', encoding='utf8') as f:
    f.write(twit_txtfile)


# 1st and major usage : Post daily tweets about COVID-19 data of last 24h and 7days from public french database. Most of the content of the main tweets will be shaped as infographics with emojis.
# 2nd and minor usage : Retweet similar content, currently I'm thinking mostly about another french bot daily tweeting about vaccination process in France.
#
# 1: A python script will collect and transform data into a message intended to be tweeted with daily updates. In addition, each of these tweets will be retweeted to provided the data sources.
# 2: Another python script should retweet content (tweets) from others with similar content of this project.