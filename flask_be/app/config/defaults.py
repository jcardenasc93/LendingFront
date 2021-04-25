""" Set default server configuration according to env values """

import os


class Config:
    """ Defines server configuration """

    def __init__(self):
        self._config = {
            "env": os.getenv("ENVIRONMENT", "production"),
            "port": os.getenv("GLOBAL_PORT", "5000")
        }

    @property
    def config(self):
        return self._config
