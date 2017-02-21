from dstore import Model as M, var, mod
from .Distro import Distro


class OS( M ):
    _namespace = "os.os"
    _vars = [
        var.RowID,
        var.String( "tag", 32, mods = [ mod.NotNull() ] ),
        var.String( "name", 32, mods = [ mod.NotNull() ] ),
        var.Text( "description" ),
        var.ForeignKey( "os.distro" )
    ]
    _acl_rules = dict(
        add    = dict( allow = [ "admin", "member" ]),
        read   = dict( default = True ),
        update = dict( allow = [ "admin" ]),
        delete = dict( allow = [ "admin" ]),
        empty  = dict( allow = [ "admin" ])
    )

    def add_version( self, **kwargs ):
        from .Version import Version
        kwargs["os_os_id"] = self.id
        return Version( **kwargs ).add()

    @staticmethod
    def defaults():
        dists = Distro.defaults()

        apps = {}
        for a in OS.all(): apps[ a.tag ] = a

        if len( apps ) == 0:
            apps = {
                "centos": OS(
                    tag = "centos",
                    name = "CentOS",
                    description = "Community Enterprise Operating System",
                    os_distro_id = dists["rhel"].id
                ).add(),
                "fedora": OS(
                    tag = "fedora",
                    name = "Fedora",
                    description = "Fedora Linux",
                    os_distro_id = dists["rhel"].id
                ).add(),
                "ubuntu": OS(
                    tag = "ubuntu",
                    name = "Ubuntu",
                    description = "Canonical Ubuntu",
                    os_distro_id = dists["debian"].id
                ).add()
            }

        return apps
