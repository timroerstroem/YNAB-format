'''
Created on 21 Jul 2016

@author: Tim Rørstrøm
'''
import os
import pandas
from time import sleep

os.chdir(os.path.expanduser('~/Downloads'))


def reformat(account):
    '''This function uses the pandas library to extract the required
    information from a CSV file from -- presumably -- most Danish banks.
    Does not work with CSV files from:
        Coop Bank
        Forbrugsforeningen
    '''
    account_data = pandas.read_csv(account, sep=';', usecols=['Dato', 'Tekst',
                                                              'Beløb'],
                                   parse_dates=[0], dayfirst=True,
                                   quotechar='"', encoding='cp1252', header=0)
    account_data.columns = ['Date', 'Payee', 'Amount']
    account_data['Amount'] = account_data['Amount'].str.replace('.', '')
    account_data['Amount'] = account_data['Amount'].str.replace(',', '.')
    account_data.to_csv(account, index=False, encoding='utf-8')


for filename in os.listdir('.'):
    if not filename.endswith('.csv'):
        continue  # skip non-csv files

    try:
        # See if we can read the file.
        pandas.read_csv(filename)
        # If pandas can read the file by default, it should be reformatted
        # already, so skip it.
        continue
    except:
        # Pandas has thrown some error, this probably means that the file
        # is a native bank csv, so reformat it.
        # It seems somewhat ugly to do it in this backwards way...
        print("Reformatting " + filename + "...")
        reformat(filename)

sleep(1)
