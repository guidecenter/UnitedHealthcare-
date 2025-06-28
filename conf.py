# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# If extensions or modules to document with autodoc are in another directory,
# add these directories to sys.path here.
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Activate UHC Account'
copyright = '2025, UnitedHealthcare'
author = 'UnitedHealthcare'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "How to Activate Your UnitedHealthcare Account – Quick Start Guide"

# Optional short title (e.g., for nav bar)
html_short_title = "Activate UHC Account"

# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'

# Choose a theme (uncomment and set if needed)
# html_theme = 'sphinx_rtd_theme'

# Hide "View page source"
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True
raw_enabled = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Paths to templates and static files (if you use them)
# templates_path = ['_templates']
# html_static_path = ['_static']  # Uncomment if using CSS, JS, images, etc.

# Patterns to ignore when looking for source files
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
