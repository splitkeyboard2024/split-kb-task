from lines import parse
import json

FILE_NAME = 'tests.json'

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


with open(FILE_NAME) as tests_file:
    raw = tests_file.read()
    tests = json.loads(raw)
    max_score = len(tests)
    scored = 0
    bad = []
    for test in tests:
        parsed = parse(test['input'])
        if parsed == test['output']:
            scored += 1
        else:
            test['parsed'] = parsed
            bad.append(test)
    
    print(f'{bcolors.ENDC}#'*80)
    for test in bad:
        input = test['input']
        output = test['output']
        parsed = test['parsed']
        print(f'{bcolors.BOLD}For input:\n{bcolors.ENDC}{input}\n{bcolors.BOLD}The expected output is:\n{bcolors.ENDC}{output}\n{bcolors.BOLD}Received output is:\n{bcolors.ENDC}{parsed}')
        print('_'*80)
    print(f'{bcolors.BOLD}FINAL SCORE: {scored}/{max_score}.')

