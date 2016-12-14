from os import environ

print environ.values()

if "build_environment" in environ.keys():
    if environ["build_environment"] == "PROD":
        from .production import *

    if environ["build_environment"] == "JENKINS":
        from .dev import *

else:
    from .dev import *
