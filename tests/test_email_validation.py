import unittest
from src.email_validation import validator


class TestEmailValidation(unittest.TestCase):
    def test_email_length(self):
        assert validator("ranjith@gmail.com") == True
