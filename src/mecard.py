# https://zxing.appspot.com/generator/

# MECARD:N:Peter Parker;ORG:แผ่นดิน;TEL:092123456;EMAIL:abc@cbs.com;;
# https://zxing.org/w/chart?cht=qr&chs=350x350&chld=L&choe=UTF-8&chl=MECARD:N:Peter Parker;ORG:แผ่นดิน;TEL:092123456;EMAIL:abc@cbs.com;
import webbrowser
from urllib.request import urlretrieve, urlopen, FancyURLopener

import shutil


class Contact:
    def __init__(self, fname, lname, phone, email):
        self.fname = fname
        self.lname = lname
        self.phone = phone
        self.email = email

    @property
    def name(self):
        return "{} {}".format(self.fname, self.lname).strip()

    def mecard(self):
        return "MECARD:N:{};TEL:{};EMAIL:{}".format(self.name, self.phone, self.email)

    def gen_qrcode(self):
        url = "https://zxing.org/w/chart?cht=qr&chs=350x350&chld=L&choe=UTF-8&chl=" + self.mecard()
        webbrowser.open(url)

        png_file = "{}.png".format(self.fname)
        # urlretrieve(url, png_file)

        # with urlopen(url) as response, open("test.png", 'wb') as out_file:
        #     data = response.read()  # a `bytes` object
        #     out_file.write(data)

        # with urlopen(url) as response, open(png_file, 'wb') as out_file:
        #     shutil.copyfileobj(response, out_file)

        # credit: http://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3
        # credit: http://stackoverflow.com/questions/31893207/python-3-4-http-error-505-retrieving-json-from-url
        url_request = FancyURLopener({})
        with url_request.open(url) as response, open(png_file, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

            # url_request = FancyURLopener({})
            # with url_request.open(url) as response, open(png_file, 'wb') as out_file:
            #     data = response.read()  # a `bytes` object
            #     out_file.write(data)


if __name__ == '__main__':
    p = Contact("Clark", "Kent", "0871234567", "clark@email.com")
    print(p.mecard())
    p.gen_qrcode()

    # contacts = [
    #     Contact("Clark", "Kent", "0871234567", "clark@email.com"),
    #     Contact("Mike", "Swift", "0889993344", "mike@email.com"),
    #     Contact("John", "Smith", "0813334455", "john@email.com")
    # ]
    # for e in contacts:
    #     e.gen_qrcode()
