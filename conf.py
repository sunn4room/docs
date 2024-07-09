extensions = [
    'myst_parser',
    'sphinx_book_theme',
    'plantweb.directive'
]

source_suffix = ['.rst', '.md']

master_doc = 'index'

project = 'sunn4room'

html_title = "sunn4room's docs"
html_theme = 'sphinx_book_theme'
html_theme_options = {
    'repository_url': 'https://github.com/sunn4room/docs',
    'use_repository_button': True,
}

