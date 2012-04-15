import sys
import os
import argparse
import json
sys.path.append(os.path.dirname(os.path.abspath(__file__)).split("/covalytics")[0])

from covalytics.tests import test_runner
from covalytics.parsers import jacoco

def start():
    args = parse_args()

    if args.action == 'extract':
        if args.coverage_tool == 'jacoco':
            print 'Analyzing JaCoCo coverage data for file %s' % args.directory
            directory = args.directory + 'coverage/'
            files = os.listdir(directory) 

            for xml_file in files:
                f = open(directory + xml_file, 'r')
                extracted_data = jacoco.analyze(f)
                f.close()
                save_extracted_data(extracted_data, args.directory, xml_file.split('.xml')[0])
    elif args.action == 'analyze':
        f = open(args.suite, 'r')
        f.close()
    elif args.action == 'test':
        test_runner.run()

def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='action')

    parser_extract = subparsers.add_parser('extract', help='Analyzes a particular file and type.')
    parser_extract.add_argument('coverage_tool', action='store', choices=['jacoco'], type=str, help='JaCoco coverage analysis')
    parser_extract.add_argument('--directory', nargs='?', required=True, help='File where the coverage data is stored')

    parser_analyze = subparsers.add_parser('analyze', help='Used to analyze and combine multiple coverage files and generate higher level metrics.')
    parser_analyze.add_argument('--suite', nargs='?', required=True, help='File containing the suite of coverage data files to analyze.')

    parser_test = subparsers.add_parser('test', help='Runs the test suite')
    
    return parser.parse_args()

def save_extracted_data(data, directory, filename):
    f = open(directory + '/results/' + filename + '.json', 'w')
    f.write(json.dumps(data))
    f.close()

if __name__ == '__main__':
    start()
