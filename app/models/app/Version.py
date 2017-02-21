from dstore import Model as M, var, mod


class Version( M ):
    _namespace = "app.version"
    _vars = [
        var.RowID,
        var.ForeignKey( "app.app" ),
        var.Number( "major",  default = 0, mods = [ mod.NotNull() ]),
        var.Number( "minor",  default = 0, mods = [ mod.NotNull() ]),
        var.Number( "bugfix", default = 0, mods = [] ),
        var.Number( "build",  default = 0, mods = [] ),
        var.String( "name", 32, mods = [] ),
        var.Date( "release_date" )
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
        from .App import App
        from datetime import date
        apps = App.defaults()

        app = apps["nginx"]
        app.add_version( major = 1, minor = 6, bugfix = 1, name = "v1.6.1", release_date = date( 2017, 01, 27) )
        app.add_version( major = 1, minor = 5, bugfix = 1, name = "v1.5.1", release_date = date( 2016, 06, 27) )

        app = apps["centos"]
        app.add_version( major = 7, minor = 0, build = 1511, name = "v7.0", release_date = date( 2015, 11, 01 ))
        app.add_version( major = 6, minor = 8,               name = "v6.8", release_date = date( 2015, 10, 01 ))
