from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'instructor_task.tasks_helper.grades')

from lms.djangoapps.instructor_task.tasks_helper.grades import *
