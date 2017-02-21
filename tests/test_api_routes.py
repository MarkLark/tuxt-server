from nose.tools import eq_
from . import BaseTest
from simplejson import loads

app_cat_defaults = [
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


class TestAPIRoutes( BaseTest ):
    def test_model_url( self ):
        with self.app.app_context():
            rtn = self.client.get( "/api/app/category/" )
            data = loads(rtn.data)
            eq_( data, app_cat_defaults, "Returned data does not match App.Category defaults" )
