
import sysconfig
print(sysconfig.get_config_var("Py_GIL_DISABLED"))

import sys
result = sys._is_gil_enabled()  # returns a boolean value
print(result)


