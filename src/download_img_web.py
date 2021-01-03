import webbrowser
from urllib.request import urlretrieve, urlopen, FancyURLopener


def download_image_web(url, output_file):
    # url = "https://en.wikipedia.org/wiki/Penguin#/media/File:South_Shetland-2016-Deception_Island%E2%80%93Chinstrap_penguin_(Pygoscelis_antarctica)_04.jpg"
    # webbrowser.open(url)

    # png_file = "{}.png".format(self.fname)
    urlretrieve(url, output_file)

    # with urlopen(url) as response, open("test.png", 'wb') as out_file:
    #     data = response.read()  # a `bytes` object
    #     out_file.write(data)

    # with urlopen(url) as response, open(png_file, 'wb') as out_file:
    #     shutil.copyfileobj(response, out_file)

    # credit: http://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3
    # credit: http://stackoverflow.com/questions/31893207/python-3-4-http-error-505-retrieving-json-from-url
    # url_request = FancyURLopener({})
    # with url_request.open(url) as response, open(png_file, 'wb') as out_file:
    #     shutil.copyfileobj(response, out_file)

        # url_request = FancyURLopener({})
        # with url_request.open(url) as response, open(png_file, 'wb') as out_file:
        #     data = response.read()  # a `bytes` object
        #     out_file.write(data)

if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/Penguin#/media/File:South_Shetland-2016-Deception_Island%E2%80%93Chinstrap_penguin_(Pygoscelis_antarctica)_04.jpg"
    download_image_web(url, "out.jpg")