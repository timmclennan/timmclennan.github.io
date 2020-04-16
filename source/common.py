import os.path

SITE_ROOT = os.path.dirname(os.path.dirname(__file__))
GOOGLE_SHEET_BASE = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQCN9pL21lGy3XPBhKwMX7jT1_SG-Sb_4ZWZ1I0Ctd-0vNhtmH4gFKaLsV5jhz4vSjYlQ9NR_fXF_b6/'

def site_file(*args):
    return os.path.join(SITE_ROOT, *args)

def setup():
    import plotly.io
    plotly.io.renderers.default = 'notebook_connected'
    plotly.io.templates.default = 'plotly_white'

def get_plotly_template(name=None):
    from plotly.io import templates
    return templates[templates.default if name is None else name]

setup()
