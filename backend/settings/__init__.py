from .base import *

try:
    from .local import *
except ImportError:
    print("Create file local.py from local.py.skeleton");