""" Defines the views for the flask app """

import json
from flask import request

from app import app
from app.app_response.response import Response
from app.services.loan_evaluation import LoanEvaluator


@app.route("/", methods=["GET"])
def health_check():
    """ Endpoint to check server status """
    response = Response(data={}, message="I'm alive", server_info="Ok")
    return response.create_response()


@app.route("/evaluate-loan", methods=["POST"])
def evaluate_loan():
    """ Controls the logic to process the loan evaluation request """
    body = None
    try:
        body = json.loads(request.data)
    except json.JSONDecodeError as e:
        response = Response(data={},
                            message="Invalid request",
                            server_info=e.__str__())

    if body:
        requested_amount = float(body["amount"])
        decision = LoanEvaluator.loan_decision(requested_amount)
        response = Response(data={},
                            message=decision,
                            server_info="Loan evaluated")

    return response.create_response()
