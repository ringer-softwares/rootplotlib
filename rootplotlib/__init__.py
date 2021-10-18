
import gc

__all__ = ['set_figure', 'get_figure', 'clear']

from . import core
__all__.extend( core.__all__ )
from .core import *

global figure
figure = Figure()

def set_figure( canvas ):
    global figure
    figure.set_canvas( canvas )

def get_figure():
    global figure
    return figure

def clear():
    global figure
    figure.clear()

from . import axis
__all__.extend( axis.__all__ )
from .axis import *

from . import canvas
__all__.extend( canvas.__all__ )
from .canvas import *

from . import plots
__all__.extend( plots.__all__ )
from .plots import *

from . import hists
__all__.extend( hists.__all__ )
from .hists import *

from . import legends
__all__.extend( legends.__all__ )
from .legends import *

from . import styles
__all__.extend( styles.__all__ )
from .styles import *
