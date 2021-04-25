""" Module to define a request validator for the app """
import json


class RequestValidator:
    """ Request validator needed for the incomming requests """
    request_definitions = {"loan_eval": {"params": ["amount"]}}

    @classmethod
    def validate_required_params(cls, request, key: str):
        """ Checks that the incomming request is valid """
        validation = {"status": True, "error": None}
        validated_request = {}
        body = None
        try:
            body = json.loads(request.data)
        except json.JSONDecodeError as e:
            validation["status"] = False
            validation["error"] = e.__str__()
            return validation, validated_request

        required_params = cls.request_definitions[key]["params"]

        # Checks that the request has the required params
        for param in required_params:
            if body.get(param):
                validated_request[param] = body.get(param)
            else:
                validation["status"] = False
                validation["error"] = "Missing {} param".format(param)

        return validation, validated_request

    @staticmethod
    def validate_number_type(data):
        """ Validates that the data is of number type """
        validation = {"status": True, "error": None}
        try:
            data = float(data)
        except ValueError as e:
            validation["status"] = False
            validation["error"] = e.__str__()
        return validation, data
