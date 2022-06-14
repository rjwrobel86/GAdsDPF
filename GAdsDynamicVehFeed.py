import pysftp
import pandas as pd
import os

#Calls a shell script to download a csv via SFTP
os.system('zsh dominion.sh')

file1 = pd.read_csv('feed.csv')

frame1 = file1[['Final URL', 'Item title']]
frame1['Custom label'] = frame1['Item title']
frame1['Page URL'] = frame1['Final URL']
frame2 = frame1[['Page URL','Custom label']]

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

frame2.to_csv('googleurls.csv', index=0)

with pysftp.Connection('IPADDRESS', username='USERNAME', password='PASSWORD', private_key=".ppk", cnopts=cnopts) as sftp:
        sftp.put('googleurls.csv') #Uploads a file
        #sftp.get('feed.csv') #Downloads a file

