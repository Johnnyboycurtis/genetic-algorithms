import sys
from time import sleep
import functools
print = functools.partial(print, flush=True)

for i in range(3):
    sleep(i)
    sys.stdout.write('sleeping {}\n'.format(i))
    sys.stdout.flush()

for i in range(3):
    sleep(i)
    print('sleeping {}'.format(i), flush=True)
    sys.stdout.flush()

for x in range(10000):
    print( "HAPPY >> %s <<\r" % str(x), sys.stdout.flush())
