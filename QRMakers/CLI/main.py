import qrcode
from PIL import Image

class QRCodeGenerator:
    def __init__(self):
        self.version = 1.0
        self.format = 'CLI'
        self.QR = qrcode
        self.qr = None
    def generateQR(self,data):
        self.qr = self.QR.QRCode(version=1, box_size=10, border=5)
        self.qr.add_data(data)
        self.qr.make(fit=True)
    def saveQR(self,filename="qrcode.png"):
        if self.qr is None:
            raise ValueError('Generate A QR code First  ')
        self.qr.make_image(fill='black', back_color='white').save(filename)


