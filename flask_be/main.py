""" Flask application entrypoint """

from app import app
from app.config.defaults import Config

if __name__ == '__main__':
    server_config = Config().config
    debug = True if server_config["env"] == "development" else False
    app.run(host="0.0.0.0", port=server_config["port"], debug=debug)
