import argparse
import subprocess as sp


def setup_init_cmd(args):
    sp.run('./setup_init')


def parse_args():
    parser = argparse.ArgumentParser(description='Deploy Helper')
    subparsers = parser.add_subparsers()
    
    setup = subparsers.add_parser('setup', help='Setup')
    setup_subparsers = setup.add_subparsers()
    
    setup_init = setup_subparsers.add_parser('init', help='Init setup')
    setup_init.set_defaults(run=setup_init_cmd)
    
    return parser.parse_args()


def main():
    args = parse_args()
    args.run(args)


if __name__ == '__main__':
    main()
