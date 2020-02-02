"""
molecool
A Python package for analyzing and visualizing xyz files. For MolSSI Workshop Python Package development workshop.
"""

# Add imports here
from .measure import calculate_angle, calculate_distance
from .visualize import draw_molecule, draw_bond_histogram
from .molecule import build_bond_list
from .atom_data import atomic_weights, atom_colors

import molecool.io

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
