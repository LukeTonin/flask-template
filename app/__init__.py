"""Main application package."""

import os
import inspect

# paths to non Python files to make the package import system work with script style importing
ROOT_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

