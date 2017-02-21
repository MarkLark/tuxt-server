from flask import Flask
from flask_dstore import API
from dstore import MemoryStore
from flask_cors import CORS


def create_app( config, models, name = __name__, store = MemoryStore ):
    app = Flask( name )
    CORS(app)
    app.config.from_object( config )
    api = API( store( models ), app )

    return app, api
