# -*- coding: utf-8 -*-
"""
Calcul monnaie à rendre
L.Ferhi
11.01.2021
"""
import pandas as pd
import numpy as np

df = pd.read_csv('bank.csv')
df['change'] = None # instanciate column

def max_quantity(remain, coin, qty):
    """
    Calculate max quantity of a coin type to give change
    """
    max_qty = 0
    while remain >= coin and qty - max_qty > 0:
        remain = remain-coin
        max_qty += 1
    return max_qty

def change_calc(total, df=df):
    """
    Calculate the total quantity of coin types to give change
    """
    # Case if not enough money
    if np.sum(df.value*df.quantity) < total:
        print('Pas assez d\'argent...')
        return None
    # load inputs
    bank=df.to_dict('index')
    total_change = []
    remain = total # initiate remain
    # Loop over all coin types
    for row in bank:
        coin = bank[row]['value']
        qty = bank[row]['quantity']
        max_qty = max_quantity(remain, coin, qty)
        remain = remain - coin*max_qty
        total_change.append(max_qty)
    # Returns df with chnage and remaining quantity
    df.change = total_change
    df['remain'] = df.quantity - df.change
    return df
    
if __name__ == '__main__':
    # calculate change to an input total
    cost = float(input('Somme due ?'))
    client_paid = float(input('Somme donnée par le client ?'))
    # Calculate the sum to give back
    user_total = round(client_paid - cost,2)
    if user_total == 0:
        print('Il y a l\'appoint !')
    elif user_total < 0:
        print('Il en manque !')
    else:
        df_change = change_calc(user_total)
        print('\nRendre {} euros\n'.format(user_total))
        print(df[['money','change']][df.change != 0])
