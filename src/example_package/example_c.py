# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

# Try use the C extension, but if it isn't available, provide a dummy
# implementation.

try:
    from example_package._example_c import return_ten
except ImportError:  # pragma: no cover

    def return_ten():
        pass

    is_extension = False
else:  # pragma: no cover
    is_extension = True
