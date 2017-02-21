from dstore import Model as M, var, mod


class Tag( M ):
    _namespace = "chapter.tag"
    _vars = [
        var.RowID,
        var.String( "name", 32, mods = [ mod.NotNull() ] )
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
