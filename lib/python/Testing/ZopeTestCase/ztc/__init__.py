#
# ZopeTestCase public interface
#

# $Id: __init__.py,v 1.1 2005/02/25 11:01:07 shh42 Exp $

import Testing.ZopeTestCase
__path__.extend(Testing.ZopeTestCase.__path__)

from Testing.ZopeTestCase import *
from Testing.ZopeTestCase.utils import *

