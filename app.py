from __future__ import print_function

from paths import *


def init():
    if not os.path.exists(TT_DIR):
        os.mkdir(TT_DIR)
        print("Creating TimeTracker home directory at {0}".format(TT_DIR))
    else:
        print("Found TimeTracker home directory at {0}".format(TT_DIR))


if __name__ == '__main__':
    init()

    parser = argparse.ArgumentParser()
    parser.add_argument("echo", help="echo the string you use here")
    args = parser.parse_args()
    print()
    args.echo
