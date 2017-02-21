from dstore import Model as M, var, mod
from .Category import Category


class SubCategory( M ):
    _namespace = "app.subcategory"
    _vars = [
        var.RowID,
        var.ForeignKey( "app.category" ),
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
        cats = Category.defaults()

        scats = {}
        for c in SubCategory.all(): scats[ c.tag ] = c

        if len( scats ) == 0:
            scats = {
                "os_rhel": SubCategory(
                    app_category_id = cats["os"].id,
                    tag             = "os_rhel",
                    name            = "RHEL",
                    description     = "RedHat Enterprise Linux"
                ).add(),
                "os_debian": SubCategory(
                    app_category_id = cats["os"].id,
                    tag             = "os_debian",
                    name            = "Debian",
                    description     = "Debian Linux"
                ).add(),
                "http_server": SubCategory(
                    app_category_id = cats["http"].id,
                    tag             = "http_server",
                    name            = "Server",
                    description     = "HTTP Server"
                ).add(),

                "http_client": SubCategory(
                    app_category_id = cats["http"].id,
                    tag             = "http_client",
                    name            = "Client",
                    description     = "HTTP Client"
                ).add()
            }

        return scats
