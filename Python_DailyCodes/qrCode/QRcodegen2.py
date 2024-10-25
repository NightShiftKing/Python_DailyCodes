import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('gus likes drippy cheese')
qr.make_image(fit=True)

img = qr.make_image(fill='black', back_color='white')

img.save('qr_code_output.jpg')