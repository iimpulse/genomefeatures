import ipywidgets as widgets
from traitlets import Unicode, Float

@widgets.register
class HelloWorld(widgets.DOMWidget):
    """An example widget."""
    _view_name = Unicode('HelloView').tag(sync=True)
    _model_name = Unicode('HelloModel').tag(sync=True)
    _view_module = Unicode('genomefeatures').tag(sync=True)
    _model_module = Unicode('genomefeatures').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)
    # value = Unicode('Hello World B').tag(sync=True)  # this is the model value, if provided it will default to this

@widgets.register
class GenomeFeature(widgets.DOMWidget):
    """An example widget."""
    _view_name = Unicode('SliderView').tag(sync=True)
    _model_name = Unicode('SliderModel').tag(sync=True)
    _view_module = Unicode('genomefeatures').tag(sync=True)
    _model_module = Unicode('genomefeatures').tag(sync=True)
    _view_module_version = Unicode('^0.1.0').tag(sync=True)
    _model_module_version = Unicode('^0.1.0').tag(sync=True)
    value = Float(80.0).tag(sync=True)
