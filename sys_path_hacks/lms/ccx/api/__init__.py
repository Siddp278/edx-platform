from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'ccx.api')

from lms.djangoapps.ccx.api import *
