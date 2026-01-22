#! python3

###########################################################################
# Name:         Profile_generator
# Purpose:     Generation of bio-data, credentials, social details and geo-location status with ease.

# Author:       U_x112000

# Created:    ...
# Encoding:  utf-8
###########################################################################

import os
import json
import secrets
import requests
from rich import print
from rich.table import Table

class ProfileGen:
    def __init__(self):
        self.api_url: dict = self.connections('https://randomuser.me/api/')
        self.data: dict = {
            'Name': f"{self.api_url['results'][0]['name']['title']}. {self.api_url['results'][0]['name']['first']} {self.api_url['results'][0]['name']['last']}",
            'Gender': f"{self.api_url['results'][0]['gender']}",
            'Age': f"{self.api_url['results'][0]['dob']['age']}",
            'Date Of Birth': f"{self.api_url['results'][0]['dob']['date']}",
            'Medium Face snapshot': f"{self.download_image(mfile=True)}",
            'Large Face snapshot': f"{self.download_image(lfile=True)}",
            'Nationality': f"{self.api_url['results'][0]['nat']} {self.api_url['results'][0]['location']['country']}",
            'Street Address': f"{self.api_url['results'][0]['location']['street']['number']}",
            'Street Name': f"{self.api_url['results'][0]['location']['street']['name']}",
            'City': f"{self.api_url['results'][0]['location']['city']}",
            'State': f"{self.api_url['results'][0]['location']['state']}",
            'Country': f"{self.api_url['results'][0]['location']['country']}",
            'Post-Code': f"{self.api_url['results'][0]['location']['postcode']}",
            'Email': f"{self.api_url['results'][0]['email']}",
            'Current Location': f"{self.api_url['results'][0]['location']['timezone']['description']}",
            'Longitude & Latitude': f"{self.api_url['results'][0]['location']['coordinates']['longitude']} {self.api_url['results'][0]['location']['coordinates']['latitude']}",
            'UUID': f"{self.api_url['results'][0]['login']['uuid']}",
            'Username': f"{self.api_url['results'][0]['login']['username']}",
            'Password': f"{self.generate_password()}"}
        
    def __str__(self):
        return f'Fake profile generator object using {self.api_url}'

    def connections(self, url):
        try:
            r = requests.get(url, timeout=10)
        except:
            raise Exception(f'Unable to connect with website api\n{self.api_url} offline')
        else:
            if r.status_code == 200:
                return r.json()
            else:
                raise Exception('Website not responding')
            
    def generate_password(self, length=12):
        passwd = secrets.token_urlsafe(length)
        return passwd

    def download_image(self, lfile=False, mfile=False):
        M_image_url = f"{self.api_url['results'][0]['picture']['medium']}"
        M_imagefile_name = f"MEDIUM_IMAGE-{self.api_url['results'][0]['name']['first']}_{self.api_url['results'][0]['name']['last']}.jpg"
        L_image_url = f"{self.api_url['results'][0]['picture']['large']}"
        L_imagefile_name = f"LARGE_IMAGE-_{self.api_url['results'][0]['name']['first']}_{self.api_url['results'][0]['name']['last']}.jpg"

        if mfile:
            with requests.get(M_image_url, stream=True, timeout=10) as mfr, open(M_imagefile_name, 'wb') as mf:
                for chunk in mfr:
                    mf.write(chunk)
            m_image_download_stat = f"{'SUCCESSFULLY DOWNLOADED MEDIUM IMAGE'.title() if os.stat(M_imagefile_name).st_size > 0 else 'DOWNLOAD FAILED!'.title()}"
            return m_image_download_stat

        elif lfile:
            with requests.get(L_image_url, stream=True, timeout=10) as lfr, open(L_imagefile_name, 'wb') as lf:
                for chunk in lfr:
                    lf.write(chunk)
            l_image_download_stat = f"{'SUCCESSFULLY DOWNLOADED Large IMAGE'.title() if os.stat(L_imagefile_name).st_size > 0 else 'DOWNLOAD FAILED!'.title()}"
            return l_image_download_stat

    def generate_gui(self):
        t = Table()
        t.add_column('Bio Fields', style='bold green')
        t.add_column('Generated Bio-data', style='bold white')
        for key, value in self.data.items():
            t.add_row(key, value)
        return t

if __name__ == '__main__':
    app = ProfileGen()
    print(app.generate_gui())
