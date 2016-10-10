'''
Created on 21 Jul 2016

@author: Tim Rørstrøm
'''
import os
import pandas

work_dir = os.path.expanduser('~\\Downloads')
os.chdir(work_dir)

def reformat(account):
    accountData = pandas.read_csv(account, sep=';', usecols=[0, 2, 4], parse_dates=[0], dayfirst=True, quotechar='"', encoding='cp1252', header=0, names=['Date', 'Payee', 'Amount'])
    accountData['Amount'] = accountData['Amount'].str.replace('.', '').str.replace(',', '.')
    accountData.to_csv(account, index=False)
    
for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip non-csv files
    reformat(csvFilename)
