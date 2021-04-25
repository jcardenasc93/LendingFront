""" Defines the views for the flask app """

import json
from flask import request

from app import app
from app.app_response.response import Response
from app.services.loan_evaluation import LoanEvaluator
from app.services.request_validator import RequestValidator


@app.route("/", methods=["GET"])
def health_check():
    """ Endpoint to check server status """
    response = Response(data={}, message="I'm alive", server_info="Ok")
    return response.create_response()


@app.route("/evaluate-loan", methods=["POST"])
def evaluate_loan():
    """ Controls the logic to process the loan evaluation request """
    check_request, validated_data = RequestValidator.validate_required_params(
        request, "loan_eval")
    if check_request["status"]:
        number_validation, requested_amount = RequestValidator.validate_number_type(
            validated_data["amount"])
        if not number_validation["status"]:
            response = Response(data={},
                                message="Invalid request",
                                server_info=number_validation["error"])
            return response.create_response(), 400
    else:
        response = Response(data={},
                            message="Invalid request",
                            server_info=check_request["error"])
        return response.create_response(), 400

    decision = LoanEvaluator.loan_decision(requested_amount)
    response = Response(data={}, message=decision, server_info="Loan evaluated")

    return response.create_response(), 200
