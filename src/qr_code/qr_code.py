from typing import Optional

import qrcode
import cv2
from pyzbar.pyzbar import decode


def generate_qr_code(request_url: str, filename: str) -> None:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(request_url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)


def scan_qr_code(filename: str) -> Optional[str]:
    image = cv2.imread(filename)
    decoded_objects = decode(image)

    if len(decoded_objects) > 0:
        decoded_url = decoded_objects[0].data.decode("utf-8")
        return decoded_url
    else:
        return None


if __name__ == "__main__":
    url_to_encode = "https://www.example.com"
    generate_qr_code(url_to_encode, "./src/qr_code/qr_code.png")
    print("QR Code generated successfully!")

    scanned_url = scan_qr_code("./src/qr_code/qr_code.png")

    if scanned_url is not None:
        print(f"URL is {scanned_url}")
    else:
        print("Unable to get the URL")
