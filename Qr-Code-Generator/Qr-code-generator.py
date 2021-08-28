#import libary for qr-code generator
import pyqrcode

site = "https://medium.com/@arghasarkar5373"
url = pyqrcode.create(site)

url.png('argha.png',scale= 8)