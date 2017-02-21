from dstore import Model as M, var, mod


class Distro( M ):
    _namespace = "os.distro"
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
        dists = {}
        for d in Distro.all(): dists[ d.tag ] = d

        if len( dists ) == 0:
            dists = {
                "rhel": Distro(
                    tag         = "rhel",
                    name        = "RHEL",
                    description = "RedHat Enterprise Linux"
                ).add(),
                "debian": Distro(
                    tag         = "debian",
                    name        = "Debian",
                    description = "Debian Linux"
                ).add()
            }

        return dists
