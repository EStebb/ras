# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 14:44:26 2018

@author: emst
"""

def ras(seed, goal):
    """ Pass the RAS algorithm for a given n x m seed matrix and n x m goal matrix"""
    import numpy as np
    import pandas as pd

    # Initialise
    goal_get_total = np.array(goal.iloc[:, -1])
    goal_getc_total = np.array(goal.iloc[-1, :])
    goal_row_totals = np.delete(goal_get_total, len(goal_get_total)-1)
    goal_col_totals = np.delete(goal_getc_total, len(goal_getc_total)-1)
    matrix = np.array(seed)

    # Replace zeros and blank so division does not create errors
    matrix = np.nan_to_num(matrix)
    goal_col_totals = np.nan_to_num(goal_col_totals)
    goal_row_totals = np.nan_to_num(goal_row_totals)
    matrix[matrix == 0] = 0.0000000001
    goal_col_totals[goal_col_totals == 0] = 0.0000000001
    goal_row_totals[goal_row_totals == 0] = 0.0000000001

    # Iterate until total GDP is within tolerance
    count = 1
    while abs(count) > 0.99:
        # Row update
        row_scalars = matrix.sum(axis=1)/goal_row_totals
        matrix = (matrix.T/row_scalars).T

        # Column update
        col_scalars = matrix.sum(axis=0)/goal_col_totals
        matrix = (matrix/col_scalars)
        count = np.sum(matrix)-np.sum(goal_col_totals)

    global goal_new
    goal_new = pd.DataFrame(matrix)
    goal_new.to_excel('RAS.xlsx', 'goal')
    return goal_new
    