""" App entry point. """
import os
from quart import Quart


def create_app():
    """ Function for bootstrapping sanic app. """

    app = Quart(__name__)

    # Register Blueprints/Views.


    app.run()

