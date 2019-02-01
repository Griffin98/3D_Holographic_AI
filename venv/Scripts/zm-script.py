#!C:\Users\Dhyey\PycharmProjects\Server\venv\Scripts\python3.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'zm==1.0','console_scripts','zm'
__requires__ = 'zm==1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('zm==1.0', 'console_scripts', 'zm')()
    )
