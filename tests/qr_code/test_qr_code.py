import unittest
import os
from src.qr_code.qr_code import generate_qr_code, scan_qr_code


class TestQRCode(unittest.TestCase):
    def test_qr_code_generation_and_scanning(self):
        qr_code_file = "./tests/qr_code/test.jpg"
        data = "https://www.kognitos.com"

        generate_qr_code(data, qr_code_file)
        self.assertTrue(os.path.exists(qr_code_file))

        scanned_url = scan_qr_code(qr_code_file)
        self.assertTrue(scanned_url, data)

        os.remove(qr_code_file)


if __name__ == "__main__":
    unittest.main()
