__version__ = "1.0.4"

import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

from .pondcleaner import *
from .demo import *
