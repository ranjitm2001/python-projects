import unittest
from src.email_validation.email_validation import validator


class TestEmailValidation(unittest.TestCase):
    def test_email_validations(self):
        assert validator("r@.in") is False
        assert validator("1anjith@gmail.com") is False
        assert validator("ran@jith@gmail.com") is False
        assert validator("ranjith@gmai.lcom") is False
        assert validator("ran_jith_@gmail.in") is True
        assert validator("ran.jith@gmail.in") is True
        assert validator("ran_jith_123@gmail.in") is True
        assert validator("ranjith 123@gmail.in") is False
        assert validator("ranJith@gmail.com") is False
