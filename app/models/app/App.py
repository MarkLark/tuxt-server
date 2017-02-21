from dstore import Model as M, var, mod
from .SubCategory import SubCategory


class App( M ):
    _namespace = "app.app"
    _vars = [
        var.RowID,
        var.String( "tag", 32, mods = [ mod.NotNull() ] ),
        var.String( "name", 32, mods = [ mod.NotNull() ] ),
        var.Text( "description" ),
        var.ForeignKey( "apps.subcategory" )
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
        kwargs["app_app_id"] = self.id
        return Version( **kwargs ).add()

    @staticmethod
    def defaults():
        scats = SubCategory.defaults()

        apps = {}
        for a in App.all(): apps[ a.tag ] = a

        if len( apps ) == 0:
            apps = {
                "centos": App(
                    tag = "centos",
                    name = "CentOS",
                    description = "Community Enterprise Operating System",
                    app_subcategory_id = scats["os_rhel"].id
                ).add(),
                "ubuntu": App(
                    tag = "ubuntu",
                    name = "Ubuntu",
                    description = "Canonical Ubuntu",
                    app_subcategory_id = scats["os_debian"].id
                ).add(),
                "nginx": App(
                    tag = "nginx",
                    name = "Nginx",
                    description = "Nginx Web Server",
                    app_subcategory_id = scats["http_server"].id
                ).add(),

                "httpd": App(
                    tag = "httpd",
                    name = "Apache",
                    description = "Apache Web Server",
                    app_subcategory_id = scats["http_server"].id
                ).add(),

                "curl" : App(
                    tag = "curl",
                    name = "Curl",
                    description = "Curl Web Client",
                    app_subcategory_id = scats["http_client"].id
                ).add(),

                "wget" : App(
                    tag = "wget",
                    name = "Wget",
                    description = "Wget Web Client",
                    app_subcategory_id = scats["http_client"].id
                ).add()
            }

        return apps
