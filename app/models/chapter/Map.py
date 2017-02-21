from dstore import Model as M, var, mod


class Map( M ):
    _namespace = "chapter.map"
    _vars = [
        var.RowID,
        var.ForeignKey( "chapter.chapter" ),
        var.ForeignKey( "apps.app" ),
        var.ForeignKey( "os.osversion" )
    ]
    _acl_rules = dict(
        add    = dict( allow = [ "admin", "member" ]),
        read   = dict( default = True ),
        update = dict( allow = [ "admin" ]),
        delete = dict( allow = [ "admin" ]),
        empty  = dict( allow = [ "admin" ])
    )

    @staticmethod
    def add_defaults():
        pass
