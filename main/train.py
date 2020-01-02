import argparse
from utils.misc import read_config
def main(args):
    read_config(args.config) 
    pass
if __name__ is '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--config',type=str)
    args = parser.parse_args()
    main(args)
    pass
