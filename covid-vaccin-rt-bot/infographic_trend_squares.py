import numpy as np
import pandas as pd
from dot_round import *


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

        >>>join_trends(['⬛\n⬛\n⬛\n⬛\n', '⬛\n💟\n💟\n💟\n'],"⬛","💟")
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