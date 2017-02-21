from dstore import Model as M, var, mod


class ContentMap( M ):
    _namespace = "chapter.contentmap"
    _vars = [
        var.RowID,
        var.ForeignKey( "chapter.content" ),
        var.ForeignKey( "chapter.map" )
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
