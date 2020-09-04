import urllib.request
import json
from urllib.request import urlretrieve
from image_slicer import join
import image_slicer

from bs4 import BeautifulSoup
import urllib
from PIL import Image
from image_slicer import join
import image_slicer

fp = urllib.request.urlopen(
    'https://comic-days.com/episode/10834108156751247927')
soup = BeautifulSoup(fp, 'html.parser')
tag_soup = soup.find_all('section', attrs={"data-json-url": True})[0]
# print(tag_soup['data-json-url'])

with urllib.request.urlopen(tag_soup['data-json-url']) as url:
    data = json.loads(url.read().decode())
    # print(data['readableProduct']['pageStructure']['spread'])
    for values in data['readableProduct']['pageStructure'].items():
        if type(values) is not str:
            for value in values:
                # print(value)
                if type(value) is not str:
                    count = 1
                    for obj in value:
                        if obj['type'] == 'main':
                            name = '{}.png'.format(count)
                            urlretrieve(obj['src'], name)
                            count = count + 1

for i in range(1, count):
    name = '{}.png'.format(i)
    im = Image.open(name)

    width, height = im.size

    left = width - width
    top = height - height
    right = width - 5
    bottom = height

    im1 = im.crop((left, top, right, bottom))
    im1.save(name)

    tiles = image_slicer.slice(name, 16, save=False)
    tiles[1].image, tiles[4].image = tiles[4].image, tiles[1].image
    tiles[2].image, tiles[8].image = tiles[8].image, tiles[2].image
    tiles[3].image, tiles[12].image = tiles[12].image, tiles[3].image
    tiles[7].image, tiles[13].image = tiles[13].image, tiles[7].image
    tiles[11].image, tiles[14].image = tiles[14].image, tiles[11].image
    tiles[6].image, tiles[9].image = tiles[9].image, tiles[6].image
    image = join(tiles)
    newname = '{}.png'.format(i)
    image.save(newname)
