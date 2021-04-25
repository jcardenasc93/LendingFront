""" Unit testing for loan evaluation logic """

from app.services.loan_evaluation import LoanEvaluator
import unittest


class LoanEvaluatorTest(unittest.TestCase):
    """ Tests definiton for loan evaluation process """

    def setUp(self):
        self.declined = LoanEvaluator.DECLINED
        self.undecided = LoanEvaluator.UNDECIDED
        self.approved = LoanEvaluator.APPROVED

    def test_declined_case(self):
        """ Test expecting declined resopnse """
        amount = 50000.001
        request_response = LoanEvaluator.loan_decision(amount)
        self.assertEqual(self.declined, request_response)

    def test_undecided_case(self):
        """ Test expecting undecided resopnse """
        amount = 50000
        request_response = LoanEvaluator.loan_decision(amount)
        self.assertEqual(self.undecided, request_response)

    def test_acepted_case(self):
        """ Test expecting undecided resopnse """
        amount = 49999.9999
        request_response = LoanEvaluator.loan_decision(amount)
        self.assertEqual(self.approved, request_response)
