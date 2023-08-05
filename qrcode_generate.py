# 1. pip install pyqrcode
# 2. Prepare a script for QR code
# 3. Run this script

import pyqrcode
from pyqrcode import QRCode

s = "https://www.youtube.com/@CodeWithHarry"
url = pyqrcode.create(s)
url.svg("myFirstQRCode.svg", scale=10)