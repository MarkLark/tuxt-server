from dstore import Model as M, var, mod


class Version( M ):
    _namespace = "os.version"
    _vars = [
        var.RowID,
        var.ForeignKey( "os.os" ),
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
        from .OS import OS
        from datetime import date
        os = OS.defaults()

        o = os["centos"]
        o.add_version( major = 7, minor = 3, build = 1611, name = "v7.3", release_date = date( 2016, 11, 01 ))
        o.add_version( major = 7, minor = 2, build = 1511, name = "v7.2", release_date = date( 2015, 11, 01 ))
        o.add_version( major = 7, minor = 1, build = 1503, name = "v7.1", release_date = date( 2015, 03, 01 ))
        o.add_version( major = 7, minor = 0, build = 1406, name = "v7.0", release_date = date( 2014, 06, 01 ))
        o.add_version( major = 6, minor = 8,               name = "v6.8", release_date = date( 2015, 10, 01 ))

        o = os["ubuntu"]
        o.add_version( major = 17, minor = 04, release_date = date(2017, 04, 01), name = "Zesty Zapus"      )
        o.add_version( major = 16, minor = 10, release_date = date(2016, 10, 13), name = "Yakkety Yak"      )
        o.add_version( major = 16, minor = 04, release_date = date(2016, 04, 21), name = "Xenial Xerus"     )
        o.add_version( major = 15, minor = 10, release_date = date(2015, 10, 22), name = "Wily Werewolf"    )
        o.add_version( major = 15, minor = 04, release_date = date(2015, 04, 23), name = "Vivid Vervet"     )
        o.add_version( major = 14, minor = 10, release_date = date(2014, 10, 23), name = "Utopic Unicorn"   )
        o.add_version( major = 14, minor = 04, release_date = date(2014, 04, 17), name = "Trusty Tahr"      )
        o.add_version( major = 13, minor = 10, release_date = date(2013, 10, 17), name = "Saucy Salamander" )
        o.add_version( major = 13, minor = 04, release_date = date(2013, 04, 25), name = "Raring Ringtail"  )
        o.add_version( major = 12, minor = 10, release_date = date(2012, 10, 18), name = "Quantal Quetzal"  )
        o.add_version( major = 12, minor = 04, release_date = date(2012, 04, 26), name = "Precise Pangolin" )

