import pyqrcode

url = input("QR oluşturmak istediğiniz url : ")

qr_code = pyqrcode.create(url)
qr_code.svg('qrcode.svg', scale = 5)