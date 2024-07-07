import argparse
import importlib.resources as importlib_resources
import subprocess as sp
from pathlib import Path


pkg = importlib_resources.files('deploy_helper')


def setup_init_cmd(args):
    sp.run(pkg / 'cmd/setup_init', cwd=Path.cwd())


def setup_destroy_cmd(args):
    sp.run(pkg / 'cmd/setup_destroy', cwd=Path.cwd())


def parse_args():
    parser = argparse.ArgumentParser(description='Deploy Helper')
    subparsers = parser.add_subparsers()
    
    setup = subparsers.add_parser('setup', help='Setup')
    setup_subparsers = setup.add_subparsers()
    
    setup_init = setup_subparsers.add_parser('init', help='Init setup')
    setup_init.set_defaults(run=setup_init_cmd)
    
    setup_init = setup_subparsers.add_parser('destroy', help='Destroy setup')
    setup_init.set_defaults(run=setup_destroy_cmd)

    return parser.parse_args()


def main():
    args = parse_args()
    args.run(args)


if __name__ == '__main__':
    main()
