from distutils.core import setup
import py2exe

setup(
    version = "1.0.1",
    description = "A compiler cache for Microsoft Visual Studio.",
    name = "CLCache",
    console = ["clcache.py"],
	options = {"py2exe":{"optimize": 2}}
    )