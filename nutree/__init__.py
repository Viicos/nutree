# -*- coding: utf-8 -*-
"""
Current version number.

See https://www.python.org/dev/peps/pep-0440

Examples
    Pre-releases (alpha, beta, release candidate):
        '3.0.0a1', '3.0.0b1', '3.0.0rc1'
    Final Release:
        '3.0.0'
    Developmental release (to mark 3.0.0 as 'used'. Don't publish this):
        '3.0.0.dev1'
NOTE:
    When pywin32 is installed, number must be a.b.c for MSI builds?
    "3.0.0a4" seems not to work in this case!
"""
# flake8: noqa
__version__ = "0.0.1-a4"

from .node import AmbigousMatchError, IterMethod, Node, TreeError, UniqueConstraintError
from .tree import Tree

__all__ = [
    Tree,
    Node,
    IterMethod,
    TreeError,
    AmbigousMatchError,
    UniqueConstraintError,
]
