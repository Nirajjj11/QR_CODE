import segno
qrcode = segno.make_qr(" \U0001f600  \U00002764 \U00002764  HAPPY NEW YEAR 2023  \U00002764 \U00002764  \U0001f600")
qrcode.save("hny2023.png",scale =100)