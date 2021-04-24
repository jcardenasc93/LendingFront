""" Defines the views for the flask app """

from app import app
from app.app_response.response import Response


@app.route("/", methods=["GET"])
def health_check():
    """ Endpoint to check server status """
    response = Response(data={}, message="I'm alive", server_info="Ok")
    return response.create_response()
