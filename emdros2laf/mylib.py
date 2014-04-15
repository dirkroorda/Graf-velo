import sys
import datetime
import time
import subprocess
import pprint

# PRETTY PRINTING of DATA STRUCTURES
# for development and debugging

pp = pprint.PrettyPrinter(indent = 4)

def pretty(data):
    pp.pprint(data)

# LOW-LEVEL functions
#
# The items method in the config module gives the items of a section.
# But it adds the items of the default section.
# Mostly we want the items that strictly belong to the indicated section.

def camel(text):
    ''' Render text in camelcase, removing spaces, and let the first word start with lower case
    '''
    words = text.split(" ")
    return ''.join([words[x].capitalize() if x > 0 else words[x] for x in range(len(words))])

def fillup(size, val, lst):
    ''' Fill lst up with dummy elements val until it has size
    '''
    return [lst[x] if x < len(lst) else val for x in range(size)] 
 
def today():
    return datetime.date.today()

def run(cmd):
    subprocess.check_call(cmd + ' 2>&1', shell = True)

def runx(cmd):
    error = subprocess.call(cmd + ' 2>&1', shell = True)

class Timestamp():
    timestamp = None

    def __init__(self):
        self.timestamp = time.time()

    def elapsed(self):
        interval = time.time() - self.timestamp
        if interval < 10:
            return "{: 2.2f}s".format(interval)
        interval = int(round(interval))
        if interval < 60:
            return "{:>2d}s".format(interval)
        if interval < 3600:
            return "{:>2d}m {:>02d}s".format(interval // 60, interval % 60)
        return "{:>2d}h {:>02d}m {:>02d}s".format(interval // 3600, (interval % 3600) // 60, interval % 60)

    def progress(self, msg):
        print("{} {}".format(self.elapsed(), msg))
        sys.stdout.flush()
