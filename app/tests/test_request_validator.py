""" Unit testing for request validator """

from app.services.request_validator import RequestValidator
import unittest

class RequestValidatorTest(unittest.TestCase):
    """ Tests definition for request validator """

    def setUp(self):
        self._valid_number = "123"
        self._invalid_number = "abc"

    def test_number_validation_cases(self):
        """ Test cases for number validatiion type """
        # Correct case
        validation, number = RequestValidator.validate_number_type(self._valid_number)
        self.assertEqual(True, validation["status"])
        # Bad case
        validation, number = RequestValidator.validate_number_type(self._invalid_number)
        self.assertEqual(False, validation["status"])

