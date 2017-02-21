from dstore import Model as M, var, mod


class Category( M ):
    _namespace = "app.category"
    _vars = [
        var.RowID,
        var.String( "tag", 32, mods = [ mod.NotNull(), mod.Unique() ] ),
        var.String( "name", 32, mods = [ mod.NotNull() ]),
        var.Text( "description" )

    ]
    _acl_rules = dict(
        add    = dict( allow = [ "admin", "member" ]),
        read   = dict( default = True ),
        update = dict( allow = [ "admin" ]),
        delete = dict( allow = [ "admin" ]),
        empty  = dict( allow = [ "admin" ])
    )

    @staticmethod
    def defaults():
        cats = {}
        for c in Category.all(): cats[ c.tag ] = c

        if len( cats ) == 0:
            cats = {
                "os": Category(
                    tag         = "os",
                    name        = "OS",
                    description = "Operating System"
                ).add(),
                "http": Category(
                    tag         = "http",
                    name        = "HTTP",
                    description = "Hypertext Transfer Protocol - Internet"
                ).add(),

                "firewall": Category(
                    tag         = "firewall",
                    name        = "Firewall",
                    description = "Network firewall"
                ).add()
            }

        return cats
