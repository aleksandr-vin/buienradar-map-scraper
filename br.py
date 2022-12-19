# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import logging
import sys
root = logging.getLogger()
root.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stderr)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

def loadProps(url):
  response = requests.get(url)
  logging.info(f"Page fetched {len(response.content)} bytes in {response.elapsed.total_seconds()} seconds")
  soup = BeautifulSoup(response.text, "html.parser")
  for l in soup.find_all('div'):
    if 'data-control' in l.attrs.keys() and l['data-control'] == "Map" and 'data-properties' in l.attrs.keys():
      props = json.loads(l['data-properties'])
      ####print(json.dumps(props))
      if 'preloadedJson' in props.keys():
        preloadedJson = props['preloadedJson']
        if 'times' in preloadedJson.keys():
          for t in preloadedJson['times']:
            if 'timestamp' in t.keys():
              print(json.dumps(t['timestamp']))
            if 'url' in t.keys():
              print(json.dumps(t['url']))


# set A:
rainUrl = u'https://www.buienradar.nl/home/RadarMapRainNL'
snowUrl = u'https://www.buienradar.nl/home/sneeuw'
satUrl = u'https://www.buienradar.nl/home/satelliet'
tempUrl = u'https://www.buienradar.nl/home/temperatuur'

# set B:
neerslag8uursUrl = u'https://www.buienradar.nl/nederland/neerslag/buienradar/8uurs'

loadProps(neerslag8uursUrl)


#  For urls of set A, some samples for result url based on 'preload' field:
#  https://image.buienradar.nl/2.0/image/single/RadarMapRainWebmercatorNL?extension=png&width=550&height=475&renderText=False&renderBranding=False&renderBackground=True&runTimestamp=202212180010&timestamp=202212180020
#  https://image.buienradar.nl/2.0/image/single/RadarMapSnowNL?height=512&width=550&extension=png&renderBackground=True&renderBranding=False&renderText=False&history=0&forecast=12&skip=0
# (?) https://image.buienradar.nl/2.0/image/single/SatVisual?height=512&width=550&extension=png,jpg&renderBackground=True&renderBranding=False&renderText=False&history=8&forecast=0&skip=0&subType=nl
#  https://image.buienradar.nl/2.0/image/single/SatVisual?extension=png&width=550&height=512&renderText=False&renderBranding=False&renderBackground=False&subType=nl&timestamp=202212171745
#  https://image.buienradar.nl/2.0/image/single/WeatherMapTemperatureActualNL?height=988&width=820&extension=png&renderBackground=False&renderBranding=False&renderText=False&history=12&forecast=0&skip=0