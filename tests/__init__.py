from unittest import TestCase
from app import create_app, models

__all__ = [ "BaseTest", "defaults" ]


class BaseTest( TestCase ):
    auto_create = True

    def setUp( self ):
        self.app, self.api = create_app( config = "configs.travis", models = models.models )
        self.client = self.app.test_client()

        if self.auto_create:
            with self.app.app_context():
                self.api.store.create_all()
                models.os.add_defaults( self.api.store )
                models.app.add_defaults( self.api.store )

    def tearDown( self ):
        if self.auto_create:
            with self.app.app_context():
                self.api.store.destroy_all()


defaults = {
    "app": {
        "category": [
            {
                "description": "Operating System",
                "id": 0,
                "name": "OS",
                "tag": "os"
            },
            {
                "description": "Hypertext Transfer Protocol - Internet",
                "id": 1,
                "name": "HTTP",
                "tag": "http"
            },
            {
                "description": "Network firewall",
                "id": 2,
                "name": "Firewall",
                "tag": "firewall"
            }
        ]
    }
}