import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)).split("/covalytics")[0])

from covalytics.tests import test_runner

if __name__ == '__main__':
    if 'test' in sys.argv:
        test_runner.run()
    else:
        print "Invalid arguments"
