from .App import App
from .Version import Version
from .Category import Category
from .SubCategory import SubCategory


__all__ = [ "App", "Version", "Category", "SubCategory" ]
models = [ App, Version, Category, SubCategory ]


def add_defaults( store ):
    SubCategory.defaults()
    App.defaults()
    Version.defaults()
