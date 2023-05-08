__version__ = "0.0.0"

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

from .pondcleaner import *
from .demo import *
