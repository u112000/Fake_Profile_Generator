#! python3
import requests
import json
import random
import os
from rich import print

api_url = 'https://randomuser.me/api/'

r = requests.get(api_url)
database = json.loads(r.text)
def solid():
    passwd = ['cb#c@', '9en$UW@2', '8HWN27£', 'O28$$$#82WN', 'W£927jsv', 'Niw92a$S']
    passwd_ = []
    for i in range(1, 3+1):
        random.shuffle(passwd)
        passwd_.append(random.choice(passwd))
    return ''.join(passwd_)

def downloaderm():
    r2 = requests.get(f'{database['results'][0]['picture']['medium']}', stream=True)
    f = open(f'medium_{database['results'][0]['name']['first']}_{database['results'][0]['name']['last']}.jpg', 'wb')
    for i in r2:
        f.write(i)
    f.close()
    if os.stat(f'medium_{database['results'][0]['name']['first']}_{database['results'][0]['name']['last']}.jpg').st_size > 0:
        return 'SUCCESSFULLY DOWNLOADED MEDIUM IMAGE'
    else:
        return 'DOWNLOAD FAILED!'

def downloaderl():
    r2 = requests.get(f'{database['results'][0]['picture']['large']}', stream=True)
    f = open(f'large_{database['results'][0]['name']['first']}_{database['results'][0]['name']['last']}.jpg', 'wb')
    for i in r2:
        f.write(i)
    f.close()
    if os.stat(f'large_{database['results'][0]['name']['first']}_{database['results'][0]['name']['last']}.jpg').st_size > 0:
        return 'SUCCESSFULLY DOWNLOADED LARGE IMAGE'
    else:
        return 'DOWNLOAD FAILED!'

print('*'*15 + '[reverse]Basic Details[/reverse]'+ '*'*15)
print(f'[+] [bold underline]Name[/bold underline]:______________________ {database['results'][0]['name']['title']}. {database['results'][0]['name']['first']} {database['results'][0]['name']['last']}')
print(f'[+] [bold underline]Gender[/bold underline]:____________________ {database['results'][0]['gender']}')
print(f'[+] [bold underline]Age[/bold underline]:_______________________ {database['results'][0]['dob']['age']}')
print(f'[+] [bold underline]DOB[/bold underline]:_______________________ {database['results'][0]['dob']['date'][:10]}')
print(f'[+] [bold underline]M. Face snapshot link[/bold underline]:_____ Downloading: [green]{downloaderm()}[/green].')
print(f'[+] [bold underline]L. Face snapshot link[/bold underline]:_____ Downloading: [green]{downloaderl()}[/green].')
print(f'[+] [bold underline]Nationality[/bold underline]:_______________ {database['results'][0]['nat']} ({database['results'][0]['location']['country']})')
print(r'[+]')
print(r'[+]')
print('*'*15 + '[reverse]Advanced Addtional Details[/reverse]'+ '*'*15)
print(f'[+] [bold underline]Street Address[/bold underline]:____________ {database['results'][0]['location']['street']['number']}')
print(f'[+] [bold underline]Street Name[/bold underline]:_______________ {database['results'][0]['location']['street']['name']}')
print(f'[+] [bold underline]City[/bold underline]:______________________ {database['results'][0]['location']['city']}')
print(f'[+] [bold underline]State[/bold underline]:_____________________ {database['results'][0]['location']['state']}')
print(f'[+] [bold underline]Country[/bold underline]:___________________ {database['results'][0]['location']['country']}')
print(f'[+] [bold underline]Post-Code[/bold underline]:_________________ {database['results'][0]['location']['postcode']}')
print()
print(f'[+] [bold underline]Email[/bold underline]:_____________________ {database['results'][0]['email']}')
print(f'[+] [bold underline]Current Location[/bold underline]:__________ {database['results'][0]['location']['timezone']['description']}')
print(f'[+] [bold underline]Longitude & Latitude[/bold underline]:______ {database['results'][0]['location']['coordinates']['longitude']} {database['results'][0]['location']['coordinates']['latitude']}')
print(f'[+] [bold underline]UUID[/bold underline]:______________________ {database['results'][0]['login']['uuid']}')
print(f'[+] [bold underline]Username[/bold underline]:__________________ {database['results'][0]['login']['username']}')
print(f'[+] [bold underline]Password[/bold underline]:__________________ {solid()}{database['results'][0]['login']['password']}{solid()}')
print()
