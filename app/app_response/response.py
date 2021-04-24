""" Defines Response class used in the application """

from flask import jsonify


class Response:
    """ Default response structure """

    def __init__(self, data: dict, message: str, server_info: str):
        self.data = data
        self.message = message
        self.server_info = server_info

    def create_response(self):
        app_response = {
            "message": self.message,
            "serverInfo": self.server_info,
            "data": self.data
        }
        return jsonify(app_response)
