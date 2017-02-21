from dstore import Model as M, var


class TagList( M ):
    _namespace = "article.taglist"
    _vars = [
        var.RowID,
        var.ForeignKey( "article.article" ),
        var.ForeignKey( "article.tag" )
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
