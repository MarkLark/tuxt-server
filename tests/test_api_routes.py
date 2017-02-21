from nose.tools import eq_
from . import BaseTest, defaults
from simplejson import loads


class TestAPIRoutes( BaseTest ):
    def test_app_category_defaults( self ):
        with self.app.app_context():
            rtn = self.client.get( "/api/app/category/" )
            data = loads(rtn.data)
            eq_( data, defaults['app']['category'], "Returned data does not match App.Category defaults" )
