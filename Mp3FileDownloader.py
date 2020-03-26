from bs4 import BeautifulSoup
import requests
import os
import sys

artist_name = sys.argv[1]

url = 'https://www.sinhalasongs.lk/sinhala-songs-download/' + artist_name + '/'
ext = 'mp3'
filename = ''
if artist_name is not None:
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    dirname = artist_name
    for node in soup.find_all('a'):
        if node.get('href').find(artist_name) != -1:
            url2 = node.get('href') + '/'
            page2 = requests.get(url2).text
            soup2 = BeautifulSoup(page2, 'html.parser')
            for node2 in soup2.find_all('a'):
                if node2.get('href').endswith(ext):
                    try:
                        if not os.path.exists(dirname):
                            os.mkdir(dirname)
                        for txt in node2.get('href').split('/'):
                            if txt.endswith(ext):
                                filename = txt
                        r = requests.get(node2.get('href'), allow_redirects=True)
                        os.chdir('C:/Python/' + dirname)
                        open(filename, 'wb').write(r.content)
                        os.chdir('C:/Python/')
                    except IndexError:
                        continue
else:
    print('Artist name needs to provide.')
