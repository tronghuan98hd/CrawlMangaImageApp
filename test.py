import os
import urllib.request
import json
from urllib.request import urlretrieve

import urllib
from PIL import Image
from image_slicer import join
import image_slicer
#
#
# # example https://comic-days.com/episode/10834108156751247927
#
def find_image(url, dirName):
    try:
        request = urllib.request.Request(url + ".json")
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
            fullNewFileName = os.path.join(dirName, name)
            im = Image.open(fullNewFileName)
            width, height = im.size
            left = width - width
            top = height - height
            right = width - 5
            bottom = height
            im1 = im.crop((left, top, right, bottom))
            im1.save(fullNewFileName)
            tiles = image_slicer.slice(fullNewFileName, 16, save=False)
            tiles[1].image, tiles[4].image = tiles[4].image, tiles[1].image
            tiles[2].image, tiles[8].image = tiles[8].image, tiles[2].image
            tiles[3].image, tiles[12].image = tiles[12].image, tiles[3].image
            tiles[7].image, tiles[13].image = tiles[13].image, tiles[7].image
            tiles[11].image, tiles[14].image = tiles[14].image, tiles[11].image
            tiles[6].image, tiles[9].image = tiles[9].image, tiles[6].image

            image = join(tiles)
            name = '{}.png'.format(i)
            fullNewFileName = os.path.join(dirName, name)
            image.save(fullNewFileName)
        return True

    except:
        return False


url = "https://comic-days.com/episode/3269632237246196279"
dirName = "E:/Tools/manga_tool/test"
find_image(url, dirName)

# name = '{}.png'.format("imageTest")
# im = Image.open(name)
# width, height = im.size
# left = width - width
# top = height - height
# right = width - 5
# bottom = height
# im1 = im.crop((left, top, right, bottom))
# fullNewFileName = os.path.join(dirName, name)
# im1.save(fullNewFileName)
# tiles = image_slicer.slice(fullNewFileName, 16, save=False)
# tiles[1].image, tiles[4].image = tiles[4].image, tiles[1].image
# tiles[2].image, tiles[8].image = tiles[8].image, tiles[2].image
# tiles[3].image, tiles[12].image = tiles[12].image, tiles[3].image
# tiles[7].image, tiles[13].image = tiles[13].image, tiles[7].image
# tiles[11].image, tiles[14].image = tiles[14].image, tiles[11].image
# tiles[6].image, tiles[9].image = tiles[9].image, tiles[6].image
#
# image = join(tiles)
# name = '{}.png'.format("result")
# fullNewFileName = os.path.join(dirName, name)
# image.save(fullNewFileName)