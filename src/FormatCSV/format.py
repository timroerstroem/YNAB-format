'''
Created on 21 Jul 2016

@author: Tim Rørstrøm
'''
import os
import pandas
from time import sleep

os.chdir(os.path.expanduser('~/Downloads'))


def reformat(account, date_col, text_col, amount_col):
    '''This function uses the pandas library to extract the required
    information from a CSV file from -- presumably -- most Danish banks.
    Does not work with CSV files from:
        Coop Bank
        Forbrugsforeningen
    '''
    account_data = pandas.read_csv(account, sep=';', usecols=[date_col,
                                                              text_col,
                                                              amount_col],
                                   parse_dates=[0], dayfirst=True,
                                   quotechar='"', encoding='ansi', header=0)
    account_data.columns = ['Date', 'Payee', 'Amount']
    # If the amounts column contains commas, replace them with dots. Also
    # remove any thousands separators
    if ',' in str(account_data['Amount'][1]):
        account_data['Amount'] = account_data['Amount'].str.replace('.', '')
        account_data['Amount'] = account_data['Amount'].str.replace(',', '.')

    account_data.to_csv(account, index=False, encoding='utf-8')


for filename in os.listdir('.'):
    if not filename.endswith('.csv'):
        print("Skipping " + filename + "...")
        continue  # skip non-csv files
    print("Reformatting " + filename + "...")
    reformat(filename, 'Dato', 'Tekst', 'Beløb')

sleep(2)
