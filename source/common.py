import os.path

SITE_ROOT = os.path.dirname(os.path.dirname(__file__))

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
