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
    accountData = pandas.read_csv(account, sep=';', usecols=['Dato', 'Tekst',
                                                             'Beløb'],
                                  parse_dates=[0], dayfirst=True,
                                  quotechar='"', encoding='cp1252', header=0,
                                  names=['Date', 'Payee', 'Amount'])
    accountData['Amount'] = accountData['Amount'].str.replace('.', '')
    accountData['Amount'] = accountData['Amount'].str.replace(',', '.')
    accountData.to_csv(account, index=False, encoding='utf-8')


for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue  # skip non-csv files

    column_check = pandas.read_csv(csvFilename)

    if len(column_check) == 3:
        # If the file has only  three columns, we have already reformatted it.
        print(csvFilename + " already reformatted, skipping.")
        continue

    print("Reformatting " + csvFilename + "...")
    reformat(csvFilename)
