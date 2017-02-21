from dstore import Model as M, var


class ChapterList( M ):
    _namespace = "article.chapterlist"
    _vars = [
        var.RowID,
        var.ForeignKey( "article.article" ),
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
