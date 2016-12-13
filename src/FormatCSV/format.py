'''
Created on 21 Jul 2016

@author: Tim Rørstrøm
'''
import os
import pandas

work_dir = os.path.expanduser('~/Downloads')
os.chdir(work_dir)


def reformat(account):
    '''This function uses the pandas library to extract the required
    information from a CSV file from presumably most Danish banks.
    '''
    account_data = pandas.read_csv(account, sep=';', usecols=['Dato', 'Tekst',
                                                              'Beløb'],
                                   parse_dates=[0], dayfirst=True,
                                   quotechar='"', encoding='cp1252', header=0,
                                   names=['Date', 'Payee', 'Amount'])
    account_data['Amount'] = account_data['Amount'].str.replace('.', '')
    account_data['Amount'] = account_data['Amount'].str.replace(',', '.')
    account_data.to_csv(account, index=False, encoding='utf-8')


for csv_filename in os.listdir('.'):
    if not csv_filename.endswith('.csv'):
        continue  # skip non-csv files

    column_check = pandas.read_csv(csv_filename)

    if len(column_check) == 3:
        # If the file has only  three columns, we have already reformatted it.
        print(csv_filename + " already reformatted, skipping.")
        continue

    print("Reformatting " + csv_filename + "...")
    reformat(csv_filename)
