import sys
import os
import argparse
import json
sys.path.append(os.path.dirname(os.path.abspath(__file__)).split("/covalytics")[0])

from covalytics.tests import test_runner
from covalytics.parsers import jacoco

def start():
    args = parse_args()

    if args.action == 'analyze':
        if args.coverage_tool == 'jacoco':
            print 'Analyzing JaCoCo coverage data for file %s' % args.file
            f = open(args.file, 'r')
            extracted_data = jacoco.analyze(f)
            f.close()
            save_extracted_data(extracted_data, args.file.split('/').pop().split('.')[0])
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

def save_extracted_data(data, filename):
    f = open('files/jacoco/results/' + filename + '.json', 'w')
    f.write(json.dumps(data))
    f.close()

if __name__ == '__main__':
    start()
