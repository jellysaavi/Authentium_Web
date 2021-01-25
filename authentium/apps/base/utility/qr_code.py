
import qrcode

#  ---------------------------------------------------------------
# qr_code_generator
#  ---------------------------------------------------------------
def qr_code_generator(qr_code_info):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_code_info)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    return img