# -*- coding: utf-8 -*-
import sys, os

pypuppetdb_root = os.path.dirname(os.path.abspath('.'))
sys.path.insert(0, pypuppetdb_root)
from pypuppetdb import __version__

# -- General configuration -----------------------------------------------------

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode']

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'pypuppetdb'
copyright = u'2013, Daniele Sluijters'

version = __version__
release = version

language = 'en'

exclude_patterns = ['_build']

pygments_style = 'sphinx'

# -- Options for HTML output ---------------------------------------------------

html_theme = 'default'

html_static_path = ['_static']

htmlhelp_basename = 'pypuppetdbdoc'

# -- Options for LaTeX output --------------------------------------------------

latex_documents = [
  ('index', 'pypuppetdb.tex', u'pypuppetdb Documentation',
   u'Daniele Sluijters', 'manual'),
]


# -- Options for manual page output --------------------------------------------

man_pages = [
    ('index', 'pypuppetdb', u'pypuppetdb Documentation',
     [u'Daniele Sluijters'], 1)
]

# -- Options for Texinfo output ------------------------------------------------

texinfo_documents = [
  ('index', 'pypuppetdb', u'pypuppetdb Documentation',
   u'Daniele Sluijters', 'pypuppetdb', 'Library to work with the PuppetDB REST API.',
   'Miscellaneous'),
]
