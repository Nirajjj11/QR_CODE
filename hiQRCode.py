# IF SEGNO IS NOT INSTALL THE TO INSTALL RUN THE CODE:
# >>>  pip install segno
import segno
qrcode=segno.make_qr("Hi how are you !")
qrcode.save("HiQRCode.png", scale = 100)