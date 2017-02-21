from dstore import Model as M, var


class TagList( M ):
    _namespace = "chapter.taglist"
    _vars = [
        var.RowID,
        var.ForeignKey( "chapter.tag" ),
        var.ForeignKey( "chapter.chapter" )
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
