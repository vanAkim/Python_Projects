import pandas as pd
import requests
import math
import numpy as np
import io


#=======================================================================================================================
# From infographic_trend_squares.py

def trend_squares(rate_sqr, moving_sqr, empty_motif, filled_motif):
        ''' (number, number, str, str) -> str

        Return an aggregated column of special characters/emojis
        which is proportional in filled_motif by the rate_sqr input
        and empty_motif by the moving_sqr input.

        >>>trend_squares(0,4,"⬛","💟")
        "⬛\n⬛\n⬛\n⬛"
        >>>trend_squares(1,4,"⬛","💟")
        "⬛\n⬛\n⬛\n💟"
        >>>trend_squares(4,4,"⬛","💟")
        "💟\n💟\n💟\n💟"
        '''


        info_col = ""
        for i in range(0,rate_sqr):
                info_col = filled_motif + "\n" + info_col

        info_col = (empty_motif + "\n")*(moving_sqr-rate_sqr) + info_col

        return info_col


def join_trends(trends_sqr, empty_motif, filled_motif):
        ''' (list of str, str, str) -> str

        Return a string visually similar to a matrix of aggregated
        special characters/emojis columns from independant strings
        shaped like columns. Plus a full upper line of empty_motif
        and full lower line of filled_motif.

        >>>join_trends(['⬛\\n⬛\\n⬛\\n⬛\\n', '⬛\\n💟\\n💟\\n💟\\n'],"⬛","💟")
        '⬛⬛
        ⬛⬛
        ⬛💟
        ⬛💟
        ⬛💟
        💟💟'
        '''


        full_bloc = ''
        for i in np.arange(0, len(trends_sqr[0]), 2):
                full_bloc = full_bloc + '\n' + ''.join([fst_el[i] for fst_el in trends_sqr])

        full_bloc = full_bloc[1:len(full_bloc)] # remove 1st "\n"

        len_1line = len(trends_sqr)
        full_bloc = empty_motif*len_1line + "\n" + full_bloc + '\n' + filled_motif*len_1line

        return full_bloc


def info_bloc(data_byDays, moving_sqr, empty_motif, filled_motif):
        """ (Series of number, number, str, str) -> str

        Return a string visually similar to a matrix of aggregated
        special characters/emojis columns which each column is
        proportional in empty_motif by the input number values.

        >>>data_byDays = pd.Series([199,167,413])
        >>>info_bloc(data_byDays, 2,"⬛","💟")
        '⬛⬛⬛
        ⬛⬛💟
        ⬛⬛💟
        💟💟💟'
        """

        ## Round up all values with specific function
        data_byDays_scale = data_byDays.apply(lambda x: (x - min(data_byDays)) / (max(data_byDays) - min(data_byDays)))

        ## Create infographic bloc
        unit_bySquare = max(data_byDays_scale) / moving_sqr

        data_byDays_scale = data_byDays_scale.apply(dot3of5, args=(unit_bySquare,))

        relativ_rate = data_byDays_scale.apply(lambda x: int(x * moving_sqr))  # by number of squares: (0 3 2 etc)
        relativ_rate = relativ_rate.apply(trend_squares,
                                          args=(moving_sqr,
                                                empty_motif,
                                                filled_motif)).tolist()  # transformed into str columns: ['⬛\n⬛\n', '⬛\n💟\n', etc]

        return join_trends(relativ_rate,
                           empty_motif,
                           filled_motif)  # transformed into full infographic bloc


#=======================================================================================================================
# From dot_round.py

def dot3of5(x,limit):
        """ number -> number

        Return a rounded number bounded to 0.6 of limit.

        >>>dot3of5(76,25)
        75
        >>>dot3of5(89,25)
        75
        >>>dot3of5(90,25)
        100
        >>>dot3of5(94,25)
        100
        """


        if x < (x//limit) * limit + 3*limit/5:
                return (x//limit) * limit

        else:
                return (x//limit) * limit + limit


#=======================================================================================================================
# From write-pattern-twit.py


#-----------------------------------------------------------------------------------------------------------------------
## Download dataframe

url = "https://www.data.gouv.fr/fr/datasets/r/f335f9ea-86e3-4ffa-9684-93c009d5e617" # URL stable
myfile = requests.get(url)
open('data/table-indicateurs-open-data-france.csv', 'wb').write(myfile.content)


## Load overall dataframe
df = pd.read_csv('data/table-indicateurs-open-data-france.csv')


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