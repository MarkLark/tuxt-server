from .OS import OS
from .Version import Version
from .Distro import Distro


__all__ = [ "OS", "Version", "Distro" ]
models = [ OS, Version, Distro ]


def add_defaults( store ):
    Distro.defaults()
    OS.defaults()
    Version.defaults()
