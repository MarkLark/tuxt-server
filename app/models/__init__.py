from . import app, article, chapter, os

__all__ = [ "app", "article", "chapter", "os" ]

models = None

if models is None:
    models = app.models
    models.extend( article.models )
    models.extend( chapter.models )
    models.extend( os.models )


def add_defaults( store ):
    os.add_defaults( store )
    app.add_defaults( store )
