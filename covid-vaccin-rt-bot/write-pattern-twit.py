import pandas as pd
from infographic_trend_squares import *
import requests
import math


## Download dataframe
url = "https://www.data.gouv.fr/fr/datasets/r/f335f9ea-86e3-4ffa-9684-93c009d5e617" # URL stable
myfile = requests.get(url)
open('data/table-indicateurs-open-data-france.csv', 'wb').write(myfile.content)


## Load overall dataframe
df = pd.read_csv('data/table-indicateurs-open-data-france.csv')


## Overall parameters to construct the infographic
days_toCompute = 10
moving_squares = 4  # seems to be the more elegant infographic pattern


#=======================================================================================================================
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

sign_res = "+" if up_pattern else "-"
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

rt_exactNmb = f"Nombre exact depuis 24h: {sign_res}{round(new_hos,2)}%"

rt_sources = f"Sources et données: @SantePubliqueFr @datagouvfr" \
             f"\nhttps://www.data.gouv.fr/fr/datasets/synthese-des-indicateurs-de-suivi-de-lepidemie-covid-19/#_" \
             f"\nhttps://www.data.gouv.fr/fr/datasets/indicateurs-de-suivi-de-lepidemie-de-covid-19/#_"

rt_hosOccRate = rt_expl + '\n' + rt_exactNmb + '\n' + rt_sources


#=======================================================================================================================
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
sign_res = "+" if up_pattern else "-"
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

rt_exactNmb = f"Nombre exact depuis 24h: {sign_res}{new_hos}"

rt_sources = f"Sources et données: @SantePubliqueFr @datagouvfr" \
             f"\nhttps://www.data.gouv.fr/fr/datasets/synthese-des-indicateurs-de-suivi-de-lepidemie-covid-19/#_"

rt_hosPpl = rt_exactNmb + '\n' + rt_sources


#=======================================================================================================================
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

sign_res = "+" if up_pattern else "-"
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

rt_exactNmb = f"Nombre exact depuis 24h: {sign_res}{new_hos}"

rt_sources = f"Sources et données: @SantePubliqueFr @datagouvfr" \
             f"\nhttps://www.data.gouv.fr/fr/datasets/synthese-des-indicateurs-de-suivi-de-lepidemie-covid-19/#_"

rt_dcHos = rt_exactNmb + '\n' + rt_sources


print(infographic_hosOccRate)
print(rt_hosOccRate)

print(infographic_hosPpl)
print(rt_hosPpl)

print(infographic_dcHos)
print(rt_dcHos)




