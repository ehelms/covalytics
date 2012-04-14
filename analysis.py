import sys
import os
import argparse
sys.path.append(os.path.dirname(os.path.abspath(__file__)).split("/covalytics")[0])

from covalytics.tests import test_runner


def start():
    args = parse_args()

    if args.action == 'analyze':
        if args.coverage_tool == 'jacoco':
            print 'Analyzing JaCoCo coverage data for file %s' % args.file
    elif args.action == 'test':
        test_runner.run()

def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='action')

    parser_analyze = subparsers.add_parser('analyze', help='Analyzes a particular file and type.')
    parser_analyze.add_argument('coverage_tool', action='store', choices=['jacoco'], type=str, help='JaCoco coverage analysis')
    parser_analyze.add_argument('--file', nargs='?', required=True, help='File where the coverage data is stored')

    parser_test = subparsers.add_parser('test', help='Runs the test suite')
    
    return parser.parse_args()


if __name__ == '__main__':
    start()
