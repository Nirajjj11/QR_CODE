import segno
qrcode = segno.make_qr('This is niraj ')
qrcode.save('welcome.png', scale=1000)