""" Module to define the loan evaluation process """


class LoanEvaluator:
    """ This class defines the loan evaluation """
    THRESHOLD = float(50000)
    DECLINED = "Declined"
    UNDECIDED = "Undecided"
    APPROVED = "Approved"

    @classmethod
    def loan_decision(cls, requested_amount):
        """ Method to define the logic for loan approval """
        if requested_amount == cls.THRESHOLD:
            return cls.UNDECIDED
        elif requested_amount > cls.THRESHOLD:
            return cls.DECLINED
        else:
            return cls.APPROVED
