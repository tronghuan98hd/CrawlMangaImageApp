import urllib.request
import json
from urllib.request import urlretrieve
from image_slicer import join
import image_slicer
import os

from bs4 import BeautifulSoup
import urllib

# example https://pocket.shonenmagazine.com/episode/13933686331699204472
# def find_image(url, dirName):
#     try:
#         fp = urllib.request.urlopen(url)
#     except:
#         return False
#     soup = BeautifulSoup(fp, 'html.parser')
#     tag_soup = soup.find_all('section', attrs={"data-json-url": True})[0]
#     with urllib.request.urlopen(tag_soup['data-json-url']) as url:
#         data = json.loads(url.read().decode())
#         try:
#             for values in data['readableProduct']['pageStructure'].items():
#                 if type(values) is not str:
#                     for value in values:
#                         if type(value) is not str:
#                             count = 1
#                             for obj in value:
#                                 if obj['type'] == 'main':
#                                     name = '{}.png'.format(count)
#                                     fullfilename = os.path.join(dirName, name)
#                                     urlretrieve(obj['src'], fullfilename)
#                                     count = count + 1
#         except:
#             return False
#     for i in range(1, count):
#         name = '{}.png'.format(i)
#         fullfilename = os.path.join(dirName, name)
#         tiles = image_slicer.slice(fullfilename, 16, save=False)
#         tiles[1].image, tiles[4].image = tiles[4].image, tiles[1].image
#         tiles[2].image, tiles[8].image = tiles[8].image, tiles[2].image
#         tiles[3].image, tiles[12].image = tiles[12].image, tiles[3].image
#         tiles[7].image, tiles[13].image = tiles[13].image, tiles[7].image
#         tiles[11].image, tiles[14].image = tiles[14].image, tiles[11].image
#         tiles[6].image, tiles[9].image = tiles[9].image, tiles[6].image
#         image = join(tiles)
#         newname = '{}.png'.format(i)
#         fullnewfilename = os.path.join(dirName, name)
#         image.save(fullnewfilename)
#     return True

def find_image_pocket(url, dirName):
    try:
        try:
            with open('cookie.txt') as f:
                lines = f.readlines()
                print(type("".join(lines)))
        except:
            return False
        request = urllib.request.Request(url + ".json")
        request.add_header("Cookie", "".join(lines))
        with urllib.request.urlopen(request) as url:
            data = json.loads(url.read().decode())
            try:
                for values in data['readableProduct']['pageStructure'].items():
                    if type(values) is not str:
                        for value in values:
                            if type(value) is not str:
                                count = 1
                                for obj in value:
                                    if obj['type'] == 'main':
                                        name = '{}.png'.format(count)
                                        fullfilename = os.path.join(dirName, name)
                                        urlretrieve(obj['src'], fullfilename)
                                        count = count + 1
            except:
                return False
        for i in range(1, count):
            name = '{}.png'.format(i)
            fullfilename = os.path.join(dirName, name)
            tiles = image_slicer.slice(fullfilename, 16, save=False)
            tiles[1].image, tiles[4].image = tiles[4].image, tiles[1].image
            tiles[2].image, tiles[8].image = tiles[8].image, tiles[2].image
            tiles[3].image, tiles[12].image = tiles[12].image, tiles[3].image
            tiles[7].image, tiles[13].image = tiles[13].image, tiles[7].image
            tiles[11].image, tiles[14].image = tiles[14].image, tiles[11].image
            tiles[6].image, tiles[9].image = tiles[9].image, tiles[6].image
            image = join(tiles)
            newname = '{}.png'.format(i)
            fullnewfilename = os.path.join(dirName, name)
            image.save(fullnewfilename)
        return True

    except:
        return False