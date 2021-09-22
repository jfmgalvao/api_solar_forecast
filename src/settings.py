from os.path import abspath, dirname, join

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

PROJECT_ROOT = abspath(dirname(__file__))
RESOURCE_PATH = join(PROJECT_ROOT, 'resources')
LOG_PATH = join(PROJECT_ROOT[:-3], 'log')
