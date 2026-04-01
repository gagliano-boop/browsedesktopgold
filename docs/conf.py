import os
import sys

sys.path.insert(0, os.path.abspath('.'))

# Project info
project = 'Browse Desktop Gold'
author = 'Heide Fasnacht'
release = '1.0'

# General config
extensions = []

templates_path = ['_templates']
exclude_patterns = []

# HTML settings
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# ✅ Google Verification (WORKING METHOD)
html_context = {
    "metatags": '<<meta name="msvalidate.01" content="41D405A709311D11A1F376A3A9030AB4" />" />'
}
